
---

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
