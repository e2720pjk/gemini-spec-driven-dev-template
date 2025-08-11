# 更新日誌

本專案的所有重要變更都將記錄在此檔案中。


## 2025-08-10

*   **refactor: relocate example project and improve spec-driven workflow**
    *   **重大調整摘要**：重構範例專案位置並改進規格驅動工作流程：
        *   **範例專案重新定位與整合**：將 `blog-post-generator` 範例專案及其所有規格文件統一移動到 `example/blog-post-generator/` 目錄下，使其成為一個獨立且易於參考的單元。
        *   **核心工作流程增強**：
            *   **智慧指導 (`/spec:steering`)**：作為新舊專案的通用入口點，集中管理語言設定，並為新專案生成初始指導文件。
            *   **技術棧決策優化 (`/spec:design`)**：在設計階段明確提示網頁搜尋最佳實踐，並在技術決策確定後自動更新 `.kiro/steering/tech.md`。
            *   **自動化文件生成 (`/spec:run-tasks`)**：當檢測到相關任務時，自動生成並更新文件內容（例如 `README.md`）。
            *   **語言一致性提升**：`init.toml` 和 `tasks.toml` 更一致地從 `config.json` 或 `spec.json` 讀取語言配置。
        *   **模板清理**：刪除主 `.kiro/steering/` 下的預設指導文件，並更新 `README.md` 以反映新的工作流程和範例專案位置。

*   **feat: Enhance spec-driven template with executable plans and samples**
    *   **重大調整摘要**：顯著增強規格驅動開發模板，使其包含可執行的計畫和範例：
        *   **`/spec:design` 命令強化**：強制要求在提出技術方案前進行網頁搜尋，確保設計提案基於最新的最佳實踐。
        *   **`/spec:init` 命令改進**：自動從用戶描述中生成符合文件系統規範的功能名稱，提高命名一致性。
        *   **引入完整範例專案**：新增 `samples/blog-post-generator`，這是一個功能齊全的 Python 專案，包含原始碼、測試和完整的規格文件（位於 `docs/kiro/specs-example/`），作為展示規格驅動工作流程的實例。
        *   **`README.md` 更新**：強調實作計畫的「可執行性」，並新增專門章節指導用戶如何探索和追溯範例專案的規格驅動工作流程。

## 2025-08-09

*   **feat(spec-template): Enhance spec commands for automation and consistency**
    *   **重大調整摘要**：顯著增強規格驅動開發模板的自動化和一致性：
        *   **新增 `/spec:run-tasks` 命令**：引入一個全新的命令，使 AI 能夠直接執行 `tasks.md` 中定義的實作任務，實現端到端自動化，並自動更新任務狀態和 `spec.json` 中的階段。
        *   **`/spec:design` 整合 `google_web_search`**：在設計生成過程中，允許 AI 使用 `google_web_search` 查詢最新的技術實踐和模式，提升設計提案的品質和實用性。
        *   **改進 `/spec:status` 命令**：`status.toml` 現在會根據當前階段和審批狀態，提供一個明確且可執行的「下一步命令」建議，增強使用者引導。
        *   **統一設定遵循**：確保所有規格相關命令（包括新的 `run-tasks`）都一致地遵循 `spec.json` 中的語言設定和 `.kiro/config.json` 中的審批模式。

*   **refactor(i18n): 移除 GEMINI.md 中的中文註釋**
    *   **重大調整摘要**：移除 `GEMINI.md` 檔案中所有標題旁的括號內中文註釋，確保該核心指令文件為純英文版本，以強化其作為 AI 代理人主要且穩定邏輯來源的角色。`GEMINI_zh-TW.md` 則繼續作為中文開發者的完整參考文件。

*   **docs: 釐清 README 中關於多語言互動的說明**
    *   **重大調整摘要**：釐清 `README.md` 中關於 `GEMINI.md` 角色與多語言互動的說明。明確指出 `GEMINI.md` 是 AI 代理人的核心邏輯來源，並闡明 `spec.json` 中的語言設定將控制該功能後續所有互動（包含提問、確認、文件生成）的語言。同時強調 `GEMINI.md` 雖為英文，但其內部邏輯支援多語言，並提供 `GEMINI_zh-TW.md` 作為中文參考。

