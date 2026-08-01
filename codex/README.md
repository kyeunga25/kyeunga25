# Public Codex Development Setup

這個目錄記錄一套可公開、可審閱的 Codex 開發基線。它不是個人 `CODEX_HOME` 的備份，也不會複製真實的全域 `config.toml`。

This directory documents a public-safe Codex development baseline. It is not a backup of a personal `CODEX_HOME`, and it does not mirror a live global `config.toml`.

## 包含內容 / Included

- [`config.example.toml`](./config.example.toml) — 適合可信任 repository 的最小權限起點。
- [`AGENTS.example.md`](./AGENTS.example.md) — repository 結構、安全邊界、驗證及 Git 工作方式的通用範例。

Codex 會在每次 run 開始時讀取適用範圍內的 `AGENTS.md`，由 repository root 向目前目錄合併，較接近工作目錄的指引優先。使用者層級設定應保留在本機，只有 repository 特定且適合團隊共享的設定才放進 `.codex/config.toml`。Project config 只會在 repository 被標記為可信任時載入。

Codex reads applicable `AGENTS.md` files at the start of each run, merging guidance from the repository root toward the working directory so closer instructions take precedence. User-level settings should stay local; only repository-specific settings that are safe to share belong in `.codex/config.toml`. Project config is loaded only for trusted repositories.

## 安全採用 / Safe adoption

這份範例刻意使用按需要批准、只限 workspace 寫入、停用 sandbox network 及非 login shell。只有在目標 repository 已記錄更窄或更廣的需要時才調整這些值。

The example deliberately uses on-request approvals, workspace-only writes, disabled sandbox network access, and non-login shells. Change those values only when the target repository documents a narrower or broader requirement.

先閱讀範例，再把需要的部分合併到目標 repository。以下指令只適合目標檔案尚不存在的情況：

```bash
mkdir -p .codex
test ! -e .codex/config.toml && cp codex/config.example.toml .codex/config.toml
test ! -e AGENTS.md && cp codex/AGENTS.example.md AGENTS.md
```

If either target already exists, merge the relevant sections manually instead of overwriting it.

## 僅保留在本機 / What stays local

| 類別 / Category | 原因 / Why it is not published |
| --- | --- |
| Authentication files, tokens, and keychain data | 屬於憑證，不應進入 Git。 / Credentials never belong in Git. |
| Session history, logs, caches, and memory stores | 可能包含程式碼、提示、路徑或其他私人工作內容。 / They can contain code, prompts, paths, or other private work context. |
| Raw global `config.toml` | 可能混合本機路徑、受信任項目、工具啟動參數與桌面設定。 / It may mix machine paths, trusted projects, tool launch arguments, and desktop settings. |
| Private MCP endpoints and environment values | 可能暴露內部服務或 bearer credentials。 / They can expose internal services or bearer credentials. |
| Personal UI, model, and notification choices | 不屬於可移植的 repository 開發契約。 / They are not part of a portable repository contract. |

## 公開前檢查 / Publication checklist

公開 Codex 設定前，至少應完成以下檢查：

1. 只選擇 repository 需要的設定，不複製整份全域 config。
2. 移除絕對路徑、帳戶或 workspace identifier、私人 URL、雜湊及裝置資料。
3. 確認沒有 auth、history、session、log、cache、environment value 或 secret。
4. 讓 `AGENTS.md` 保持簡短、可執行，並列出真實的 build、test、lint 與完成條件。
5. 在提交前檢查 staged diff，並以獨立工具重新掃描敏感資料。

## 官方參考 / Official references

- [Codex configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic)
- [AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Approvals and sandboxing](https://learn.chatgpt.com/docs/agent-approvals-security)
