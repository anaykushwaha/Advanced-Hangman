# test_word_manager.py 
# Unit tests for word_manager.py 


import unittest
from unittest.mock import patch
from game.word_manager import (
    Word,
    WordManager
)

class TestWord(unittest.TestCase): 
    # Tests for the Word dataclass 

    def test_word_creation(self):
        word = Word(
            text="PYTHON",
            category="Programming",
            difficulty="Easy"
        )

        self.assertEqual(
            word.text,
            "PYTHON"
        )

        self.assertEqual(
            word.category,
            "Programming"
        )

        self.assertEqual(
            word.difficulty,
            "Easy"
        )

    def test_length(self):
        word = Word(
            text="HELLO WORLD",
            category="Phrase",
            difficulty="Easy"
        )

        self.assertEqual(
            word.length,
            10
        )

    def test_word_count(self):
        word = Word(
            text="HELLO WORLD AGAIN",
            category="Phrase",
            difficulty="Easy"
        )

        self.assertEqual(
            word.word_count,
            3
        )


class TestWordManager(unittest.TestCase): 
    # Unit tests for WordManager 

    def setUp(self):

        self.exists = patch(
            "utils.file_manager.FileManager.exists",
            return_value=True
        )

        self.loader = patch(
            "utils.file_manager.FileManager.load_json",
            return_value={
                "Programming": [
                    "Python",
                    "Java"
                ],
                "Animals": [
                    "Tiger"
                ]
            }
        )

        self.exists.start()
        self.loader.start()

        self.manager = WordManager()

    def tearDown(self):
        patch.stopall()

    # Constructor

    def test_manager_created(self):
        self.assertIsInstance(
            self.manager,
            WordManager
        )

    def test_current_word_none(self):
        self.assertIsNone(
            self.manager.current_word
        )

    def test_difficulties_exist(self):
        self.assertEqual(
            set(self.manager.words.keys()),
            {
                "Easy",
                "Medium",
                "Hard",
                "Impossible"
            }
        )

    # Loading

    def test_easy_words_loaded(self):
        self.assertGreater(
            len(self.manager.words["Easy"]),
            0
        )

    def test_total_words(self):
        self.assertGreater(
            self.manager.total_words(),
            0
        )

    def test_all_words_returns_list(self):
        words = self.manager.all_words("Easy")

        self.assertIsInstance(
            words,
            list
        )

    def test_categories(self):
        categories = self.manager.categories(
            "Easy"
        )

        self.assertIn(
            "Programming",
            categories
        )

    def test_difficulties(self):
        difficulties = self.manager.difficulties()

        self.assertEqual(
            len(difficulties),
            4
        )

    def test_exists_true(self):
        self.assertTrue(
            self.manager.exists("python")
        )

    def test_exists_false(self):
        self.assertFalse(
            self.manager.exists("Banana")
        ) 

    # Random Word Selection

    @patch("random.choice")
    def test_random_word(self, mocked_choice):
        sample = self.manager.words["Easy"][0]
        mocked_choice.return_value = sample

        word = self.manager.random_word("Easy")

        self.assertEqual(
            word,
            sample
        )

    @patch("random.choice")
    def test_random_word_sets_current(self, mocked_choice):
        sample = self.manager.words["Easy"][0]
        mocked_choice.return_value = sample

        self.manager.random_word("Easy")

        self.assertEqual(
            self.manager.current(),
            sample
        )

    def test_current_without_selection(self):
        with self.assertRaises(RuntimeError):
            WordManager().current()

    def test_random_word_invalid_difficulty(self):
        with self.assertRaises(KeyError):
            self.manager.random_word("Unknown")

    # Category Selection

    @patch("random.choice")
    def test_random_category_word(self, mocked_choice):
        sample = self.manager.words["Easy"][0]
        mocked_choice.return_value = sample

        word = self.manager.random_category_word(
            "Easy",
            "Programming"
        )

        self.assertEqual(
            word.category,
            "Programming"
        )

    def test_random_category_invalid(self):
        with self.assertRaises(ValueError):
            self.manager.random_category_word(
                "Easy",
                "Nonexistent"
            )

    # Searching

    def test_words_by_length(self):
        words = self.manager.words_by_length(
            6,
            "Easy"
        )

        for word in words:
            self.assertEqual(
                word.length,
                6
            )

    def test_words_by_length_all(self):
        words = self.manager.words_by_length(6)

        self.assertIsInstance(
            words,
            list
        )

    def test_phrases(self):
        self.manager.words["Easy"].append(
            Word(
                text="HELLO WORLD",
                category="Phrase",
                difficulty="Easy"
            )
        )

        phrases = self.manager.phrases("Easy")

        self.assertGreater(
            len(phrases),
            0
        )

        for word in phrases:
            self.assertGreater(
                word.word_count,
                1
            )

    def test_single_words(self):
        singles = self.manager.single_words("Easy")

        for word in singles:
            self.assertEqual(
                word.word_count,
                1
            )

    def test_longest_word(self):
        longest = self.manager.longest_word("Easy")

        self.assertIsInstance(
            longest,
            Word
        )

    def test_shortest_word(self):
        shortest = self.manager.shortest_word("Easy")

        self.assertIsInstance(
            shortest,
            Word
        )

    def test_categories_sorted(self):
        categories = self.manager.categories("Easy")

        self.assertEqual(
            categories,
            sorted(categories)
        )

    def test_total_words_easy(self):
        self.assertEqual(
            self.manager.total_words("Easy"),
            len(self.manager.words["Easy"])
        ) 

    # Statistics

    def test_category_counts(self):
        counts = self.manager.category_counts("Easy")

        self.assertIsInstance(
            counts,
            dict
        )

        self.assertIn(
            "Programming",
            counts
        )

    def test_category_counts_all(self):
        counts = self.manager.category_counts()

        self.assertIsInstance(
            counts,
            dict
        )

    def test_difficulty_counts(self):
        counts = self.manager.difficulty_counts()

        self.assertEqual(
            len(counts),
            4
        )

        self.assertIn(
            "Easy",
            counts
        )

    def test_total_categories(self):
        total = self.manager.total_categories()

        self.assertGreater(
            total,
            0
        )

    # Reload

    @patch.object(WordManager, "load_all")
    def test_reload(self, mocked_load):
        self.manager.reload()

        mocked_load.assert_called_once()

        self.assertIsNone(
            self.manager.current_word
        )

    # Magic Methods

    def test_len(self):
        self.assertEqual(
            len(self.manager),
            self.manager.total_words()
        )

    def test_iter(self):
        words = list(self.manager)

        self.assertEqual(
            len(words),
            self.manager.total_words()
        )

        self.assertIsInstance(
            words[0],
            Word
        )

    def test_contains_operator_true(self):
        self.assertTrue(
            "Python" in self.manager
        )

    def test_contains_operator_false(self):
        self.assertFalse(
            "Banana" in self.manager
        )

    def test_string_representation(self):
        text = str(self.manager)

        self.assertIn(
            "WordManager",
            text
        )

        self.assertIn(
            "Total=",
            text
        )

    def test_repr(self):
        self.assertEqual(
            repr(self.manager),
            str(self.manager)
        )

    # Edge Cases

    def test_empty_word_database(self):
        self.manager.words = {
            "Easy": [],
            "Medium": [],
            "Hard": [],
            "Impossible": []
        }

        self.assertEqual(
            self.manager.total_words(),
            0
        )

    def test_random_word_empty_database(self):
        self.manager.words["Easy"] = []

        with self.assertRaises(ValueError):
            self.manager.random_word("Easy")

    def test_remove_word_empty_database(self):
        self.manager.words["Easy"] = []

        self.assertFalse(
            self.manager.remove_word(
                "Python",
                "Easy"
            )
        )

    def test_exists_empty_database(self):
        self.manager.words = {
            "Easy": [],
            "Medium": [],
            "Hard": [],
            "Impossible": []
        }

        self.assertFalse(
            self.manager.exists("Python")
        )

    def test_categories_empty_database(self):
        self.manager.words["Easy"] = []

        self.assertEqual(
            self.manager.categories("Easy"),
            []
        )

    def test_category_counts_empty(self):
        self.manager.words["Easy"] = []

        self.assertEqual(
            self.manager.category_counts("Easy"),
            {}
        )

    def test_multiple_custom_words(self):
        self.manager.add_word(
            "Computer",
            "Programming",
            "Easy"
        )

        self.manager.add_word(
            "Compiler",
            "Programming",
            "Easy"
        )

        self.assertTrue(
            self.manager.exists("Computer")
        )

        self.assertTrue(
            self.manager.exists("Compiler")
        )


if __name__ == "__main__":
    unittest.main() 

