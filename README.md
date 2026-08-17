# Ken Yeung

把實際問題做成可用、可驗證，而且重視私隱的軟件。

I build practical, verifiable software with clear interfaces, privacy-conscious architecture, and reliable delivery.

[個人網站 / Portfolio](https://k-y.cc) · [公開開發設定 / Public setup](#公開開發設定--public-development-setup)

## 已發布產品 / Released products

以下狀態於 2026-08-17 按公開 release、repository、文件與正式網站核對；preview 或未合併的實驗不會列作已發布成果。

Status was checked on 17 August 2026 against public releases, repositories, documentation, and production sites.

### [Wallpect](https://github.com/kyeunga25/wallpect) — [v0.4.0](https://github.com/kyeunga25/wallpect/releases/tag/v0.4.0) · Released

在瀏覽器內為 Apple 裝置預覽、調整並輸出桌布，提供構圖與系統遮擋提示；圖片解碼、編輯及輸出不會上載到伺服器。

Browser-only wallpaper composition, device guides, and exact-size export for Apple devices, without uploading the selected image.

[線上使用 / Live](https://wallpect.k-y.cc) · [文件 / Docs](https://github.com/kyeunga25/wallpect/tree/main/docs)

### [Anisonary｜動畫歌典](https://github.com/kyeunga25/anisonary) — [v1.3.0](https://github.com/kyeunga25/anisonary/releases/tag/v1.3.0) · Public

按季度與日本播出日整理動畫 OP／ED；四個經審閱的季度快照現有 280 部作品及 615 筆主題曲資料，並保留逐曲來源記錄。

A source-traceable seasonal anime theme directory with 280 reviewed titles, 615 known OP／ED records, per-song evidence, and local-only search.

[瀏覽目錄 / Live](https://anisonary.k-y.cc) · [文件 / Docs](https://github.com/kyeunga25/anisonary/tree/main/docs)

### [Personal Space](https://github.com/kyeunga25/personal-space) — [v0.7.0](https://github.com/kyeunga25/personal-space/releases/tag/v0.7.0) · Public

以 Astro 與 Cloudflare Workers 建立 Notes、Articles、Editions、搜尋及封存；私人 Studio 與寫入操作維持受保護。

A bilingual Astro publishing space on Cloudflare Workers, with public reading surfaces and an access-protected private studio.

[查看網站 / Live](https://space.k-y.cc) · [文件 / Docs](https://github.com/kyeunga25/personal-space/tree/main/docs)

## 私人測試與早期開發 / Private beta and early work

這些產品只開放受邀工作區或仍有明確停用功能；公開 repository 與產品介紹不代表公開註冊。

### [AisleStage](https://github.com/kyeunga25/aislestage) — [v0.5.1](https://github.com/kyeunga25/aislestage/releases/tag/v0.5.1) · Closed beta · Invite-only

把獲授權商品圖、已核實的繁中／英文商業資料與人工批准，整理成 1:1、4:5、9:16 Campaign Pack。

A controlled ecommerce workflow for three-format campaign packs built from approved product imagery, verified copy, and explicit human approval.

[文件 / Docs](https://github.com/kyeunga25/aislestage/tree/main/docs)

### RigStage — Invite-only

面向電腦商戶的受保護產品目錄、私人素材審核與 PC Builder；公開畫面只使用合成示範資料。

An invite-only PC catalogue, private asset-review, and assembly workspace whose public showcase uses synthetic demo data.

[產品介紹 / Overview](https://rigstage.k-y.cc)

### [StudyMix AI](https://github.com/kyeunga25/studymix-ai) — Closed beta · Early MVP

為已擁有或獲授權的錄音設計私人音訊風格重塑流程；目前沒有公開註冊，正式上載及外部生成保持停用。

A private audio-restyling MVP for authorized recordings; public registration, production uploads, and external generation remain disabled.

[文件 / Docs](https://github.com/kyeunga25/studymix-ai/tree/main/docs)

## 工程方向 / Engineering focus

TypeScript、React、Astro、Node.js、Python 與 Cloudflare Workers／Static Assets；重點包括瀏覽器端私隱、受限制的雲端工作流程、可追溯資料、測試自動化及可回復的發佈流程。

TypeScript, React, Astro, Node.js, Python, Cloudflare Workers, and Static Assets, with an emphasis on browser-side privacy, bounded cloud workflows, traceable data, automated testing, and recoverable releases.

## 公開開發設定 / Public development setup

- **[Repository guidance](./AGENTS.md)** — 這個 Profile repository 實際採用的公開安全範圍與完成條件。
- **[Portfolio website](https://github.com/kyeunga25/kyeunga25.github.io)** — `k-y.cc` 的獨立靜態網站 source、project status 與 GitHub Pages 發布文件。
- **[Codex development setup](./codex/)** — 可參考、可審閱的 `AGENTS.md` 與最小權限 `config.toml` 範例。
- **[macOS dotfiles](./dotfiles/)** — 可攜、可審閱的 shell／terminal 設定子集，以及對應的 [Brewfile](./Brewfile)。
- **[Public profile validation](./scripts/validate_public_profile.py)** — 檢查相對連結、公開設定、過時連結及常見敏感資料類別。

The published setup is intentionally a reviewable reference rather than an export of live machine state. It excludes credentials, machine paths, private service mappings, sessions, prompts, and interface preferences.
