# Tasks: blog-post-generator

## 1. Setup and Project Structure
- [x] Create project directory and initialize Git repository.
- [x] Create `src/` directory for source code.
- [x] Create `tests/` directory for test files.
- [x] Create `requirements.txt` for Python dependencies.

## 2. `file_manager.py` Component
- [x] **Test**: Write unit tests for `file_manager.py` functions:
    - [x] Test `create_posts_directory` to ensure it creates the directory if it doesn't exist.
    - [x] Test `create_posts_directory` to ensure it does nothing if the directory already exists.
    - [x] Test `generate_kebab_cased_filename` for various title inputs (e.g., spaces, special characters, empty string).
    - [x] Test `save_markdown_file` to ensure it writes content to the correct path.
    - [x] Test `save_markdown_file` for error handling (e.g., permission denied).
- [x] Implement `file_manager.py`:
    - [x] Implement `create_posts_directory` function.
    - [x] Implement `generate_kebab_cased_filename` function.
    - [x] Implement `save_markdown_file` function.

## 3. `markdown_generator.py` Component
- [x] **Test**: Write unit tests for `markdown_generator.py` functions:
    - [x] Test `generate_markdown_header` for correct metadata formatting (title, author, date).
    - [x] Test `generate_markdown_content` to combine header and body correctly.
- [x] Implement `markdown_generator.py`:
    - [x] Implement `generate_markdown_header` function.
    - [x] Implement `generate_markdown_content` function.
    - [x] Choose and integrate a Python Markdown library for robust Markdown generation.

## 4. `main.py` (CLI Entry Point)
- [x] **Test**: Write integration tests for `main.py`:
    - [x] Test the full workflow: prompting, generation, and saving.
    - [x] Test with valid inputs.
    - [x] Test with empty inputs for title, author, and content.
    - [x] Test with special characters in title.
- [x] Implement `main.py`:
    - [x] Implement user prompting for title, author, and content using standard input.
    - [x] Call `markdown_generator.py` functions to generate Markdown.
    - [x] Call `file_manager.py` functions to save the file.
    - [x] Add basic command-line argument parsing (e.g., `--help`, `--version`).

## 5. End-to-End Testing
- [x] **Test**: Write end-to-end tests:
    - [x] Simulate running the CLI tool.
    - [x] Verify the creation of the 'posts' directory.
    - [x] Verify the correct filename (kebab-cased).
    - [x] Verify the content of the generated Markdown file, including metadata.
    - [x] Test error scenarios (e.g., invalid file paths if applicable).

## 6. Documentation and Distribution
- [x] Update `README.md` with usage instructions.
- [x] Add a simple `setup.py` or `pyproject.toml` for packaging and distribution.