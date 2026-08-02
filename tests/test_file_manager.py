# test_file_manager.py 
# Unit tests for file_manager.py 

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from utils.file_manager import FileManager


class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.temp_directory = Path(
            tempfile.mkdtemp()
        )

    def tearDown(self):
        shutil.rmtree(
            self.temp_directory,
            ignore_errors=True
        )

    # ---------------------------------------------------------
    # Text Files
    # ---------------------------------------------------------

    def test_save_text_creates_file(self):
        path = self.temp_directory / "hello.txt"

        FileManager.save_text(
            path,
            "Hello World"
        )

        self.assertTrue(
            path.exists()
        )

    def test_load_text(self):
        path = self.temp_directory / "text.txt"

        path.write_text(
            "Python Testing",
            encoding="utf-8"
        )

        result = FileManager.load_text(path)

        self.assertEqual(
            result,
            "Python Testing"
        )

    def test_save_and_load_text(self):
        path = self.temp_directory / "notes.txt"

        FileManager.save_text(
            path,
            "Advanced Hangman"
        )

        result = FileManager.load_text(path)

        self.assertEqual(
            result,
            "Advanced Hangman"
        )

    def test_save_text_overwrites_existing_file(self):
        path = self.temp_directory / "overwrite.txt"

        path.write_text(
            "Old",
            encoding="utf-8"
        )

        FileManager.save_text(
            path,
            "New"
        )

        self.assertEqual(
            FileManager.load_text(path),
            "New"
        )

    def test_save_text_creates_parent_directory(self):
        path = (
            self.temp_directory
            / "folder"
            / "subfolder"
            / "file.txt"
        )

        FileManager.save_text(
            path,
            "Created"
        )

        self.assertTrue(
            path.exists()
        )

    def test_load_empty_text_file(self):
        path = self.temp_directory / "empty.txt"

        path.write_text(
            "",
            encoding="utf-8"
        )

        self.assertEqual(
            FileManager.load_text(path),
            ""
        )

    def test_unicode_text(self):
        path = self.temp_directory / "unicode.txt"

        text = "こんにちは 😀"

        FileManager.save_text(
            path,
            text
        )

        self.assertEqual(
            FileManager.load_text(path),
            text
        ) 

        # ---------------------------------------------------------
    # JSON Files
    # ---------------------------------------------------------

    def test_save_json_creates_file(self):
        path = self.temp_directory / "data.json"

        FileManager.save_json(
            path,
            {"score": 100}
        )

        self.assertTrue(
            path.exists()
        )

    def test_load_json(self):
        path = self.temp_directory / "player.json"

        data = {
            "name": "Alex",
            "score": 250
        }

        path.write_text(
            json.dumps(data),
            encoding="utf-8"
        )

        result = FileManager.load_json(path)

        self.assertEqual(
            result,
            data
        )

    def test_save_and_load_json(self):
        path = self.temp_directory / "save.json"

        data = {
            "player": "John",
            "score": 500,
            "lives": 7
        }

        FileManager.save_json(
            path,
            data
        )

        result = FileManager.load_json(path)

        self.assertEqual(
            result,
            data
        )

    def test_save_json_overwrites_existing_file(self):
        path = self.temp_directory / "overwrite.json"

        FileManager.save_json(
            path,
            {"old": 1}
        )

        FileManager.save_json(
            path,
            {"new": 2}
        )

        result = FileManager.load_json(path)

        self.assertEqual(
            result,
            {"new": 2}
        )

    def test_save_json_nested_directory(self):
        path = (
            self.temp_directory
            / "folder"
            / "subfolder"
            / "game.json"
        )

        FileManager.save_json(
            path,
            {"value": 10}
        )

        self.assertTrue(
            path.exists()
        )

    def test_save_json_list(self):
        path = self.temp_directory / "list.json"

        data = [
            1,
            2,
            3,
            4
        ]

        FileManager.save_json(
            path,
            data
        )

        result = FileManager.load_json(path)

        self.assertEqual(
            result,
            data
        )

    def test_save_json_with_indent(self):
        path = self.temp_directory / "pretty.json"

        FileManager.save_json(
            path,
            {"a": 1},
            indent=2
        )

        text = path.read_text(
            encoding="utf-8"
        )

        self.assertIn(
            "\n",
            text
        )

    def test_unicode_json(self):
        path = self.temp_directory / "unicode.json"

        data = {
            "text": "こんにちは 😀"
        }

        FileManager.save_json(
            path,
            data
        )

        result = FileManager.load_json(path)

        self.assertEqual(
            result,
            data
        ) 

        # ---------------------------------------------------------
    # Utility Methods
    # ---------------------------------------------------------

    def test_exists_true(self):
        path = self.temp_directory / "exists.txt"

        path.write_text(
            "Hello",
            encoding="utf-8"
        )

        self.assertTrue(
            FileManager.exists(path)
        )

    def test_exists_false(self):
        path = self.temp_directory / "missing.txt"

        self.assertFalse(
            FileManager.exists(path)
        )

    def test_delete_existing_file(self):
        path = self.temp_directory / "delete.txt"

        path.write_text(
            "Delete Me",
            encoding="utf-8"
        )

        result = FileManager.delete(path)

        self.assertTrue(
            result
        )

        self.assertFalse(
            path.exists()
        )

    def test_delete_missing_file(self):
        path = self.temp_directory / "missing.txt"

        result = FileManager.delete(path)

        self.assertFalse(
            result
        )

    def test_create_folder(self):
        folder = (
            self.temp_directory
            / "folder1"
            / "folder2"
        )

        FileManager.create_folder(folder)

        self.assertTrue(
            folder.exists()
        )

        self.assertTrue(
            folder.is_dir()
        )

    def test_create_existing_folder(self):
        folder = self.temp_directory / "existing"

        folder.mkdir()

        FileManager.create_folder(folder)

        self.assertTrue(
            folder.exists()
        )

    def test_file_size(self):
        path = self.temp_directory / "size.txt"

        path.write_text(
            "abcdef",
            encoding="utf-8"
        )

        self.assertEqual(
            FileManager.file_size(path),
            6
        )

    def test_file_size_empty_file(self):
        path = self.temp_directory / "empty.txt"

        path.write_text(
            "",
            encoding="utf-8"
        )

        self.assertEqual(
            FileManager.file_size(path),
            0
        )

    def test_file_size_missing_file(self):
        path = self.temp_directory / "missing.txt"

        self.assertEqual(
            FileManager.file_size(path),
            0
        )

    def test_clear_file(self):
        path = self.temp_directory / "clear.txt"

        path.write_text(
            "Some text",
            encoding="utf-8"
        )

        FileManager.clear_file(path)

        self.assertEqual(
            path.read_text(
                encoding="utf-8"
            ),
            ""
        )

    def test_clear_empty_file(self):
        path = self.temp_directory / "empty.txt"

        path.write_text(
            "",
            encoding="utf-8"
        )

        FileManager.clear_file(path)

        self.assertEqual(
            path.read_text(
                encoding="utf-8"
            ),
            ""
        )

    def test_clear_file_creates_parent_directory(self):
        path = (
            self.temp_directory
            / "folder"
            / "subfolder"
            / "clear.txt"
        )

        FileManager.clear_file(path)

        self.assertTrue(
            path.exists()
        )

        self.assertEqual(
            path.read_text(
                encoding="utf-8"
            ),
            ""
        ) 

        # ---------------------------------------------------------
    # Edge Cases
    # ---------------------------------------------------------

    def test_save_text_multiple_times(self):
        path = self.temp_directory / "multiple.txt"

        FileManager.save_text(
            path,
            "First"
        )

        FileManager.save_text(
            path,
            "Second"
        )

        FileManager.save_text(
            path,
            "Third"
        )

        self.assertEqual(
            FileManager.load_text(path),
            "Third"
        )

    def test_save_json_multiple_times(self):
        path = self.temp_directory / "multiple.json"

        FileManager.save_json(
            path,
            {"value": 1}
        )

        FileManager.save_json(
            path,
            {"value": 2}
        )

        FileManager.save_json(
            path,
            {"value": 3}
        )

        self.assertEqual(
            FileManager.load_json(path),
            {"value": 3}
        )

    def test_delete_then_exists(self):
        path = self.temp_directory / "delete.txt"

        path.write_text(
            "Delete",
            encoding="utf-8"
        )

        FileManager.delete(path)

        self.assertFalse(
            FileManager.exists(path)
        )

    def test_create_folder_twice(self):
        folder = self.temp_directory / "folder"

        FileManager.create_folder(folder)
        FileManager.create_folder(folder)

        self.assertTrue(
            folder.exists()
        )

    def test_clear_file_twice(self):
        path = self.temp_directory / "clear.txt"

        FileManager.clear_file(path)
        FileManager.clear_file(path)

        self.assertEqual(
            FileManager.load_text(path),
            ""
        )

    def test_save_empty_text(self):
        path = self.temp_directory / "empty.txt"

        FileManager.save_text(
            path,
            ""
        )

        self.assertEqual(
            FileManager.load_text(path),
            ""
        )

    def test_save_empty_json_object(self):
        path = self.temp_directory / "empty.json"

        FileManager.save_json(
            path,
            {}
        )

        self.assertEqual(
            FileManager.load_json(path),
            {}
        )

    def test_save_empty_json_list(self):
        path = self.temp_directory / "list.json"

        FileManager.save_json(
            path,
            []
        )

        self.assertEqual(
            FileManager.load_json(path),
            []
        )

    def test_exists_after_clear(self):
        path = self.temp_directory / "clear.txt"

        FileManager.save_text(
            path,
            "Testing"
        )

        FileManager.clear_file(path)

        self.assertTrue(
            FileManager.exists(path)
        )

    def test_file_size_after_clear(self):
        path = self.temp_directory / "clear.txt"

        FileManager.save_text(
            path,
            "abcdef"
        )

        FileManager.clear_file(path)

        self.assertEqual(
            FileManager.file_size(path),
            0
        )

    def test_save_json_boolean_values(self):
        path = self.temp_directory / "bool.json"

        data = {
            "won": True,
            "finished": False
        }

        FileManager.save_json(
            path,
            data
        )

        self.assertEqual(
            FileManager.load_json(path),
            data
        )

    def test_save_json_nested_dictionary(self):
        path = self.temp_directory / "nested.json"

        data = {
            "player": {
                "name": "Alex",
                "score": 100
            },
            "difficulty": "Hard"
        }

        FileManager.save_json(
            path,
            data
        )

        self.assertEqual(
            FileManager.load_json(path),
            data
        )

    def test_save_json_nested_list(self):
        path = self.temp_directory / "nested_list.json"

        data = {
            "letters": [
                "A",
                "B",
                "C"
            ]
        }

        FileManager.save_json(
            path,
            data
        )

        self.assertEqual(
            FileManager.load_json(path),
            data
        ) 

        # ---------------------------------------------------------
    # Integration Tests
    # ---------------------------------------------------------

    def test_text_file_lifecycle(self):
        path = self.temp_directory / "lifecycle.txt"

        FileManager.save_text(
            path,
            "Hello"
        )

        self.assertTrue(
            FileManager.exists(path)
        )

        self.assertEqual(
            FileManager.load_text(path),
            "Hello"
        )

        FileManager.clear_file(path)

        self.assertEqual(
            FileManager.load_text(path),
            ""
        )

        self.assertTrue(
            FileManager.delete(path)
        )

        self.assertFalse(
            FileManager.exists(path)
        )

    def test_json_file_lifecycle(self):
        path = self.temp_directory / "lifecycle.json"

        data = {
            "score": 250,
            "lives": 5
        }

        FileManager.save_json(
            path,
            data
        )

        self.assertTrue(
            FileManager.exists(path)
        )

        self.assertEqual(
            FileManager.load_json(path),
            data
        )

        self.assertTrue(
            FileManager.delete(path)
        )

        self.assertFalse(
            FileManager.exists(path)
        )

    def test_create_folder_then_save_file(self):
        folder = (
            self.temp_directory
            / "folder"
            / "subfolder"
        )

        FileManager.create_folder(folder)

        path = folder / "file.txt"

        FileManager.save_text(
            path,
            "Advanced Hangman"
        )

        self.assertEqual(
            FileManager.load_text(path),
            "Advanced Hangman"
        )

    def test_create_folder_then_save_json(self):
        folder = (
            self.temp_directory
            / "json"
            / "saves"
        )

        FileManager.create_folder(folder)

        path = folder / "save.json"

        data = {
            "player": "John",
            "wins": 15
        }

        FileManager.save_json(
            path,
            data
        )

        self.assertEqual(
            FileManager.load_json(path),
            data
        )

    def test_delete_after_clear(self):
        path = self.temp_directory / "temp.txt"

        FileManager.save_text(
            path,
            "Temporary"
        )

        FileManager.clear_file(path)

        self.assertTrue(
            FileManager.delete(path)
        )

        self.assertFalse(
            FileManager.exists(path)
        )


if __name__ == "__main__":
    unittest.main() 

