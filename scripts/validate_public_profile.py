#!/usr/bin/env python3
"""Validate public profile content without printing candidate sensitive values."""

from __future__ import annotations

import re
import subprocess
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    category: str


def candidate_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / item.decode() for item in result.stdout.split(b"\0") if item]


def text_files(paths: list[Path]) -> dict[Path, str]:
    contents: dict[Path, str] = {}
    for path in paths:
        if not path.is_file():
            continue
        data = path.read_bytes()
        if b"\0" in data:
            continue
        try:
            contents[path] = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
    return contents


def line_for(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def add_pattern_findings(
    findings: set[Finding], contents: dict[Path, str], category: str, pattern: re.Pattern[str]
) -> None:
    for path, text in contents.items():
        for match in pattern.finditer(text):
            findings.add(Finding(relative(path), line_for(text, match.start()), category))


def check_sensitive_content(findings: set[Finding], contents: dict[Path, str]) -> None:
    patterns = {
        "private key marker": re.compile("-" * 5 + r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
        "GitHub token": re.compile(r"\b(?:github_pat_|gh[pousr]_)[A-Za-z0-9_]{20,}\b"),
        "OpenAI API key": re.compile(r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{20,}\b"),
        "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "live payment key": re.compile(r"\b(?:sk|rk|pk)_live_[A-Za-z0-9]{16,}\b"),
        "UUID": re.compile(
            r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-"
            r"[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b"
        ),
        "Cloudflare identifier assignment": re.compile(
            r"\b(?:account_id|database_id)\s*[:=]\s*[\"']?[0-9a-fA-F]{32}\b"
        ),
        "macOS home path": re.compile(
            re.escape("/" + "Users/")
            + r"(?!(?:username|user|example|some|not|me|directory|<[^>]+>)(?:/|\b))[^/\s\"'`]+"
        ),
        "Linux home path": re.compile(
            re.escape("/" + "home/")
            + r"(?!(?:username|user|example|some|not|me|directory|<[^>]+>)(?:/|\b))[^/\s\"'`]+"
        ),
        "Windows home path": re.compile(
            r"[A-Za-z]:[\\/]+" + "Users" + r"[\\/]+(?!(?:username|user|example)[\\/])[^\\/\s\"'`]+"
        ),
    }

    for category, pattern in patterns.items():
        add_pattern_findings(findings, contents, category, pattern)

    email_pattern = re.compile(r"\b[\w.%+-]+@([\w.-]+\.[A-Za-z]{2,})\b")
    allowed_addresses = {"x@y.com"}
    allowed_domains = {"example.com", "mycompany.com", "users.noreply.github.com"}
    for path, text in contents.items():
        for match in email_pattern.finditer(text):
            if (
                match.group(0).lower() not in allowed_addresses
                and match.group(1).lower() not in allowed_domains
            ):
                findings.add(Finding(relative(path), line_for(text, match.start()), "email literal"))


def check_tracked_names(findings: set[Finding], paths: list[Path]) -> None:
    forbidden_names = {".DS_Store", ".env", "auth.json", "credentials.json"}
    forbidden_suffixes = {".key", ".pem", ".p12", ".pfx"}
    for path in paths:
        if path.name in forbidden_names or path.suffix.lower() in forbidden_suffixes:
            findings.add(Finding(relative(path), 1, "forbidden public filename"))


def check_markdown_links(findings: set[Finding], contents: dict[Path, str]) -> int:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    checked = 0
    for path, text in contents.items():
        if path.suffix.lower() != ".md":
            continue
        for match in link_pattern.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and ">" in target:
                target = target[1 : target.index(">")]
            else:
                target = target.split(maxsplit=1)[0]
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            checked += 1
            local_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            resolved = (path.parent / local_target).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                findings.add(Finding(relative(path), line_for(text, match.start()), "link escapes repository"))
            elif not resolved.exists():
                findings.add(Finding(relative(path), line_for(text, match.start()), "missing local link"))
    return checked


def check_codex_config(findings: set[Finding]) -> None:
    path = ROOT / "codex" / "config.example.toml"
    try:
        config = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError):
        findings.add(Finding(relative(path), 1, "invalid TOML"))
        return

    expected_keys = {"approval_policy", "sandbox_mode", "allow_login_shell", "sandbox_workspace_write"}
    if set(config) != expected_keys:
        findings.add(Finding(relative(path), 1, "unexpected public config keys"))
    if config.get("approval_policy") != "on-request":
        findings.add(Finding(relative(path), 1, "approval policy drift"))
    if config.get("sandbox_mode") != "workspace-write":
        findings.add(Finding(relative(path), 1, "sandbox mode drift"))
    if config.get("allow_login_shell") is not False:
        findings.add(Finding(relative(path), 1, "login shell hardening drift"))
    if config.get("sandbox_workspace_write") != {"network_access": False}:
        findings.add(Finding(relative(path), 1, "sandbox network policy drift"))


def check_brewfile(findings: set[Finding]) -> None:
    path = ROOT / "Brewfile"
    formulas: list[str] = []
    statement = re.compile(r'^brew "([a-z0-9@+_.-]+)"$')
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        match = statement.fullmatch(line)
        if not match:
            findings.add(Finding(relative(path), line_number, "unsupported Brewfile statement"))
            continue
        formulas.append(match.group(1))
    if len(formulas) != len(set(formulas)):
        findings.add(Finding(relative(path), 1, "duplicate Brewfile formula"))


def check_profile_contract(findings: set[Finding]) -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    required = {
        "AisleStage repository": "https://github.com/kyeunga25/aislestage",
        "Wallpect release": "/wallpect/releases/tag/v0.2.2",
        "Anisonary release": "/anisonary/releases/tag/v1.1.0",
        "Personal Space release": "/personal-space/releases/tag/v0.6.0",
        "AisleStage release": "/aislestage/releases/tag/v0.5.1",
        "RigStage release": "/pc-ai-3d-builder/releases/tag/v1.0.1",
        "released products group": "## 已發布產品 / Released products",
        "private beta group": "## 私人測試與早期開發 / Private beta and early work",
    }
    for label, fragment in required.items():
        if fragment not in text:
            findings.add(Finding(relative(path), 1, f"missing profile contract: {label}"))

    deprecated = {
        "legacy repository name": "marketing_image_ai_web",
        "broken preview hostname": "motive-ecommerce-visuals",
        "stale Anisonary version": "v0.4.0",
    }
    for label, fragment in deprecated.items():
        offset = text.find(fragment)
        if offset >= 0:
            findings.add(Finding(relative(path), line_for(text, offset), label))


def main() -> int:
    findings: set[Finding] = set()
    paths = candidate_files()
    contents = text_files(paths)

    check_tracked_names(findings, paths)
    check_sensitive_content(findings, contents)
    local_links = check_markdown_links(findings, contents)
    check_codex_config(findings)
    check_brewfile(findings)
    check_profile_contract(findings)

    if findings:
        for finding in sorted(findings):
            print(f"{finding.path}:{finding.line}: {finding.category}")
        print(f"FAIL: {len(findings)} public-content finding(s); candidate values were not printed.")
        return 1

    print(
        f"PASS: {len(paths)} candidate files scanned, {local_links} local Markdown links checked, "
        "and the public Codex/Brewfile contracts validated."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
