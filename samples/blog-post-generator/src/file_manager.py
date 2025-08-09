import os
import re

def create_posts_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)

def generate_kebab_cased_filename(title):
    title = title.strip().lower()
    title = re.sub(r'[^a-z0-9\s-]', '', title) # Remove special characters except spaces and hyphens
    title = re.sub(r'\s+', '-', title) # Replace spaces with hyphens
    return f"{title}.md"

def save_markdown_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
