import unittest
from unittest.mock import patch
import os
import shutil
import subprocess

class TestE2E(unittest.TestCase):

    def setUp(self):
        self.posts_dir = "posts"
        if os.path.exists(self.posts_dir):
            shutil.rmtree(self.posts_dir)

    def tearDown(self):
        if os.path.exists(self.posts_dir):
            shutil.rmtree(self.posts_dir)

    def test_e2e_valid_input(self):
        title = "My E2E Test Post"
        author = "E2E Author"
        content = "This is the content of the E2E test post."

        process = subprocess.run(
            ["python3", "-m", "src.main"],
            input=f"{title}\n{author}\n{content}\n",
            capture_output=True,
            text=True,
            check=True
        )

        expected_file_path = os.path.join(self.posts_dir, "my-e2e-test-post.md")
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as f:
            file_content = f.read()
            self.assertIn(f"title: {title}", file_content)
            self.assertIn(f"author: {author}", file_content)
            self.assertIn(content, file_content)

        self.assertIn(f"Blog post saved to {expected_file_path}", process.stdout)

    def test_e2e_empty_title(self):
        title = ""
        author = "E2E Author"
        content = "This is the content of the E2E test post."

        process = subprocess.run(
            ["python3", "-m", "src.main"],
            input=f"{title}\n{author}\n{content}\n",
            capture_output=True,
            text=True,
            check=True
        )

        # Expecting a file to be created with an empty title, which will result in '.md'
        expected_file_path = os.path.join(self.posts_dir, ".md")
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as f:
            file_content = f.read()
            self.assertIn(f"title: {title}", file_content)
            self.assertIn(f"author: {author}", file_content)
            self.assertIn(content, file_content)

        self.assertIn(f"Blog post saved to {expected_file_path}", process.stdout)

if __name__ == '__main__':
    unittest.main()
