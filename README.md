# Gemini Spec-Driven Dev Template

> 🌐 **Language**: [English](#english) | [繁體中文](#繁體中文)

---

## English

### Inspiration and Origin

This project is a re-implementation and adaptation of the concepts from the **`claude-code-spec`** project, designed to bring its powerful spec-driven development workflow into the Gemini CLI ecosystem. The original project demonstrated a robust, Kiro-style, three-phase approval workflow for Claude Code.

- **Original Project**: [claude-code-spec](https://github.com/gotalab/claude-code-spec) 

Our goal was to replicate that seamless, automated, and reliable development process using the native capabilities of the Gemini CLI, particularly its custom commands and tool execution features.

### Project Overview

`gemini-spec-driven-dev-template` is a starter kit and a powerful extension for the Gemini CLI. It provides a structured, command-driven workflow for software development, guiding you from a high-level feature idea to a detailed implementation plan through a series of automated steps. This ensures consistency, quality, and clear documentation throughout the development lifecycle.

### How to Get Started

1.  **Copy the Extension**: Copy the `.gemini` directory  into your own project's directory.
2.  **Copy Steering Files**: Copy the `.kiro/steering` directory into your project's `.kiro/` directory to establish the foundational development principles.
3.  **Initialize a Feature**: Start your first feature specification by running:
    ```bash
    /spec:init "A detailed description of the feature you want to build."
    ```

### Development Workflow & Command Sequence

Follow this sequence to develop a feature from scratch:

1.  **Initialize (`/spec:init`**):
    -   **Command**: `/spec:init "[Your detailed feature description]"`
    -   **Action**: Creates the necessary directory structure and metadata files for your new feature under `.kiro/specs/[feature-name]/`.

2.  **Generate Requirements (`/spec:requirements`**):
    -   **Command**: `/spec:requirements [feature-name]`
    -   **Action**: Generates a `requirements.md` file based on your initial description. It then instructs you to review it.

3.  **Generate Design (`/spec:design`**):
    -   **Command**: `/spec:design [feature-name]`
    -   **Action**: This command first **implicitly approves the requirements** (updating `spec.json`) and then generates the `design.md` file based on the requirements. It then instructs you to review the design.

4.  **Generate Tasks (`/spec:tasks`**):
    -   **Command**: `/spec:tasks [feature-name]`
    -   **Action**: This command **implicitly approves the design** and then generates a detailed `tasks.md` file with a checklist for implementation.

5.  **Check Status (`/spec:status`**):
    -   **Command**: `/spec:status [feature-name]`
    -   **Action**: At any point, run this command to get a full report on the feature's progress, including an automated calculation of task completion from `tasks.md`.

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

`gemini-spec-driven-dev-template` 是一個為 Gemini CLI 設計的啟動套件與強大的擴充功能。它提供了一套結構化的、由指令驅動的軟體開發工作流程，透過一系列自動化步驟，引導您從一個高層次的功能構想，產出一份詳細的實作計畫。這確保了在整個開發生命週期中的一致性、高品質與清晰的文件紀錄。

### 如何開始

1.  **複製擴充功能**：將 `.gemini/` 資料夾，複製到您自己專案的目錄中。
2.  **複製指導原則檔案**：將 `.kiro/steering` 目錄複製到您專案的 `.kiro/` 目錄下，以建立基礎的開發原則。
3.  **初始化一個功能**：執行以下指令來開始您的第一個功能規格：
    ```bash
    /spec:init "在這裡詳細描述您想建立的功能。"
    ```

### 開發工作流程與指令順序

請遵循以下順序來從頭開發一個新功能：

1.  **初始化 (`/spec:init`**):
    -   **指令**: `/spec:init "[您功能的詳細描述]"`
    -   **作用**: 在 `.kiro/specs/[feature-name]/` 路徑下，為您的新功能建立必要的目錄結構和元數據檔案。

2.  **產生需求 (`/spec:requirements`**):
    -   **指令**: `/spec:requirements [feature-name]`
    -   **作用**: 根據您的初始描述產生一份 `requirements.md` 檔案，並指示您進行審閱。

3.  **產生設計 (`/spec:design`**):
    -   **指令**: `/spec:design [feature-name]`
    -   **作用**: 此指令首先會**隱含地批准需求**（更新 `spec.json`），然後根據需求文件產生 `design.md` 檔案，並指示您審閱設計稿。

4.  **產生任務 (`/spec:tasks`**):
    -   **指令**: `/spec:tasks [feature-name]`
    -   **作用**: 此指令會**隱含地批准設計**，然後產生一份帶有實作清單的詳細 `tasks.md` 檔案。

5.  **檢查狀態 (`/spec:status`**):
    -   **指令**: `/spec:status [feature-name]`
    -   **作用**: 在任何時間點執行此指令，以獲取關於功能進度的完整報告，其中包含根據 `tasks.md` 自動計算的任務完成度。

### 各階段功能及與 `claude-code-spec` 的差異

#### **進度追蹤 (Progress Tracking)**

-   **`claude-code-spec`**: 使用事件驅動的 **Hooks**，在檔案被修改後自動在背景觸發進度更新。這是一個**主動的、推播式 (Push-based)** 的系統。
-   **本專案 (Gemini)**: 透過 `/spec:status` 指令來實現進度追蹤。當指令被執行時，一個 Python 腳本 (`calculate_progress.py`) 會被**按需 (Pull-based)** 執行。它提供了一個高度可靠、確定性的進度計算，而不會去修改 `spec.json` 檔案，僅將即時狀態呈現在報告中。

#### **規格漂移檢測 (Specification Drift Detection)**

-   **`claude-code-spec`**: 依賴 Hooks，當原始碼檔案變更時，可能會在背景觸發 LLM 進行分析，提供即時回饋。
-   **本專案 (Gemini)**: 目前沒有提供此功能。
