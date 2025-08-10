
# Gemini Spec-Driven Dev Template

> 🌐 **Language**: [English](#english) | [繁體中文](#繁體中文)

---

## English

### Inspiration and Origin

This project is a re-implementation and adaptation of the concepts from the **`claude-code-spec`** project, designed to bring its powerful spec-driven development workflow into the Gemini CLI ecosystem. The original project demonstrated a robust, Kiro-style, three-phase approval workflow for Claude Code.

- **Original Project**: [claude-code-spec](https://github.com/gotalab/claude-code-spec) 

Our goal was to replicate that seamless, automated, and reliable development process using the native capabilities of the Gemini CLI, particularly its custom commands and tool execution features.

### Project Overview

`gemini-spec-driven-dev-template` is a starter kit and a powerful extension for the Gemini CLI. It provides a structured, command-driven workflow for software development, guiding you from a high-level feature idea to a detailed, and now executable, implementation plan (via the new `/spec:run-tasks` command) through a series of automated steps. This ensures consistency, quality, and clear documentation throughout the development lifecycle.

### The Role of `GEMINI.md` and Multilingual Interaction

This template includes a `GEMINI.md` file, which acts as the **central brain** for the AI agent. It contains a detailed set of instructions that define the agent's behavior, workflow, and logic.

A key feature of this logic is **multilingual support**. The recommended entry point for language configuration is now the `/spec:steering` command, which sets the project's default language stored in `.kiro/config.json`. All subsequent commands, including `/spec:init`, will automatically read and use this setting to maintain consistent multilingual interactions.

### Configurable Workflow

This template now supports both **implicit** and **interactive** approval workflows. You can switch between them by editing the `.kiro/config.json` file.

-   **`"approval_mode": "implicit"`** (Default): The original, streamlined workflow where running the next command (e.g., `/spec:design`) automatically approves the previous stage.
-   **`"approval_mode": "interactive"`**: A more deliberate workflow where the agent will ask for your explicit `[y/N]` confirmation before proceeding to the next stage, similar to the original `claude-code-spec`.

### How to Get Started

1.  **Copy Core Files**: Copy the `.gemini`, `.kiro`, and `GEMINI.md` files into your project's root directory.
2.  **(Optional) Configure Workflow**: Edit `.kiro/config.json` to set your preferred `approval_mode`.
3.  **Set Project Language and Initial Steering**: Run the recommended first step for any new project:
    ```bash
    /spec:steering
    ```
    This command initializes or updates the project's high-level goals and architecture, including setting the default language.
4.  **Initialize a Feature**: Start your first feature specification by running:
    ```bash
    /spec:init "A detailed description of the feature you want to build."
    ```

### Development Workflow & Command Sequence

Follow this sequence to develop a feature from scratch:

0.  **Steering (`/spec:steering`)**:
    -   **Command**: `/spec:steering`
    -   **Action**: Establishes or updates the project's high-level goals, architecture, and structure. For new projects, it prompts for a high-level description and generates initial `product.md`, `tech.md`, and `structure.md`. It also sets the project's default language in `.kiro/config.json`.

0.1. **Custom Steering (`/spec:steering-custom`)**:
    -   **Command**: `/spec:steering-custom`
    -   **Action**: Creates custom steering documents for specialized contexts (e.g., API standards, testing approaches).

1.  **Initialize (`/spec:init`)**:
    -   **Command**: `/spec:init "[Your detailed feature description]"`
    -   **Action**: Creates the necessary directory structure and metadata files for your new feature under `.kiro/specs/[feature-name]/`. It automatically reads the language setting from `.kiro/config.json`.

2.  **Generate Requirements (`/spec:requirements`)**:
    -   **Command**: `/spec:requirements [feature-name]`
    -   **Action**: Generates a `requirements.md` file based on your initial description. It then instructs you to review it.

3.  **Generate Design (`/spec:design`)**:
    -   **Command**: `/spec:design [feature-name]`
    -   **Action**: This command first **implicitly approves the requirements** and then generates the `design.md` file. It now leverages web search to research best practices before proposing technical solutions. After finalizing technical decisions, it updates `.kiro/steering/tech.md` as the project’s final technical standard.

4.  **Generate Tasks (`/spec:tasks`)**:
    -   **Command**: `/spec:tasks [feature-name]`
    -   **Action**: This command **implicitly approves the design** and then generates a detailed `tasks.md` file with a TDD-style checklist for implementation.

5.  **Execute Implementation (`/spec:run-tasks`)**:
    -   **Command**: `/spec:run-tasks [feature-name]`
    -   **Action**: Automatically executes the coding tasks defined in `tasks.md`, writing and modifying files to build the feature. It now also automatically generates and writes related documentation files as needed (e.g., updating `README.md`).

6.  **Check Status (`/spec:status`)**:
    -   **Command**: `/spec:status [feature-name]`
    -   **Action**: At any point, run this command to get a full report on the feature's progress. The report now includes a specific, runnable next command to guide you.

### Using the Sample Project

This template includes a fully functional and completed sample project located at:

```
example/blog-post-generator/
```

This project demonstrates a complete spec-driven development workflow. For detailed information and usage instructions, please refer to the `README.md` file in the example project directory.

### Phase-by-Phase Functionality and Differences from `claude-code-spec`

#### **Progress Tracking**

-   **`claude-code-spec`**: Uses event-driven **Hooks** that automatically trigger in the background after a file is modified to update progress. This is a **proactive, push-based** system.
-   **This Project (Gemini)**: Implements progress tracking via the `/spec:status` command. A Python script (`calculate_progress.py`) is executed **on-demand (pull-based)** when the command is run. It provides a highly reliable, deterministic calculation of progress without modifying the `spec.json` file, presenting the live status in the generated report.

#### **Specification Drift Detection**

-   **`claude-code-spec`**: Relies on Hooks that could trigger an LLM analysis in the background whenever source code files are changed, providing real-time feedback.
-   **This Project (Gemini)**: This feature is not currently available.

---

## 繁體中文

### 靈感與起源

本專案是 **`claude-code-spec`** 專案概念的重新實現與改造，旨在將其強大的規格驅動開發工作流程，帶入 Gemini CLI 的生態系統中。原始專案展示了一套為 Claude Code 設計的、基於 Kiro 風格的、穩健的三階段審批工作流程。

- **原始專案**: [claude-code-spec](https://github.com/gotalab/claude-code-spec)

我們的目標是使用 Gemini CLI 的原生功能，特別是其自訂指令和工具執行能力，來複製那種無縫、自動化且可靠的開發過程。

### 專案簡介

`gemini-spec-driven-dev-template` 是一個為 Gemini CLI 設計的啟動套件與強大的擴充功能。它提供了一套結構化的、由指令驅動的軟體開發工作流程，透過一系列自動化步驟，引導您從一個高層次的功能構想，產出一份詳細且**可執行**的實作計畫（透過新的 `/spec:run-tasks` 指令）。這確保了在整個開發生命週期中的一致性、高品質與清晰的文件紀錄。

### `GEMINI.md` 的角色與多語言互動

本範本包含一個 `GEMINI.md` 檔案，它扮演著 AI 代理人的 **核心大腦**。該檔案內含一組詳細的指令，定義了代理人的行為、工作流程與核心邏輯。

這套邏輯中的一個關鍵特性是**多語言支援**。推薦的語言設定進入點是 `/spec:steering` 指令，該指令會設定並儲存專案預設語言到 `.kiro/config.json`，所有後續指令（包含 `/spec:init`）會讀取該設定，確保全流程的語言一致性。

### 可配置的工作流程

本範本現在同時支援 **隱式 (implicit)** 和 **互動式 (interactive)** 兩種審批工作流程。您可以透過編輯 `.kiro/config.json` 檔案來切換模式。

-   **`"approval_mode": "implicit"`** (預設): 原有的流線型工作流程，執行下一階段的指令（例如 `/spec:design`）即會自動批准前一階段。
-   **`"approval_mode": "interactive"`**: 一個更嚴謹的工作流程，代理人在進入下一階段之前，會明確詢問您的 `[y/N]` 確認，類似於原始的 `claude-code-spec`。

### 如何開始

1.  **複製核心檔案**：將 `.gemini`、`.kiro` 和 `GEMINI.md` 檔案複製到您專案的根目錄。
2.  **（可選）配置工作流程**：編輯 `.kiro/config.json` 來設定您偏好的 `approval_mode`。
3.  **設定專案語言與初始指導**：執行推薦的新專案第一步：
    ```bash
    /spec:steering
    ```
    該指令用於初始化或更新專案的宏觀目標與架構，同時設定預設語言。
4.  **初始化一個功能**：執行：
    ```bash
    /spec:init "在這裡詳細描述您想建立的功能。"
    ```

### 開發工作流程與指令順序

請遵循以下順序來從頭開發一個新功能：

0.  **指導原則 (`/spec:steering`)**:
    -   **指令**: `/spec:steering`
    -   **作用**: 建立或更新專案的宏觀目標、架構和結構。新專案時，會要求高層描述並生成初步的 `product.md`、`tech.md` 和 `structure.md`。並且會將專案預設語言寫入 `.kiro/config.json`。

0.1. **自訂指導原則 (`/spec:steering-custom`)**:
    -   **指令**: `/spec:steering-custom`
    -   **作用**: 建立用於特定情境的自訂指導原則文件（例如：API 標準、測試方法）。

1.  **初始化 (`/spec:init`)**:
    -   **指令**: `/spec:init "[您功能的詳細描述]"`
    -   **作用**: 在 `.kiro/specs/[feature-name]/` 路徑下，為您的新功能建立必要的目錄結構和元數據檔案，並自動讀取 `.kiro/config.json` 中的語言設定。

2.  **產生需求 (`/spec:requirements`)**:
    -   **指令**: `/spec:requirements [feature-name]`
    -   **作用**: 根據初始描述產生 `requirements.md` 檔案，並指示您進行審閱。

3.  **產生設計 (`/spec:design`)**:
    -   **指令**: `/spec:design [feature-name]`
    -   **作用**: 此指令首先**隱含批准需求**，然後產生 `design.md` 檔案。它會利用網頁搜尋研究最佳實踐，並在使用者做出技術決策後，更新 `.kiro/steering/tech.md` 作為專案最終技術標準。

4.  **產生任務 (`/spec:tasks`)**:
    -   **指令**: `/spec:tasks [feature-name]`
    -   **作用**: 此指令**隱含批准設計**，然後產生帶有 TDD 清單的詳細 `tasks.md`。

5.  **執行實作 (`/spec:run-tasks`)**:
    -   **指令**: `/spec:run-tasks [feature-name]`
    -   **作用**: 自動執行 `tasks.md` 中的任務，透過寫入與修改檔案建構功能。現在也會自動生成並更新相關文件（例如 README.md）。

6.  **檢查狀態 (`/spec:status`)**:
    -   **指令**: `/spec:status [feature-name]`
    -   **作用**: 隨時執行此指令以獲得功能進度報告，報告中會包含明確的下一步執行指令。

### 使用範例專案

本範本包含一個功能齊全且已完成的示範專案，位於：

```
example/blog-post-generator/
```

該專案展示了完整的規格驅動開發流程。詳細內容與使用說明，請參閱該目錄下的 `README.md`。

### 各階段功能及與 `claude-code-spec` 的差異

#### **進度追蹤**

-   **`claude-code-spec`**: 使用事件驅動的 **Hooks**，在檔案被修改後自動在背景觸發進度更新。這是一個**主動、推播式**系統。
-   **本專案 (Gemini)**: 透過 `/spec:status` 指令實現進度追蹤。執行時會按需呼叫 Python 腳本 (`calculate_progress.py`) 計算進度，不修改 `spec.json`，直接呈現即時狀態。

#### **規格漂移檢測**

-   **`claude-code-spec`**: 依賴 Hooks，在原始碼變更時背景觸發 LLM 分析，提供即時回饋。
-   **本專案 (Gemini)**: 目前尚未支援此功能。

---
