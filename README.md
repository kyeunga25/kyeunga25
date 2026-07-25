# Ken Yeung

把實際問題做成可用、可驗證，而且重視私隱的軟件。

I build practical, verifiable software with clear interfaces, privacy-conscious architecture, and reliable delivery.

[個人網站 / Portfolio](https://k-y.cc) · [公開開發設定 / Public setup](#公開開發設定--public-development-setup)

## 現正開發 / Current work

以下項目以公開、可核實的版本為準；未合併的實驗不會列作已完成成果。

| 項目 / Project | 內容 / What it does | 狀態 / Status |
| --- | --- | --- |
| **[Wallpect](https://github.com/kyeunga25/wallpect)** | 在瀏覽器內預覽、調整並輸出 Apple 裝置桌布；圖片不會上傳。<br>Browser-only wallpaper preview, fitting, and exact-size export for Apple devices. | **v0.2.2 · Released**<br>[線上使用 / Live](https://wallpect.k-y.cc) |
| **[Anisonary｜動畫歌典](https://github.com/kyeunga25/anisonary)** | 按季度與播出日整理動畫 OP／ED；2026 春夏目錄現有 139 部作品及 298 筆主題曲資料。<br>A source-traceable seasonal anime theme directory with local, privacy-bounded search. | **v0.4.0 · Public**<br>[瀏覽目錄 / Live](https://anisonary.k-y.cc) |
| **[Personal Space](https://github.com/kyeunga25/personal-space)** | 以 Shorts、Longform 和有來源的 Briefings 組織內容的雙語發佈介面。<br>A bilingual publishing foundation for short posts, longform writing, and source-backed briefings. | **Active development**<br>[查看網站 / Live](https://space.k-y.cc) |
| **[Motive](https://github.com/kyeunga25/marketing_image_ai_web)** | 把產品資料、品牌規範與參考圖整理成一致的電商 campaign visuals。<br>A controlled ecommerce workflow for coordinated campaign visuals. | **Closed beta**<br>[預覽 / Preview](https://motive-ecommerce-visuals.kyeunga25.workers.dev) |
| **[RigStage](https://github.com/kyeunga25/pc-ai-3d-builder)** | 面向電腦商戶的邀請制配置及 3D 視覺工作台；目前只使用合成示範資料。<br>An invite-only merchant PC configuration and 3D visualisation workspace using synthetic demo data. | **Invite-only MVP**<br>[查看程式碼 / Repository](https://github.com/kyeunga25/pc-ai-3d-builder) |
| **[StudyMix AI](https://github.com/kyeunga25/studymix-ai)** | 把已獲授權的音訊轉成適合學習的純音樂版本，並以私人儲存及限時保留作設計邊界。<br>An early cloud-native MVP for authorized audio restyling, designed around private storage and limited retention. | **Early MVP**<br>[查看程式碼 / Repository](https://github.com/kyeunga25/studymix-ai) |

## 工程方向 / Engineering focus

TypeScript、React、Astro、Node.js、Python 與 Cloudflare Workers；重點包括瀏覽器端私隱、受限制的雲端工作流程、可追溯資料、測試自動化及可回復的發佈流程。

TypeScript, React, Astro, Node.js, Python, and Cloudflare Workers, with an emphasis on browser-side privacy, bounded cloud workflows, traceable data, automated testing, and recoverable releases.

## 公開開發設定 / Public development setup

- **[Codex development setup](./codex/)** — 可重用的 `AGENTS.md` 與最小權限 `config.toml` 範例；不包含憑證、本機路徑、工作紀錄或介面偏好。
- **[macOS dotfiles](./dotfiles/)** — 可攜、可審閱的 shell／terminal 設定子集，以及對應的 [Brewfile](./Brewfile)。

The published setup is intentionally a reviewable reference rather than an export of live machine state.
