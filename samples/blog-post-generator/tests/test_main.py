import unittest
from unittest.mock import patch
import os
import shutil
from src.main import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.posts_dir = "posts"
        if os.path.exists(self.posts_dir):
            shutil.rmtree(self.posts_dir)

    def tearDown(self):
        if os.path.exists(self.posts_dir):
            shutil.rmtree(self.posts_dir)

    @patch('builtins.input', side_effect=["Test Title", "Test Author", "Test Content"])
    def test_main_workflow_valid_input(self, mock_input):
        main()
        expected_file_path = os.path.join(self.posts_dir, "test-title.md")
        self.assertTrue(os.path.exists(expected_file_path))
        with open(expected_file_path, "r") as f:
            content = f.read()
            self.assertIn("title: Test Title", content)
            self.assertIn("author: Test Author", content)
            self.assertIn("Test Content", content)

    @patch('builtins.input', side_effect=["", "", ""])
    def test_main_workflow_empty_input(self, mock_input):
        main()
        # Expecting a file to be created even with empty title, but with default name or error handling
        # For now, just check if the posts directory is created
        self.assertTrue(os.path.exists(self.posts_dir))

    @patch('builtins.input', side_effect=["Title with Special Chars!@#", "Author", "Content"])
    def test_main_workflow_special_chars_in_title(self, mock_input):
        main()
        expected_file_path = os.path.join(self.posts_dir, "title-with-special-chars.md")
        self.assertTrue(os.path.exists(expected_file_path))

if __name__ == '__main__':
    unittest.main()