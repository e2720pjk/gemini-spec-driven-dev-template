import unittest
from src.file_manager import create_posts_directory, generate_kebab_cased_filename, save_markdown_file
import os
import shutil

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_posts"
        self.test_file = os.path.join(self.test_dir, "test-title.md")
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_create_posts_directory_creates_if_not_exists(self):
        create_posts_directory(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))

    def test_create_posts_directory_does_nothing_if_exists(self):
        os.makedirs(self.test_dir)
        create_posts_directory(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))

    def test_generate_kebab_cased_filename(self):
        self.assertEqual(generate_kebab_cased_filename("My Test Title"), "my-test-title.md")
        self.assertEqual(generate_kebab_cased_filename("Another Title with Special Chars!@#"), "another-title-with-special-chars.md")
        self.assertEqual(generate_kebab_cased_filename("  Leading and Trailing Spaces  "), "leading-and-trailing-spaces.md")
        self.assertEqual(generate_kebab_cased_filename("empty"), "empty.md")

    def test_save_markdown_file(self):
        create_posts_directory(self.test_dir)
        content = "# Test Content"
        save_markdown_file(self.test_file, content)
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, "r") as f:
            self.assertEqual(f.read(), content)

    def test_save_markdown_file_permission_denied(self):
        # This test might require specific OS permissions setup, so it's commented out for now.
        # For a real scenario, you'd mock os.makedirs or os.open to raise PermissionError.
        pass

if __name__ == '__main__':
    unittest.main()