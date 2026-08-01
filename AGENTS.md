# Repository Guidance

## 目的 / Purpose

- `README.md` 是公開 GitHub Profile 首頁；內容以繁體中文為主並提供清晰英文。
- This repository publishes the GitHub profile and a small, reviewable development setup.
- `k-y.cc` 是獨立網站及 repository。不要把兩者的 source、deployment 或 release 狀態混合。

## 公開內容 / Public content

- 專案名稱、repository、release、live URL 及狀態必須以目前公開證據核對。
- 明確區分 `Released`、`Public`、`Closed beta`、`Invite-only` 與 `Early MVP`；preview、CI 或本機 branch 不是 production 證據。
- 只描述已合併、可公開驗證的能力。不要加入沒有可重現證據的使用量、效能或商業指標。
- 保持文案簡潔、專業及以產品能力為中心，不加入對話背景、私人動機或未公開 roadmap。

## 安全邊界 / Safety boundaries

- 不得提交憑證、環境值、帳戶或部署 identifier、私人 URL、真實本機路徑、logs、sessions、caches 或使用者資料。
- 公開 Codex 設定只可使用 portable examples；不得複製真實全域設定、trusted-project 清單、啟動參數或個人介面設定。
- 測試資料、畫面及例子必須是合成、獲授權或已明確批准公開的內容。
- 不要加入付款供應商、merchant mapping、checkout、subscription 或跨產品付款基礎設施資料。
- 未經明確批准，不要新增或更改 repository license 或對外授權條款。
- 不執行廣泛或破壞性刪除；任何刪除都需要明確目標及批准。

## Repository structure

- `README.md` — Profile 首頁及目前公開項目狀態。
- `codex/` — 可參考、可審閱的公開 Codex examples，不是本機 `CODEX_HOME` 備份。
- `dotfiles/` 與 `Brewfile` — 經篩選的可攜設定，不是現機狀態 dump。
- `scripts/validate_public_profile.py` — 本地與 CI 共用的公開內容檢查。
- `.github/workflows/validate-public-profile.yml` — 最小權限的 pull request／`main` validation。

## 驗證 / Verification

修改後至少執行：

```bash
python3 scripts/validate_public_profile.py
git diff --check
```

發布前亦要：

- 使用 GitHub Markdown rendering 核對 Profile 的 headings、links 與 mobile-readable structure；
- 逐一核對外部 repository、latest release 及 live route，並移除 404 或舊 preview URL；
- 檢查 staged／unstaged diff 及所有擬加入的 untracked files；
- 以不輸出候選值的方式掃描 secret markers、私人路徑、email、UUID 與受保護服務 mapping；
- 確認 commit author 使用公開安全的 GitHub noreply metadata。

## Git

- 從最新 `main` 建立 `codex/` 分支，並只 stage 已審閱且屬於本次範圍的檔案。
- Commit 與 pull request metadata 保持簡短、中性和專業。
- 合併前核對 PR head SHA 及 checks；合併後確認 local `main`、`origin/main` 與 GitHub `main` 一致。
- 除非明確要求，不刪除 local 或 remote branches。
