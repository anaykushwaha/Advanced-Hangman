# test_scoreboard.py 
# Unit tests for scoreboard.py 

import unittest
from game.player import Player
from game.scoreboard import ScoreBoard
from game.difficulty import DifficultyManager

from utils.constants import (
    POINTS_CORRECT_GUESS,
    POINTS_GAME_WON,
    POINTS_WORD_COMPLETED,
    POINTS_FAST_FINISH,
    POINTS_PER_UNUSED_LIFE,
    POINTS_WRONG_GUESS,
    POINTS_DUPLICATE_GUESS,
    FAST_FINISH_TIME,
    COMBO_START,
    COMBO_BONUS,
)


class TestScoreBoard(unittest.TestCase): 
    # Units tests for ScoreBoard 
    def setUp(self):
        self.player = Player("Tester")

    # Difficulty Multiplier

    def test_multiplier_positive(self):
        self.assertGreater(
            ScoreBoard.multiplier(),
            0
        )

    def test_scaled_returns_integer(self):
        value = ScoreBoard.scaled(100)

        self.assertIsInstance(value, int)

    # Correct Guess

    def test_correct_guess_returns_integer(self):
        score = ScoreBoard.correct_guess(self.player)

        self.assertIsInstance(score, int)

    def test_correct_guess_positive(self):
        score = ScoreBoard.correct_guess(self.player)

        self.assertGreater(score, 0)

    def test_combo_bonus_applied(self):
        self.player.current_streak = COMBO_START

        combo_score = ScoreBoard.correct_guess(self.player)

        expected = ScoreBoard.scaled(
            POINTS_CORRECT_GUESS +
            COMBO_START * COMBO_BONUS
        )

        self.assertEqual(combo_score, expected)

    def test_large_combo_bonus(self):
        self.player.current_streak = 100

        score = ScoreBoard.correct_guess(self.player)

        self.assertGreater(score, 0)

    # Wrong Guess

    def test_wrong_guess_penalty(self):
        self.assertEqual(
            ScoreBoard.wrong_guess(),
            POINTS_WRONG_GUESS
        )

    # Duplicate Guess

    def test_duplicate_guess_penalty(self):
        self.assertEqual(
            ScoreBoard.duplicate_guess(),
            POINTS_DUPLICATE_GUESS
        )

    # Hint

    def test_hint_penalty_negative(self):
        penalty = ScoreBoard.hint_used()

        self.assertLess(penalty, 0)

    # Word Completion

    def test_word_completed_bonus(self):
        score = ScoreBoard.word_completed()

        expected = ScoreBoard.scaled(
            POINTS_WORD_COMPLETED
        )

        self.assertEqual(score, expected)

    # Win Bonus

    def test_game_won_bonus(self):
        self.player.lives_remaining = 5

        expected = ScoreBoard.scaled(
            POINTS_GAME_WON +
            5 * POINTS_PER_UNUSED_LIFE
        )

        self.assertEqual(
            ScoreBoard.game_won(self.player),
            expected
        )

    def test_game_won_positive(self):
        score = ScoreBoard.game_won(self.player)

        self.assertGreater(score, 0)

    # Fast Finish

    def test_fast_finish_bonus(self):
        score = ScoreBoard.fast_finish(
            FAST_FINISH_TIME
        )

        self.assertEqual(
            score,
            ScoreBoard.scaled(
                POINTS_FAST_FINISH
            )
        )

    def test_fast_finish_after_limit(self):
        score = ScoreBoard.fast_finish(
            FAST_FINISH_TIME + 1
        )

        self.assertEqual(score, 0)

    # Final Score

    def test_calculate_final_score(self):
        self.player.lives_remaining = 3

        score = ScoreBoard.calculate_final_score(
            self.player,
            FAST_FINISH_TIME
        )

        self.assertGreater(score, 0)

    def test_calculate_final_score_slow(self):
        score = ScoreBoard.calculate_final_score(
            self.player,
            FAST_FINISH_TIME + 100
        )

        self.assertGreater(score, 0)

    # Formatting

    def test_score_formatting(self):
        formatted = ScoreBoard.format(15420)

        self.assertEqual(
            formatted,
            "15,420"
        )

    def test_zero_formatting(self):
        self.assertEqual(
            ScoreBoard.format(0),
            "0"
        )

    def test_large_number_formatting(self):
        formatted = ScoreBoard.format(
            123456789
        )

        self.assertEqual(
            formatted,
            "123,456,789"
        )

    # Edge Cases

    def test_scaled_zero(self):
        self.assertEqual(
            ScoreBoard.scaled(0),
            0
        )

    def test_scaled_negative(self):
        value = ScoreBoard.scaled(-100)

        self.assertLessEqual(value, 0)

    def test_correct_guess_no_combo(self):
        self.player.current_streak = 0

        expected = ScoreBoard.scaled(
            POINTS_CORRECT_GUESS
        )

        self.assertEqual(
            ScoreBoard.correct_guess(self.player),
            expected
        )

    def test_fast_finish_exact_boundary(self):
        score = ScoreBoard.fast_finish(
            FAST_FINISH_TIME
        )

        self.assertGreater(score, 0)

    def test_fast_finish_far_after_limit(self):
        score = ScoreBoard.fast_finish(
            99999
        )

        self.assertEqual(score, 0)


if __name__ == "__main__":
    unittest.main() 