# Changelog

All notable changes to this project will be documented in this file.


## 2025-08-10

*   **refactor: relocate example project and improve spec-driven workflow**
    *   **Major Adjustment Summary**: Refactored example project location and improved the spec-driven workflow:
        *   **Example Project Relocation and Integration**: Moved the `blog-post-generator` example project and all its specification documents to `example/blog-post-generator/` (from `samples/blog-post-generator/` and `docs/kiro/specs-example/` respectively), making it a self-contained and easily referenceable unit.
        *   **Core Workflow Enhancements**:
            *   **Smart Steering (`/spec:steering`)**: Now serves as a universal entry point for both new and existing projects, centralizing language settings and generating initial steering documents for new projects.
            *   **Tech Stack Decision Optimization (`/spec:design`)**: Explicitly prompts for web searches for best practices during the design phase and automatically updates `.kiro/steering/tech.md` once technical decisions are finalized.
            *   **Automated Documentation Generation (`/spec:run-tasks`)**: Automatically generates and updates documentation content (e.g., `README.md`) when relevant tasks are detected.
            *   **Improved Language Consistency**: `init.toml` and `tasks.toml` now consistently read language configuration from `config.json` or `spec.json`.
        *   **Template Cleanup**: Removed default steering documents from the main `.kiro/steering/` and updated `README.md` to reflect the new workflow and example project location.

*   **feat: Enhance spec-driven template with executable plans and samples**
    *   **Major Adjustment Summary**: Significantly enhanced the spec-driven development template to include executable plans and samples:
        *   **`/spec:design` Command Enhancement**: Mandates web searches before proposing technical solutions, ensuring design proposals are based on the latest best practices.
        *   **`/spec:init` Command Improvement**: Automatically generates filesystem-friendly feature names from user descriptions, improving naming consistency.
        *   **Introduction of Complete Example Project**: Added `samples/blog-post-generator`, a fully functional Python project including source code, tests, and complete specification documents (located in `docs/kiro/specs-example/`), serving as a practical example of the spec-driven workflow.
        *   **`README.md` Updates**: Emphasized the "executable" nature of implementation plans and added a dedicated section guiding users on how to explore and trace the example project's spec-driven workflow.

## 2025-08-09

*   **feat(spec-template): Enhance spec commands for automation and consistency**
    *   **Major Adjustment Summary**: Significantly enhanced the spec-driven development template for automation and consistency:
        *   **New `/spec:run-tasks` Command**: Introduced a new command enabling the AI to directly execute implementation tasks defined in `tasks.md`, achieving end-to-end automation and automatically updating task status and `spec.json` phase.
        *   **`/spec:design` Integration with `google_web_search`**: Allows the AI to use `google_web_search` during design generation to query for latest best practices and patterns, improving the quality and practicality of design proposals.
        *   **Improved `/spec:status` Command**: `status.toml` now provides a clear, runnable "Next Command" recommendation based on the current phase and approval status, enhancing user guidance.
        *   **Unified Settings Adherence**: Ensures all spec-related commands (including the new `run-tasks`) consistently adhere to language settings in `spec.json` and approval modes in `.kiro/config.json`.

*   **refactor(i18n): Remove Chinese comments from GEMINI.md**
    *   **Major Adjustment Summary**: Removed all parenthesized Chinese comments from `GEMINI.md` to ensure the core instruction file remains purely English, reinforcing its role as the primary and stable source of logic for the AI agent. `GEMINI_zh-TW.md` continues to serve as a complete reference for Chinese developers.

*   **docs: Clarify multilingual interaction in README.md**
    *   **Major Adjustment Summary**: Clarified the explanation of `GEMINI.md`'s role and multilingual interaction in `README.md`. Explicitly stated that `GEMINI.md` is the core logic source for the AI agent, and that the language setting in `spec.json` controls all subsequent interactions (including questions, confirmations, and document generation) for that feature. Also emphasized that while `GEMINI.md` is in English, its internal logic supports multilingualism, and `GEMINI_zh-TW.MD` is provided as a Chinese reference.

