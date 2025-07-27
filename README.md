# Gemini Spec-Driven Development Template

This is a template for setting up a spec-driven development workflow with Gemini.

## Overview

This template provides a structured approach to software development using Gemini, based on the concept of spec-driven development. It helps ensure that development is aligned with product goals, technical architecture, and project conventions.

## Getting Started

### Step 0: Project Setup (One-time)

1.  **Copy Configuration**: Copy the `.gemini/` directory and its contents to your project's root directory.
    ```bash
    cp -r /path/to/gemini-spec-driven-dev-template/.gemini/ .
    ```
2.  **Create Kiro Directories**: Create the `.kiro/steering` and `.kiro/specs` directories in your project's root.
    ```bash
    mkdir -p .kiro/steering .kiro/specs
    ```
3.  **Create Steering Documents**: These foundational documents guide Gemini's understanding of your project. **It is highly recommended to use the `gemini steering` command to generate these files**, as it intelligently analyzes your project and populates them with initial content.
    ```bash
    gemini steering
    ```
    Alternatively, you can create empty files and fill them manually:
    - `product.md`: Defines product goals, target users, and core value.
    - `tech.md`: Defines the tech stack, architecture, and development environment.
    - `structure.md`: Defines the project's directory structure and code organization conventions.
    ```bash
    touch .kiro/steering/product.md .kiro/steering/tech.md .kiro/steering/structure.md
    ```

### Development Workflow Example: Adding a "User Login" Feature

#### Step 1: Initialize the Spec

- **Your Command**: `gemini spec-init "User Login Feature"`
- **Gemini's Action**: Creates the necessary files and directories for the new feature spec.

#### Step 2: Define Requirements

- **Your Command**: `gemini spec-requirements "User Login Feature" "As a user, I want to log in with my email and password."`
- **Gemini's Action**: Fills in the `requirements.md` file.
- **Your Approval**: `Approve requirements`

#### Step 3: Generate Technical Design

- **Your Command**: `gemini spec-design "User Login Feature"`
- **Gemini's Action**: Generates the technical design in `design.md`.
- **Your Approval**: `Approve design`

#### Step 4: Generate Implementation Tasks

- **Your Command**: `gemini spec-tasks "User Login Feature"`
- **Gemini's Action**: Creates a task list in `tasks.md`.
- **Your Approval**: `Approve tasks`

#### Step 5: Implementation

- **Your Command**: `cat .kiro/specs/User-Login-Feature/tasks.md` (to view tasks)
- **Your Command**: `gemini "Implement the first task: ..."`

## Spec-Driven Development Process

### Process Flow Diagram

This flow requires "Review & Approval" at each phase.

**Steering documents** are documents that record persistent knowledge about the project (architecture, tech stack, code conventions, etc.). Creating and updating them is optional but recommended for long-term maintainability of the project.

```mermaid
graph TD
    A["Project Start"] --> B{"Document<br/>Steering?"}
    B -->|Yes| C["gemini steering"]
    B -->|No| D["gemini spec-init"]
    C --> D
    
    D --> E["gemini spec-requirements"]
    E --> F["requirements.md"]
    F --> G{"Satisfied?"}
    G -->|No| G1["Edit & Revise"]
    G1 --> F
    G -->|Yes| H["To Next Phase"]
    
    H --> I["gemini spec-design"]
    I --> J["design.md"]
    J --> K{"Satisfied?"}
    K -->|No| K1["Edit & Revise"]
    K1 --> J
    K -->|Yes| L["To Next Phase"]
    
    L --> M["gemini spec-tasks"]
    M --> N["tasks.md"]
    N --> O{"Satisfied?"}
    O -->|No| O1["Edit & Revise"]
    O1 --> N
    O -->|Yes| P["Ready for Implementation"]
    
    P --> Q["Start Implementation"]
    Q --> R["gemini spec-status"]
    R --> S{"Complete?"}
    S -->|No| Q
    S -->|Yes| T["Feature Complete"]
    
    T --> U{"Update<br/>Steering?"}
    U -->|Yes| V["gemini steering"]
    U -->|No| W["Done"]
    V --> W
    
    %% Style definitions
    style A fill:#f8f9fa,stroke:#495057
    style C fill:#495057,stroke:#343a40,color:#ffffff
    style D fill:#495057,stroke:#343a40,color:#ffffff
    style E fill:#495057,stroke:#343a40,color:#ffffff
    style I fill:#495057,stroke:#343a40,color:#ffffff
    style M fill:#495057,stroke:#343a40,color:#ffffff
    style R fill:#495057,stroke:#343a40,color:#ffffff
    style V fill:#495057,stroke:#343a40,color:#ffffff
    style F fill:#f8f9fa,stroke:#6c757d
    style J fill:#f8f9fa,stroke:#6c757d
    style N fill:#f8f9fa,stroke:#6c757d
    style H fill:#e8f5e9,stroke:#28a745
    style L fill:#e8f5e9,stroke:#28a745
    style P fill:#e8f5e9,stroke:#28a745
    style Q fill:#adb5bd,stroke:#495057
    style T fill:#6c757d,stroke:#495057,color:#ffffff
    style W fill:#6c757d,stroke:#495057,color:#ffffff
```