*   **feat(workflow): 導入多語言支援、互動式審批與 GEMINI.md**
    *   **重大調整摘要**：導入多項重大功能，顯著增強了規格驅動開發工作流程：
        *   **多語言支援**：`spec-init.toml` 允許指定語言，後續所有規格文件和互動將依此語言進行。
        *   **可配置審批流程**：新增 `.kiro/config.json`，允許在「隱式」和「互動式」審批模式間切換，提升工作流程彈性。
        *   **`GEMINI.md` 作為核心指導**：引入 `GEMINI.md` (及 `GEMINI_zh-TW.md`) 作為 AI 代理人的行為準則，確保其行為一致性與可預測性。
        *   **提示優化與邏輯增強**：所有 `spec` 命令的提示內容大幅改進，支援新功能（如設計階段的技術討論、EARS 格式需求、TDD 任務生成），並處理檔案存在性檢查等邊界情況。
        *   **README 更新**：`README.md` 更新以說明這些新功能。

## 2025-08-01

*   **refactor: Rename spec TOML files to remove duplicate 'spec' prefix**
    *   **重大調整摘要**：重構命令檔案命名，將 `.gemini/commands/spec/` 目錄下所有帶有重複「spec-」前綴的 TOML 檔案重新命名，例如 `spec-design.toml` 改為 `design.toml`，以提高命名的一致性和簡潔性。

*   **relese v1.0**
    *   **重大調整摘要**：標誌著 v1.0 版本的發布，此版本正式化了 Gemini 規格驅動開發的工作流程。主要變動包括：
        *   **命令邏輯強化**：`spec-design.toml` 和 `spec-tasks.toml` 更新，明確定義了在生成設計和任務前，自動批准前一階段（需求或設計）的流程，並更新 `spec.json` 中的狀態。
        *   **引入自動化進度追蹤**：新增 `.gemini/scripts/calculate_progress.py` 腳本，用於自動計算 `tasks.md` 中的任務完成進度，並更新 `spec-status.toml` 以利用此腳本。
        *   **README 大幅重寫**：`README.md` 進行了全面更新，詳細說明了新的開發工作流程、命令序列，並闡述了與 `claude-code-spec` 專案在進度追蹤等方面的差異。同時，`README.zh-TW.md` 被刪除。

*   **Change gemini commands namespaces**
    *   **重大調整摘要**：重新組織 Gemini 命令，將所有 `spec-` 和 `steering-` 相關的 `.toml` 命令文件移動到 `.gemini/commands/spec/` 子目錄下，建立了更清晰的命令命名空間。同時，大幅更新了 `.kiro/steering/` 下的 `product.md`、`structure.md` 和 `tech.md` 文件，使其內容更具體，明確定義了專案的產品目標、詳細的目錄結構和所使用的核心技術棧，提升了專案的指導性和可讀性。

## 2025-07-27

*   **Change commands file .md to .toml**
    *   **重大調整摘要**：重大重構 Gemini 命令定義方式，將 `.gemini/commands/` 下的所有 `.md` 命令文件轉換為 `.toml` 格式。這包含了將命令描述和提示內容封裝在 TOML 結構中，並刪除了舊的 `settings.json` 配置檔案。同時，`spec-init.toml` 中的預設語言從「日語」更改為「繁體中文」，並更新了 `README.md` 和 `README.zh-TW.md` 以反映這些配置和工作流程的變更。

*   **init template**
    *   **重大調整摘要**：初始化專案模板，建立了 Gemini 規格驅動開發所需的核心目錄結構與文件。這包括 `.gemini/commands` (用於定義各種規格相關操作指令)、`.kiro/steering` (產品、技術、架構指導文件)、`.kiro/specs` (規格文件存放處)，以及初始的 `README.md` 和 `docs` 文件 (包含英文與繁體中文版本)。此 commit 為專案奠定了基礎結構與工作流程。
