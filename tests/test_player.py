# Unit tests for player.py 

import unittest 
from game.player import Player 


class TestPlayer(unittest.TestCase): 
    # Unit tests for the Player class 

    def setUp(self): 
        # Create a fresh player before every test 
        self.player = Player("Anay") 

    # Initialization 

    def test_player_name(self): 
        # Player name should be stored correctly 
        self.assertEqual(self.player.name, "Anay")

    def test_initial_score(self): 
        # Player should start with zero score 
        self.assertEqual(self.player.score, 0)

    def test_initial_correct_guesses(self):
        self.assertEqual(self.player.correct_guesses, 0)

    def test_initial_wrong_guesses(self):
        self.assertEqual(self.player.wrong_guesses, 0)

    def test_initial_remaining_lives(self):
        self.assertGreater(self.player.remaining_lives, 0)

    # Score

    def test_add_score(self):
        self.player.add_score(150)
        self.assertEqual(self.player.score, 150)

    def test_multiple_score_additions(self):
        self.player.add_score(100)
        self.player.add_score(250)
        self.assertEqual(self.player.score, 350)

    def test_negative_score_not_allowed(self):
        old_score = self.player.score

        try:
            self.player.add_score(-50)
        except ValueError:
            pass

        self.assertGreaterEqual(self.player.score, 0)

    # Correct guesses

    def test_add_correct_guess(self):
        self.player.add_correct_guess()
        self.assertEqual(self.player.correct_guesses, 1)

    def test_multiple_correct_guesses(self):
        for _ in range(5):
            self.player.add_correct_guess()

        self.assertEqual(self.player.correct_guesses, 5)

    # Wrong guesses

    def test_add_wrong_guess(self):
        self.player.add_wrong_guess()
        self.assertEqual(self.player.wrong_guesses, 1)

    def test_multiple_wrong_guesses(self):
        for _ in range(7):
            self.player.add_wrong_guess()

        self.assertEqual(self.player.wrong_guesses, 7)

    # Lives

    def test_lose_life(self):
        starting = self.player.remaining_lives

        self.player.lose_life()

        self.assertEqual(
            self.player.remaining_lives,
            starting - 1
        )

    def test_lives_never_negative(self):
        for _ in range(100):
            self.player.lose_life()

        self.assertGreaterEqual(
            self.player.remaining_lives,
            0
        )

    # Accuracy

    def test_accuracy_no_guesses(self):
        self.assertEqual(
            self.player.calculate_accuracy(),
            0
        )

    def test_accuracy_half_correct(self):
        for _ in range(5):
            self.player.add_correct_guess()

        for _ in range(5):
            self.player.add_wrong_guess()

        self.assertEqual(
            self.player.calculate_accuracy(),
            50.0
        )

    def test_accuracy_all_correct(self):
        for _ in range(8):
            self.player.add_correct_guess()

        self.assertEqual(
            self.player.calculate_accuracy(),
            100.0
        )

    # Reset

    def test_reset_statistics(self):
        self.player.add_score(500)

        for _ in range(3):
            self.player.add_correct_guess()

        for _ in range(2):
            self.player.add_wrong_guess()

        self.player.reset_statistics()

        self.assertEqual(self.player.score, 0)
        self.assertEqual(self.player.correct_guesses, 0)
        self.assertEqual(self.player.wrong_guesses, 0)

    def test_reset_lives(self):
        self.player.lose_life()
        self.player.lose_life()

        self.player.reset_lives()

        self.assertEqual(
            self.player.remaining_lives,
            self.player.max_lives
        )

    # String Representation

    def test_string_representation(self):
        player_string = str(self.player)

        self.assertIn("Anay", player_string)

    # Edge Cases

    def test_large_score(self):
        self.player.add_score(1_000_000)

        self.assertEqual(
            self.player.score,
            1_000_000
        )

    def test_many_correct_guesses(self):
        for _ in range(100):
            self.player.add_correct_guess()

        self.assertEqual(
            self.player.correct_guesses,
            100
        )

    def test_many_wrong_guesses(self):
        for _ in range(100):
            self.player.add_wrong_guess()

        self.assertEqual(
            self.player.wrong_guesses,
            100
        )


if __name__ == "__main__":
    unittest.main() 