Analyze the entire project to create or update the steering documents (`product.md`, `tech.md`, `structure.md`).

1.  **Scan Project**: Use `glob` to find all relevant source code files (e.g., `*.js`, `*.py`, `package.json`, etc.).
2.  **Read Files**: Use `read_many_files` to read the content of the scanned files.
3.  **Analyze and Draft**: Analyze the content and generate draft versions of `product.md`, `tech.md`, and `structure.md`.
4.  **Request Approval**: Present the drafts to the user for approval before writing them to the `.kiro/steering/` directory.