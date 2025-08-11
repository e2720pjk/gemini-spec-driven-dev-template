# Example Project

> 🌐 **Language**: [English](#english) | [繁體中文](#繁體中文)

---

## English

### Using the Example Project as a Template

This template provides a **fully functional and completed example project** located at:

```bash
example/blog-post-generator/
```

This project demonstrates a complete spec-driven development workflow — from requirements, design, and tasks to automated execution and testing.

#### Main Project Structure (Simplified)

```
example/blog-post-generator/
├── README.md                     # Project description
├── requirements.txt              # Python dependencies
├── pyproject.toml                # Python project settings
├── posts/                       # Output directory for generated blog posts
├── src/                         # Source code
├── tests/                       # Test cases
├── .gemini/                     # Gemini CLI commands and scripts
├── .kiro/                       # Spec files and configurations
│   └── specs/blog-post-generator/  # Generated spec documents (requirements.md, design.md, tasks.md, etc.)
```

#### How to Use This Example

1.  Navigate into the example directory:

    ```bash
    cd example/blog-post-generator/
    ```

2.  Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  (Optional) Run tests to verify the environment:

    ```bash
    pytest
    ```

4.  Explore the spec files under `.kiro/specs/blog-post-generator/` to understand the requirements, design, and tasks that drive development.

5.  Use the Gemini CLI `/spec:*` commands with this project to simulate or track the full spec-driven development workflow.

---

## 繁體中文

### 將範例專案作為模板使用

此模板提供了一個**功能齊全且已完成的範例專案**，位於：

```bash
example/blog-post-generator/
```

此專案展示了一個完整的規格驅動開發工作流程 — 從需求、設計、任務到自動化執行和測試。

#### 主要專案結構（簡化）

```
example/blog-post-generator/
├── README.md                     # 專案描述
├── requirements.txt              # Python 依賴
├── pyproject.toml                # Python 專案設定
├── posts/                       # 生成部落格文章的輸出目錄
├── src/                         # 原始碼
├── tests/                       # 測試案例
├── .gemini/                     # Gemini CLI 指令與腳本
├── .kiro/                       # 規格檔案與配置
│   └── specs/blog-post-generator/  # 生成的規格文件 (requirements.md, design.md, tasks.md 等)
```

#### 如何使用此範例

1.  導航到範例目錄：

    ```bash
    cd example/blog-post-generator/
    ```

2.  安裝 Python 依賴：

    ```bash
    pip install -r requirements.txt
    ```

3.  （可選）運行測試以驗證環境：

    ```bash
    pytest
    ```

4.  探索 `.kiro/specs/blog-post-generator/` 下的規格檔案，以了解驅動開發的需求、設計和任務。

5.  使用 Gemini CLI 的 `/spec:*` 指令與此專案一起使用，以模擬或追蹤完整的規格驅動開發工作流程。

---