*   **feat(workflow): Introduce multilingual support, interactive approval, and GEMINI.md**
    *   **Major Adjustment Summary**: Introduced several major features significantly enhancing the spec-driven development workflow:
        *   **Multilingual Support**: `spec-init.toml` allows specifying a language, which will be used for all subsequent spec documents and interactions.
        *   **Configurable Approval Workflow**: Added `.kiro/config.json`, allowing switching between "implicit" and "interactive" approval modes, increasing workflow flexibility.
        *   **`GEMINI.md` as Core Guidance**: Introduced `GEMINI.md` (and `GEMINI_zh-TW.md`) as the AI agent's behavioral guidelines, ensuring consistency and predictability.
        *   **Prompt Optimization and Logic Enhancement**: Significantly improved prompts for all `spec` commands, supporting new features (e.g., technical discussion during design, EARS format requirements, TDD task generation), and handling edge cases like file existence checks.
        *   **README Update**: Updated `README.md` to explain these new features.

## 2025-08-01

*   **refactor: Rename spec TOML files to remove duplicate 'spec' prefix**
    *   **Major Adjustment Summary**: Refactored command file naming by renaming all TOML files under `.gemini/commands/spec/` that had a redundant "spec-" prefix (e.g., `spec-design.toml` to `design.toml`), improving naming consistency and conciseness.

*   **relese v1.0**
    *   **Major Adjustment Summary**: Marked the release of v1.0, formalizing the Gemini spec-driven development workflow. Key changes include:
        *   **Command Logic Enhancement**: `spec-design.toml` and `spec-tasks.toml` updated to explicitly define the process of automatically approving the previous phase (requirements or design) before generating the next, and updating `spec.json` status.
        *   **Introduction of Automated Progress Tracking**: Added `.gemini/scripts/calculate_progress.py` script for automatically calculating task completion progress in `tasks.md`, and updated `spec-status.toml` to utilize this script.
        *   **Major README Rewrite**: `README.md` was comprehensively updated, detailing the new development workflow, command sequence, and explaining differences from the `claude-code-spec` project regarding progress tracking. `README.zh-TW.md` was also deleted.

*   **Change gemini commands namespaces**
    *   **Major Adjustment Summary**: Reorganized Gemini commands by moving all `spec-` and `steering-` related `.toml` command files into the `.gemini/commands/spec/` subdirectory, creating clearer command namespaces. Simultaneously, significantly updated `product.md`, `structure.md`, and `tech.md` under `.kiro/steering/`, making their content more concrete, explicitly defining project product goals, detailed directory structure, and core technology stack, enhancing project guidance and readability.

## 2025-07-27

*   **Change commands file .md to .toml**
    *   **Major Adjustment Summary**: Major refactoring of Gemini command definition methods, converting all `.md` command files under `.gemini/commands/` to `.toml` format. This included encapsulating command descriptions and prompt content within the TOML structure and deleting the old `settings.json` configuration file. Concurrently, the default language in `spec-init.toml` was changed from "Japanese" to "Traditional Chinese", and `README.md` and `README.zh-TW.md` were updated to reflect these configuration and workflow changes.

*   **init template**
    *   **Major Adjustment Summary**: Initialized the project template, establishing the core directory structure and files required for Gemini spec-driven development. This includes `.gemini/commands` (for defining various spec-related operations), `.kiro/steering` (product, tech, architecture guidance documents), `.kiro/specs` (spec file storage), and initial `README.md` and `docs` files (including English and Traditional Chinese versions). This commit laid the foundation for the project's structure and workflow.

### Refactor

- Restructure example project and enhance workflow.
  - The `blog-post-generator` example project has been moved from `samples/blog-post-generator/` to `example/blog-post-generator/`.
  - Its associated specification documents have been moved from `docs/kiro/specs-example/` to `example/blog-post-generator/.kiro/specs/`.
  - This provides a single, consolidated location for the complete example project, making it easier for users to reference.

