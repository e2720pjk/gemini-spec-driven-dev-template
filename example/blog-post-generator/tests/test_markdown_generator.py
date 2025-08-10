import unittest
from src.markdown_generator import generate_markdown_header, generate_markdown_content
import datetime

class TestMarkdownGenerator(unittest.TestCase):

    def test_generate_markdown_header(self):
        title = "My Awesome Post"
        author = "John Doe"
        date = datetime.date(2025, 1, 1)
        expected_header = """
---
title: My Awesome Post
author: John Doe
date: 2025-01-01
---

"""
        self.assertEqual(generate_markdown_header(title, author, date), expected_header)

    def test_generate_markdown_content(self):
        title = "My Awesome Post"
        author = "John Doe"
        date = datetime.date(2025, 1, 1)
        content = "This is the body of the post."
        expected_full_content = """
---
title: My Awesome Post
author: John Doe
date: 2025-01-01
---

This is the body of the post."""
        self.assertEqual(generate_markdown_content(title, author, date, content), expected_full_content)

if __name__ == '__main__':
    unittest.main()