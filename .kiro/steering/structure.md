# Project Structure

The project is organized as follows:

-   `.gitignore`: Specifies intentionally untracked files to ignore by Git.
-   `README.md`, `README.zh-TW.md`: Provides a general overview and introduction to the project in English and Traditional Chinese.
-   `.gemini/`: Contains configurations and command definitions specific to the Gemini CLI.
    -   `settings.json`: Global settings for the Gemini CLI.
    -   `commands/`: A collection of Markdown (`.md`) files for command descriptions and TOML (`.toml`) files for command configurations. This includes definitions for `spec-design`, `spec-init`, `spec-requirements`, `spec-status`, `spec-tasks`, `steering`, and `steering-custom` commands.
-   `.git/`: The hidden directory used by Git for version control.
-   `.kiro/`: A directory likely intended for project-specific specifications and steering documents.
    -   `specs/`: Currently contains `.gitkeep`, suggesting it's a placeholder for future user-defined specifications.
    -   `steering/`: Contains the `product.md`, `structure.md`, and `tech.md` files, which define the project's product goals, technical stack, and structural organization.
-   `docs/`: Comprehensive project documentation.
    -   `architecture.md`, `architecture.zh-TW.md`: Documents the project's architectural design.
    -   `index.md`, `index.zh-TW.md`: Main index files for the documentation.
    -   `usage.md`, `usage.zh-TW.md`: Provides instructions on how to use the project.