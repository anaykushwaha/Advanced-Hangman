# test_validator.py
# Unit tests for validator.py

import unittest

from game.validator import Validator


class TestValidator(unittest.TestCase): 
    # Unit tests for the Player class 

    # normalize_letter

    def test_normalize_letter(self):
        self.assertEqual(
            Validator.normalize_letter(" a "),
            "A"
        )

    # is_single_letter

    def test_single_letter_lowercase(self):
        self.assertTrue(
            Validator.is_single_letter("a")
        )

    def test_single_letter_uppercase(self):
        self.assertTrue(
            Validator.is_single_letter("Z")
        )

    def test_invalid_empty(self):
        self.assertFalse(
            Validator.is_single_letter("")
        )

    def test_invalid_multiple_letters(self):
        self.assertFalse(
            Validator.is_single_letter("ab")
        )

    def test_invalid_digit(self):
        self.assertFalse(
            Validator.is_single_letter("5")
        )

    def test_invalid_symbol(self):
        self.assertFalse(
            Validator.is_single_letter("@")
        )

    # validate_letter

    def test_validate_letter_returns_uppercase(self):
        self.assertEqual(
            Validator.validate_letter("b"),
            "B"
        )

    def test_validate_letter_strips_spaces(self):
        self.assertEqual(
            Validator.validate_letter(" c "),
            "C"
        )

    def test_validate_letter_invalid(self):
        with self.assertRaises(ValueError):
            Validator.validate_letter("12")

    def test_validate_letter_empty(self):
        with self.assertRaises(ValueError):
            Validator.validate_letter("")

    # already_guessed

    def test_already_guessed_correct(self):
        self.assertTrue(
            Validator.already_guessed(
                "A",
                {"A"},
                set()
            )
        )

    def test_already_guessed_wrong(self):
        self.assertTrue(
            Validator.already_guessed(
                "B",
                set(),
                {"B"}
            )
        )

    def test_not_already_guessed(self):
        self.assertFalse(
            Validator.already_guessed(
                "C",
                {"A"},
                {"B"}
            )
        )

    # Menu validation

    def test_valid_menu_choice(self):
        self.assertTrue(
            Validator.valid_menu_choice("1")
        )

    def test_invalid_menu_choice(self):
        self.assertFalse(
            Validator.valid_menu_choice("99")
        )

    # Yes / No

    def test_is_yes(self):
        self.assertTrue(
            Validator.is_yes("y")
        )

    def test_is_no(self):
        self.assertTrue(
            Validator.is_no("n")
        )

    def test_not_yes(self):
        self.assertFalse(
            Validator.is_yes("maybe")
        )

    def test_not_no(self):
        self.assertFalse(
            Validator.is_no("yes")
        )

    # Commands

    def test_is_quit(self):
        self.assertTrue(
            Validator.is_quit("quit")
        )

    def test_is_save(self):
        self.assertTrue(
            Validator.is_save("save")
        )

    def test_is_load(self):
        self.assertTrue(
            Validator.is_load("load")
        )

    def test_is_hint(self):
        self.assertTrue(
            Validator.is_hint("hint")
        )

    # Player names

    def test_valid_player_name(self):
        self.assertEqual(
            Validator.validate_player_name("Anay"),
            "Anay"
        )

    def test_player_name_trimmed(self):
        self.assertEqual(
            Validator.validate_player_name("  John  "),
            "John"
        )

    def test_empty_player_name(self):
        with self.assertRaises(ValueError):
            Validator.validate_player_name("")

    def test_long_player_name(self):
        with self.assertRaises(ValueError):
            Validator.validate_player_name(
                "A" * 25
            )

    def test_invalid_player_name_character(self):
        with self.assertRaises(ValueError):
            Validator.validate_player_name(
                "John!"
            )

    # Positive numbers

    def test_positive_number(self):
        self.assertTrue(
            Validator.is_positive_number("5")
        )

    def test_zero_not_positive(self):
        self.assertFalse(
            Validator.is_positive_number("0")
        )

    def test_negative_not_positive(self):
        self.assertFalse(
            Validator.is_positive_number("-3")
        )

    def test_not_number(self):
        self.assertFalse(
            Validator.is_positive_number("abc")
        )

    # Word validation

    def test_validate_word(self):
        self.assertEqual(
            Validator.validate_word("python"),
            "PYTHON"
        )

    def test_validate_word_with_space(self):
        self.assertEqual(
            Validator.validate_word("ice cream"),
            "ICE CREAM"
        )

    def test_validate_word_invalid_character(self):
        with self.assertRaises(ValueError):
            Validator.validate_word("abc123")

    def test_empty_word(self):
        with self.assertRaises(ValueError):
            Validator.validate_word("")

    # Category validation

    def test_valid_category(self):
        self.assertEqual(
            Validator.validate_category(
                "Animals"
            ),
            "Animals"
        )

    def test_trimmed_category(self):
        self.assertEqual(
            Validator.validate_category(
                "  Food  "
            ),
            "Food"
        )

    def test_empty_category(self):
        with self.assertRaises(ValueError):
            Validator.validate_category(
                ""
            )

    # not_empty

    def test_not_empty(self):
        self.assertTrue(
            Validator.not_empty("Hello")
        )

    def test_not_empty_spaces(self):
        self.assertFalse(
            Validator.not_empty("    ")
        )


if __name__ == "__main__":
    unittest.main() 

