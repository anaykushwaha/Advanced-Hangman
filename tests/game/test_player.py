# test_player.py
# Unit tests for player.py

import unittest

from game.player import Player


class TestPlayer(unittest.TestCase):
    # Unit tests for the Player class

    def setUp(self):
        self.player = Player("Anay")

    # Initialization

    def test_player_name(self):
        self.assertEqual(self.player.name, "Anay")

    def test_initial_score(self):
        self.assertEqual(self.player.score, 0)

    def test_initial_lives(self):
        self.assertEqual(
            self.player.lives_remaining,
            self.player.max_lives,
        )

    def test_initial_guess_sets_empty(self):
        self.assertEqual(len(self.player.correct_letters), 0)
        self.assertEqual(len(self.player.wrong_letters), 0)

    def test_initial_statistics(self):
        self.assertEqual(self.player.total_guesses, 0)
        self.assertEqual(self.player.correct_guesses, 0)
        self.assertEqual(self.player.wrong_guesses, 0)

    # Score

    def test_add_score(self):
        self.player.add_score(150)

        self.assertEqual(
            self.player.score,
            150,
        )

    def test_multiple_score_additions(self):
        self.player.add_score(100)
        self.player.add_score(250)

        self.assertEqual(
            self.player.score,
            350,
        )

    def test_score_never_negative(self):
        self.player.add_score(100)
        self.player.add_score(-500)

        self.assertEqual(
            self.player.score,
            0,
        )

    # Correct guesses

    def test_add_correct_guess(self):
        self.player.add_correct_guess("A")

        self.assertIn("A", self.player.correct_letters)
        self.assertEqual(self.player.correct_guesses, 1)
        self.assertEqual(self.player.total_guesses, 1)

    def test_duplicate_correct_guess(self):
        self.player.add_correct_guess("A")
        self.player.add_correct_guess("A")

        self.assertEqual(self.player.correct_guesses, 1)
        self.assertEqual(self.player.total_guesses, 1)

    def test_multiple_correct_guesses(self):
        for letter in "ABCDE":
            self.player.add_correct_guess(letter)

        self.assertEqual(self.player.correct_guesses, 5)
        self.assertEqual(self.player.total_guesses, 5)

    # Wrong guesses

    def test_add_wrong_guess(self):
        starting = self.player.lives_remaining

        self.player.add_wrong_guess("Z")

        self.assertIn("Z", self.player.wrong_letters)
        self.assertEqual(self.player.wrong_guesses, 1)
        self.assertEqual(self.player.total_guesses, 1)
        self.assertEqual(
            self.player.lives_remaining,
            starting - 1,
        )

    def test_duplicate_wrong_guess(self):
        self.player.add_wrong_guess("Z")
        self.player.add_wrong_guess("Z")

        self.assertEqual(self.player.wrong_guesses, 1)
        self.assertEqual(self.player.total_guesses, 1)

    def test_player_loses_after_all_lives(self):
        for i in range(self.player.max_lives):
            self.player.add_wrong_guess(chr(65 + i))

        self.assertTrue(self.player.lost)
        self.assertFalse(self.player.is_alive)

    # Hint usage

    def test_use_hint(self):
        self.player.use_hint()

        self.assertEqual(
            self.player.hints_used,
            1,
        )

    # Guess lookup

    def test_has_guessed_correct(self):
        self.player.add_correct_guess("P")

        self.assertTrue(
            self.player.has_guessed("P")
        )

    def test_has_guessed_wrong(self):
        self.player.add_wrong_guess("Q")

        self.assertTrue(
            self.player.has_guessed("Q")
        )

    def test_has_not_guessed(self):
        self.assertFalse(
            self.player.has_guessed("X")
        )

    # Accuracy

    def test_accuracy_no_guesses(self):
        self.assertEqual(
            self.player.accuracy,
            0.0,
        )

    def test_accuracy_half_correct(self):
        for letter in "ABCDE":
            self.player.add_correct_guess(letter)

        for letter in "FGHIJ":
            self.player.add_wrong_guess(letter)

        self.assertEqual(
            self.player.accuracy,
            50.0,
        )

    def test_accuracy_all_correct(self):
        for letter in "ABCDEFGH":
            self.player.add_correct_guess(letter)

        self.assertEqual(
            self.player.accuracy,
            100.0,
        )

    # Reset

    def test_reset(self):
        self.player.add_score(500)
        self.player.add_correct_guess("A")
        self.player.add_wrong_guess("B")
        self.player.use_hint()

        self.player.reset()

        self.assertEqual(self.player.score, 0)
        self.assertEqual(
            self.player.lives_remaining,
            self.player.max_lives,
        )
        self.assertEqual(self.player.total_guesses, 0)
        self.assertEqual(self.player.correct_guesses, 0)
        self.assertEqual(self.player.wrong_guesses, 0)
        self.assertEqual(self.player.hints_used, 0)
        self.assertEqual(len(self.player.correct_letters), 0)
        self.assertEqual(len(self.player.wrong_letters), 0)

    # Win/Loss

    def test_mark_win(self):
        # Current implementation only updates won/lost flags.
        self.player.mark_win()

        self.assertTrue(self.player.won)
        self.assertFalse(self.player.lost)

    def test_mark_loss(self):
        self.player.mark_loss()

        self.assertFalse(self.player.won)
        self.assertTrue(self.player.lost)

    # Properties

    def test_is_alive(self):
        self.assertTrue(self.player.is_alive)

    def test_guesses_remaining(self):
        self.assertEqual(
            self.player.guesses_remaining,
            self.player.max_lives,
        )

    # String representation

    def test_string_representation(self):
        player_string = str(self.player)

        self.assertIn("Anay", player_string)
        self.assertIn("score", player_string)
        self.assertIn("lives", player_string)

    # Edge cases

    def test_large_score(self):
        self.player.add_score(1_000_000)

        self.assertEqual(
            self.player.score,
            1_000_000,
        )

    def test_many_correct_guesses(self):
        for i in range(26):
            self.player.add_correct_guess(chr(65 + i))

        self.assertEqual(
            self.player.correct_guesses,
            26,
        )

    def test_many_wrong_guesses(self):
        for i in range(self.player.max_lives):
            self.player.add_wrong_guess(chr(65 + i))

        self.assertEqual(
            self.player.wrong_guesses,
            self.player.max_lives,
        )


if __name__ == "__main__":
    unittest.main() 

