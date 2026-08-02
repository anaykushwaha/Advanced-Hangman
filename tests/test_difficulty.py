# test_difficulty.py
# Unit tests for difficulty.py

import unittest

from game.difficulty import (
    Difficulty,
    DifficultyManager,
    DifficultySettings,
)


class TestDifficulty(unittest.TestCase):
    # Unit tests for DifficultyManager

    def setUp(self):
        DifficultyManager.reset()

    def tearDown(self):
        DifficultyManager.reset()

    # Enum Tests

    def test_easy_enum(self):
        self.assertEqual(
            Difficulty.EASY.value,
            "Easy"
        )

    def test_medium_enum(self):
        self.assertEqual(
            Difficulty.MEDIUM.value,
            "Medium"
        )

    def test_hard_enum(self):
        self.assertEqual(
            Difficulty.HARD.value,
            "Hard"
        )

    def test_impossible_enum(self):
        self.assertEqual(
            Difficulty.IMPOSSIBLE.value,
            "Impossible"
        )

    # Default Difficulty

    def test_default_is_medium(self):
        settings = DifficultyManager.get_settings()

        self.assertEqual(
            settings.name,
            "Medium"
        )

    # set_difficulty()

    def test_set_easy(self):
        DifficultyManager.set_difficulty(
            Difficulty.EASY
        )

        self.assertEqual(
            DifficultyManager.get_settings().name,
            "Easy"
        )

    def test_set_medium(self):
        DifficultyManager.set_difficulty(
            Difficulty.MEDIUM
        )

        self.assertEqual(
            DifficultyManager.get_settings().name,
            "Medium"
        )

    def test_set_hard(self):
        DifficultyManager.set_difficulty(
            Difficulty.HARD
        )

        self.assertEqual(
            DifficultyManager.get_settings().name,
            "Hard"
        )

    def test_set_impossible(self):
        DifficultyManager.set_difficulty(
            Difficulty.IMPOSSIBLE
        )

        self.assertEqual(
            DifficultyManager.get_settings().name,
            "Impossible"
        )

    # get()

    def test_get_easy(self):
        settings = DifficultyManager.get(
            Difficulty.EASY
        )

        self.assertEqual(
            settings.max_lives,
            12
        )

    def test_get_medium(self):
        settings = DifficultyManager.get(
            Difficulty.MEDIUM
        )

        self.assertEqual(
            settings.max_lives,
            10
        )

    def test_get_hard(self):
        settings = DifficultyManager.get(
            Difficulty.HARD
        )

        self.assertEqual(
            settings.max_lives,
            8
        )

    def test_get_impossible(self):
        settings = DifficultyManager.get(
            Difficulty.IMPOSSIBLE
        )

        self.assertEqual(
            settings.max_lives,
            6
        )

    # DifficultySettings

    def test_get_returns_settings(self):
        self.assertIsInstance(
            DifficultyManager.get(
                Difficulty.EASY
            ),
            DifficultySettings
        )

    def test_get_settings_returns_settings(self):
        self.assertIsInstance(
            DifficultyManager.get_settings(),
            DifficultySettings
        )

    # get_all()

    def test_get_all_returns_list(self):
        data = DifficultyManager.get_all()

        self.assertIsInstance(
            data,
            list
        )

    def test_get_all_length(self):
        self.assertEqual(
            len(
                DifficultyManager.get_all()
            ),
            4
        )

    # get_names()

    def test_get_names_returns_list(self):
        names = DifficultyManager.get_names()

        self.assertIsInstance(
            names,
            list
        )

    def test_get_names_length(self):
        self.assertEqual(
            len(
                DifficultyManager.get_names()
            ),
            4
        )

    def test_get_names_contains_easy(self):
        self.assertIn(
            "Easy",
            DifficultyManager.get_names()
        )

    def test_get_names_contains_medium(self):
        self.assertIn(
            "Medium",
            DifficultyManager.get_names()
        )

    def test_get_names_contains_hard(self):
        self.assertIn(
            "Hard",
            DifficultyManager.get_names()
        )

    def test_get_names_contains_impossible(self):
        self.assertIn(
            "Impossible",
            DifficultyManager.get_names()
        )

    # from_string()

    def test_from_string_easy(self):
        self.assertEqual(
            DifficultyManager.from_string(
                "Easy"
            ),
            Difficulty.EASY
        )

    def test_from_string_lowercase(self):
        self.assertEqual(
            DifficultyManager.from_string(
                "medium"
            ),
            Difficulty.MEDIUM
        )

    def test_from_string_with_spaces(self):
        self.assertEqual(
            DifficultyManager.from_string(
                "  hard  "
            ),
            Difficulty.HARD
        )

    def test_from_string_impossible(self):
        self.assertEqual(
            DifficultyManager.from_string(
                "Impossible"
            ),
            Difficulty.IMPOSSIBLE
        )

    def test_from_string_invalid(self):
        with self.assertRaises(
            ValueError
        ):
            DifficultyManager.from_string(
                "Impossible++"
            )

    # print_difficulties()

    def test_print_difficulties(self):
        from unittest.mock import patch

        with patch("builtins.print") as mocked:
            DifficultyManager.print_difficulties()

            self.assertGreater(
                mocked.call_count,
                0
            )

    # reset()

    def test_reset(self):
        DifficultyManager.set_difficulty(
            Difficulty.HARD
        )

        DifficultyManager.reset()

        self.assertEqual(
            DifficultyManager.get_settings().name,
            "Medium"
        )

    # Individual Setting Values

    def test_easy_score_multiplier(self):
        self.assertEqual(
            DifficultyManager.get(
                Difficulty.EASY
            ).score_multiplier,
            1.0
        )

    def test_medium_score_multiplier(self):
        self.assertEqual(
            DifficultyManager.get(
                Difficulty.MEDIUM
            ).score_multiplier,
            1.5
        )

    def test_hard_score_multiplier(self):
        self.assertEqual(
            DifficultyManager.get(
                Difficulty.HARD
            ).score_multiplier,
            2.0
        )

    def test_impossible_score_multiplier(self):
        self.assertEqual(
            DifficultyManager.get(
                Difficulty.IMPOSSIBLE
            ).score_multiplier,
            3.5
        )

    def test_easy_word_file(self):
        self.assertEqual(
            DifficultyManager.get(
                Difficulty.EASY
            ).word_file,
            "data/easy_words.json"
        )

    def test_impossible_has_no_hints(self):
        self.assertEqual(
            DifficultyManager.get(
                Difficulty.IMPOSSIBLE
            ).hints_allowed,
            0
        )

    def test_easy_has_five_hints(self):
        self.assertEqual(
            DifficultyManager.get(
                Difficulty.EASY
            ).hints_allowed,
            5
        )


if __name__ == "__main__":
    unittest.main() 

