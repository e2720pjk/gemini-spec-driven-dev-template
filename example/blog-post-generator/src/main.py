import datetime
import os
from src.file_manager import create_posts_directory, generate_kebab_cased_filename, save_markdown_file
from src.markdown_generator import generate_markdown_content

def main():
    print("--- Blog Post Generator ---")
    title = input("Enter blog post title: ")
    author = input("Enter author's name: ")
    content = input("Enter blog post content: ")

    today = datetime.date.today()
    markdown_content = generate_markdown_content(title, author, today, content)

    posts_dir = "posts"
    create_posts_directory(posts_dir)

    filename = generate_kebab_cased_filename(title)
    file_path = os.path.join(posts_dir, filename)

    save_markdown_file(file_path, markdown_content)

    print(f"Blog post saved to {file_path}")

if __name__ == "__main__":
    main()