### 3-Phase Approval Workflow

The core of this system requires human review and approval at each phase:

```mermaid
sequenceDiagram
    participant D as Developer
    participant G as Gemini
    participant H as Human Reviewer
    
    D->>G: "gemini spec-requirements feature"
    G->>G: "Generate Requirements"
    G->>D: "requirements.md"
    D->>H: "Request Review"
    H->>H: "Review & Edit"
    
    D->>G: "gemini spec-design feature"
    G->>D: "Review confirmation: Please review requirements.md. If approved, reply with `Approve requirements`."
    D->>G: "Approve requirements"
    G->>G: "Generate Design (based on requirements)"
    G->>D: "design.md"
    D->>H: "Request Review"
    H->>H: "Review & Edit"
    
    D->>G: "gemini spec-tasks feature"
    G->>D: "Review confirmation: Please review design.md. If approved, reply with `Approve design`."
    D->>G: "Approve design"
    G->>G: "Generate Tasks (based on design)"
    G->>D: "tasks.md"
    D->>H: "Request Review"
    H->>H: "Review & Edit"
    
    D->>G: "Start Implementation"
```

## Best Practices

### ✅ Recommendations

1.  **Always start with steering**
    - Use `gemini steering` for all scenarios (intelligently handles both creation and updates)
    - The unified command protects existing files while handling them appropriately

2.  **Don't skip phases**
    - Strictly follow the order: Requirements → Design → Tasks
    - Ensure human review at each phase

3.  **Regular progress checks**
    - Use `gemini spec-status` to understand current situation
    - Update task completion status appropriately

4.  **Maintain steering**
    - Run `gemini steering` after major changes (automatically determines update strategy)
    - Update as the project grows

### ❌ Things to Avoid

1.  **Moving to next phase without approval**
    - Don't forget to respond to confirmation prompts

2.  **Neglecting steering documents**
    - Outdated information hinders development

3.  **Not updating task status**
    - Progress becomes unclear and management becomes difficult

## Project Structure

```
.
├── .gemini/
│   ├── commands/          # Gemini command definitions
│   │   ├── spec-init.md
│   │   ├── spec-requirements.md
│   │   ├── spec-design.md
│   │   ├── spec-tasks.md
│   │   ├── spec-status.md
│   │   ├── steering.md          # Unified steering command
│   │   └── steering-custom.md
│   └── settings.json
├── .kiro/
│   ├── steering/          # Steering documents
│   │   ├── product.md
│   │   ├── tech.md
│   │   └── structure.md
│   └── specs/             # Feature specifications
│       └── [feature-name]/
│           ├── spec.json      # Phase approval status
│           ├── requirements.md # Requirements document
│           ├── design.md      # Technical design document
│           └── tasks.md       # Implementation tasks
├── docs/
│   ├── architecture.md
│   ├── index.md
│   └── usage.md
├── README.md              # English version README
├── README.zh-TW.md        # Traditional Chinese version README
└── (your project files)
```

## Automation Features (Simulated)

Gemini simulates automation through interactive approvals and file updates:

-   **Task Progress Tracking**: Manually update `tasks.md` checkboxes. `gemini spec-status` will parse and report progress.
-   **Specification Compliance Checking**: Gemini will check `spec.json` for phase approvals before proceeding to the next stage.
-   **Context Preservation**: Gemini will always refer to the `.kiro/steering/` and `.kiro/specs/` documents for context.
-   **Steering Drift Detection**: The `gemini steering` command will analyze the project and suggest updates to steering documents.

## Troubleshooting

### When commands don't work
1.  Check existence of `.gemini/commands/` directory.
2.  Verify command file naming convention (`command-name.md`).
3.  Ensure you are in the correct project directory.

### When stuck in approval flow
1.  Check that you're responding correctly to review confirmation prompts (e.g., `Approve requirements`).
2.  Verify previous phase approval is complete by checking `spec.json`.
3.  Use `gemini spec-status <feature_name>` to diagnose current state.
4.  Manually check/edit `spec.json` if needed.

## Command Summary

- `gemini steering`: Analyzes the project and generates steering documents.
- `gemini steering-custom`: Creates custom steering documents for specialized contexts.
- `gemini spec-init <feature_name>`: Initializes a new feature spec.
- `gemini spec-requirements <feature_name> "<description>"`: Generates requirements.
- `gemini spec-design <feature_name>`: Generates the technical design.
- `gemini spec-tasks <feature_name>`: Generates implementation tasks.
- `gemini spec-status <feature_name>`: Shows current status and progress for a feature.
