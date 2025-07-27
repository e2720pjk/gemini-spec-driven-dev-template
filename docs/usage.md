# Usage

This document explains how to use the Gemini Spec-Driven Development framework.

## Step 0: Project Setup (One-time)

1.  **Copy Configuration**: Copy the `.gemini/` directory and its contents to your project's root directory.
    ```bash
    cp -r /path/to/gemini-spec-driven-dev-template/.gemini/ .
    ```
2.  **Create Kiro Directories**: Create the `.kiro/steering` and `.kiro/specs` directories in your project's root.
    ```bash
    mkdir -p .kiro/steering .kiro/specs
    ```
3.  **Create Steering Documents**: Create the following three files in `.kiro/steering/`. You can start with empty files and gradually fill them in, or use the `steering` command to generate them.
    - `product.md`: Defines product goals, target users, and core value.
    - `tech.md`: Defines the tech stack, architecture, and development environment.
    - `structure.md`: Defines the project's directory structure and code organization conventions.
    ```bash
    touch .kiro/steering/product.md .kiro/steering/tech.md .kiro/steering/structure.md
    ```

## Development Workflow Example: Adding a "User Login" Feature

### Step 1: Initialize the Spec

-   **Your Command**: `gemini spec-init "User Login Feature"`
-   **Gemini's Action**: Creates the necessary files and directories for the new feature spec (`.kiro/specs/User-Login-Feature/`).

### Step 2: Define Requirements

-   **Your Command**: `gemini spec-requirements "User Login Feature" "As a user, I want to log in with my email and password so that I can access my account."`
-   **Gemini's Action**: Fills in the `requirements.md` file (`.kiro/specs/User-Login-Feature/requirements.md`) based on your description.
-   **Your Approval**: Review the generated `requirements.md`. If satisfied, reply with `Approve requirements`.

### Step 3: Generate Technical Design

-   **Your Command**: `gemini spec-design "User Login Feature"`
-   **Gemini's Action**: Generates the technical design in `design.md` (`.kiro/specs/User-Login-Feature/design.md`) based on approved requirements and steering documents.
-   **Your Approval**: Review the generated `design.md`. If satisfied, reply with `Approve design`.

### Step 4: Generate Implementation Tasks

-   **Your Command**: `gemini spec-tasks "User Login Feature"`
-   **Gemini's Action**: Creates a task list in `tasks.md` (`.kiro/specs/User-Login-Feature/tasks.md`) based on the approved design.
-   **Your Approval**: Review the generated `tasks.md`. If satisfied, reply with `Approve tasks`.

### Step 5: Implementation

-   **Your Command**: `cat .kiro/specs/User-Login-Feature/tasks.md` (to view the generated tasks)
-   **Your Command**: `gemini "Implement the first task: Create the login form component as per tasks.md"` (or similar instruction to start coding)

## Command Summary

-   `gemini steering`: Analyzes the project and generates/updates core steering documents (`product.md`, `tech.md`, `structure.md`).
    -   **Example**: `gemini steering`
-   `gemini steering-custom <document_name> "<topic_purpose>" "<initial_content>"`: Creates custom steering documents for specialized contexts.
    -   **Example**: `gemini steering-custom "api-standards.md" "Guidelines for RESTful API design" "# API Standards\n\n- Use RESTful principles\n- Version APIs\n- Handle errors consistently"`
-   `gemini spec-init <feature_name>`: Initializes a new feature spec.
    -   **Example**: `gemini spec-init "User Profile Management"`
-   `gemini spec-requirements <feature_name> "<description>"`: Generates requirements.
    -   **Example**: `gemini spec-requirements "User Profile Management" "As a user, I want to update my profile information."`
-   `gemini spec-design <feature_name>`: Generates the technical design.
    -   **Example**: `gemini spec-design "User Profile Management"`
-   `gemini spec-tasks <feature_name>`: Generates implementation tasks.
    -   **Example**: `gemini spec-tasks "User Profile Management"`
-   `gemini spec-status <feature_name>`: Shows current status and progress for a feature.
    -   **Example**: `gemini spec-status "User Profile Management"`