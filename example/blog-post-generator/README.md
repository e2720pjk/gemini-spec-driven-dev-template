### Blog Post Generator CLI Tool

This project includes a simple command-line tool to generate Markdown blog posts.

#### Usage:

1.  **Run the tool**:
    ```bash
    python3 src/main.py
    ```
2.  **Follow the prompts**: The tool will ask you for the blog post title, author, and content.
3.  **Output**: A Markdown file will be created in a `posts/` directory (created if it doesn't exist) with a kebab-cased filename derived from your title. The file will include a header with the provided metadata.

**Example:**

```
--- Blog Post Generator ---
Enter blog post title: My First Blog Post
Enter author's name: John Doe
Enter blog post content: This is the content of my first blog post.
Blog post saved to posts/my-first-blog-post.md
```