### Feat

- Enhance spec-driven development workflow.
  - **Smart Steering (`/spec:steering`):**
    - Now serves as the universal starting point for both new and existing projects.
    - Automatically detects project status (new/existing) and adapts its behavior.
    - Centralizes project language configuration in `.kiro/config.json`.
    - For new projects, generates preliminary steering documents based on a high-level description.
  - **Refined Tech Stack Decision:**
    - `/spec:design` now explicitly informs the user about web searches for technical approaches.
    - `/spec:design` formalizes the tech stack decision by updating `.kiro/steering/tech.md` with the user's final choice.
  - **Automated Documentation Generation:**
    - `/spec:run-tasks` now automatically generates content for documentation files (e.g., `README.md`) when encountering relevant tasks.
  - **Improved Language Consistency:**
    - `init.toml` now reads language from `.kiro/config.json`.
    - `tasks.toml` includes language determination for consistent interaction.

### Chore

- Template Cleanup:
  - The default `product.md`, `structure.md`, and `tech.md` in `.kiro/steering/` have been removed, as they are now generated by `/spec:steering`.
  - `README.md` has been updated to reflect the new workflow and example project location.

## Initial Setup and Core Features

### Feat

- Enhance spec-driven template with executable plans and samples.
  - Integrates `google_web_search` into the `/spec:design` command for better technical proposals.
  - Improves `/spec:init` for more robust feature name generation and path handling.
  - Updates `README.md` to:
    - Emphasize the "executable" nature of implementation plans (via /spec:run-tasks).
    - Add a dedicated section for the samples/blog-post-generator project, guiding users on how to explore and trace the spec-driven workflow with a completed example.
    - Reorder sections for better readability and user experience.
  - Includes the samples/blog-post-generator project and updated docs/ as part of the template.

- Enhance spec commands for automation and consistency.
  - Adds a new `/spec:run-tasks` command to enable end-to-end automation, allowing the AI to execute implementation plans directly from `tasks.md`.
  - Integrates `google_web_search` into the `/spec:design` command to ground technical proposals in current best practices.
  - Improves the `/spec:status` command to provide a clear, runnable next command, enhancing user guidance.
  - Ensures all spec-related commands (`run-tasks`, `design`, etc.) consistently respect shared settings from `spec.json` (language) and `.kiro/config.json` (approval_mode).

- Introduce multilingual support, interactive approval, and `GEMINI.md`.
  - **Multilingual Support**:`/spec:init` command now allows users to specify language for spec documents; all subsequent interactions and document generation will use this setting.
  - **Interactive Approval**: Added configurable approval workflow (`.kiro/config.json`), allowing users to choose between "implicit" and "interactive" modes.
  - **`GEMINI.md` Core Guidance**: Introduced `GEMINI.md` as the core guidance file defining AI agent behavior, ensuring consistency and predictability.
  - **Prompt Optimization**: Significantly improved prompts for all `/spec:*` commands to support new features, enhance output quality (e.g., EARS format, TDD task generation), and handle edge cases.
  - **Documentation Update**: Updated `README.md` to explain new features.

### Refactor

- Remove Chinese comments from `GEMINI.md`.
  - Ensures the AI agent's core instruction file is purely English, reinforcing its role as the primary, stable logic source. `GEMINI_zh-TW.md` continues to serve as a complete reference for Chinese developers.

- Rename spec TOML files to remove duplicate 'spec' prefix.

- Change gemini commands namespaces.

- Change commands file .md to .toml.

### Docs

- Clarify multilingual interaction in `README.md`.
  - Updates `README.md` to accurately describe the relationship between `GEMINI.md` and spec language settings.
  - Explains `GEMINI.md` as the AI agent's core logic, written in English for stability.
  - Clarifies that the `language` setting in `spec.json` controls both "output documents" and "AI interaction" language.
  - This update reflects tested and verified system behavior.

## Project Initialization

### Chore

- Initial template setup.
