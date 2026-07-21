# test_validator.py 
# Unit tests for validator.py 

import unittest 
from game.validator import Validator 


class TestValidator(unittest.TestCase): 
    # Unit tests for the Validator class 

    def setUp(self):
        self.validator = Validator()

    # Letter Validation

    def test_valid_single_letter_lowercase(self):
        self.assertTrue(
            self.validator.validate_letter("a")
        )

    def test_valid_single_letter_uppercase(self):
        self.assertTrue(
            self.validator.validate_letter("Z")
        )

    def test_invalid_empty_string(self):
        self.assertFalse(
            self.validator.validate_letter("")
        )

    def test_invalid_multiple_letters(self):
        self.assertFalse(
            self.validator.validate_letter("ab")
        )

    def test_invalid_number(self):
        self.assertFalse(
            self.validator.validate_letter("5")
        )

    def test_invalid_special_character(self):
        self.assertFalse(
            self.validator.validate_letter("@")
        )

    def test_invalid_space(self):
        self.assertFalse(
            self.validator.validate_letter(" ")
        )

    # Duplicate Guess Validation

    def test_new_letter_not_duplicate(self):
        guessed = {"A", "B", "C"}

        self.assertFalse(
            self.validator.is_duplicate_guess(
                "D",
                guessed
            )
        )

    def test_duplicate_guess(self):
        guessed = {"A", "B", "C"}

        self.assertTrue(
            self.validator.is_duplicate_guess(
                "A",
                guessed
            )
        )

    def test_duplicate_case_insensitive(self):
        guessed = {"A"}

        self.assertTrue(
            self.validator.is_duplicate_guess(
                "a",
                guessed
            )
        )

    # Menu Choice Validation

    def test_valid_menu_choice(self):
        self.assertTrue(
            self.validator.validate_menu_choice(
                "3",
                1,
                5
            )
        )

    def test_menu_choice_too_small(self):
        self.assertFalse(
            self.validator.validate_menu_choice(
                "0",
                1,
                5
            )
        )

    def test_menu_choice_too_large(self):
        self.assertFalse(
            self.validator.validate_menu_choice(
                "6",
                1,
                5
            )
        )

    def test_menu_choice_not_number(self):
        self.assertFalse(
            self.validator.validate_menu_choice(
                "abc",
                1,
                5
            )
        )

    # Player Name Validation

    def test_valid_player_name(self):
        self.assertTrue(
            self.validator.validate_player_name(
                "Anay"
            )
        )

    def test_player_name_with_spaces(self):
        self.assertTrue(
            self.validator.validate_player_name(
                "John Smith"
            )
        )

    def test_empty_player_name(self):
        self.assertFalse(
            self.validator.validate_player_name("")
        )

    def test_player_name_only_spaces(self):
        self.assertFalse(
            self.validator.validate_player_name(
                "     "
            )
        )

    def test_player_name_too_long(self):
        name = "A" * 100

        self.assertFalse(
            self.validator.validate_player_name(name)
        )

    # Difficulty Validation

    def test_valid_difficulty(self):
        self.assertTrue(
            self.validator.validate_difficulty(
                "Easy"
            )
        )

    def test_invalid_difficulty(self):
        self.assertFalse(
            self.validator.validate_difficulty(
                "Impossible++"
            )
        )

    # Game Mode Validation

    def test_valid_game_mode(self):
        self.assertTrue(
            self.validator.validate_game_mode(
                "Classic"
            )
        )

    def test_invalid_game_mode(self):
        self.assertFalse(
            self.validator.validate_game_mode(
                "Sandbox"
            )
        )

    # File Name Validation

    def test_valid_json_filename(self):
        self.assertTrue(
            self.validator.validate_filename(
                "easy_words.json"
            )
        )

    def test_invalid_filename(self):
        self.assertFalse(
            self.validator.validate_filename(
                "../passwords.txt"
            )
        )

    # Generic Integer Validation

    def test_valid_integer(self):
        self.assertTrue(
            self.validator.is_integer("42")
        )

    def test_negative_integer(self):
        self.assertTrue(
            self.validator.is_integer("-10")
        )

    def test_invalid_integer(self):
        self.assertFalse(
            self.validator.is_integer("12.5")
        )

    def test_invalid_integer_letters(self):
        self.assertFalse(
            self.validator.is_integer("abc")
        )

    # Edge Cases

    def test_none_letter(self):
        self.assertFalse(
            self.validator.validate_letter(None)
        )

    def test_none_player_name(self):
        self.assertFalse(
            self.validator.validate_player_name(None)
        )

    def test_none_menu_choice(self):
        self.assertFalse(
            self.validator.validate_menu_choice(
                None,
                1,
                5
            )
        )

    def test_unicode_letter(self):
        self.assertFalse(
            self.validator.validate_letter("é")
        )

    def test_tab_character(self):
        self.assertFalse(
            self.validator.validate_letter("\t")
        )

    def test_newline_character(self):
        self.assertFalse(
            self.validator.validate_letter("\n")
        )


if __name__ == "__main__":
    unittest.main() 