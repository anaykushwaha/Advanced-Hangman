# test_scoreboard.py
# Unit tests for scoreboard.py

import unittest

from game.player import Player
from game.scoreboard import ScoreBoard

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
    MAX_COMBO_MULTIPLIER,
)


class TestScoreBoard(unittest.TestCase):
    # Unit tests for ScoreBoard 

    def setUp(self):
        self.player = Player("Tester")

    # Difficulty multiplier

    def test_multiplier_positive(self):
        self.assertGreater(
            ScoreBoard.multiplier(),
            0
        )

    def test_scaled_returns_integer(self):
        value = ScoreBoard.scaled(100)

        self.assertIsInstance(
            value,
            int
        )

    def test_scaled_zero(self):
        self.assertEqual(
            ScoreBoard.scaled(0),
            0
        )

    def test_scaled_negative(self):
        self.assertLessEqual(
            ScoreBoard.scaled(-100),
            0
        )

    # Correct guesses

    def test_correct_guess_returns_integer(self):
        score = ScoreBoard.correct_guess(self.player)

        self.assertIsInstance(
            score,
            int
        )

    def test_correct_guess_positive(self):
        score = ScoreBoard.correct_guess(self.player)

        self.assertGreater(
            score,
            0
        )

    def test_correct_guess_no_combo(self):
        self.player.current_streak = 0

        expected = ScoreBoard.scaled(
            POINTS_CORRECT_GUESS
        )

        self.assertEqual(
            ScoreBoard.correct_guess(self.player),
            expected
        )

    def test_combo_bonus_applied(self):
        self.player.current_streak = COMBO_START

        expected = ScoreBoard.scaled(
            POINTS_CORRECT_GUESS
            + COMBO_START * COMBO_BONUS
        )

        self.assertEqual(
            ScoreBoard.correct_guess(self.player),
            expected
        )

    def test_combo_bonus_is_capped(self):
        self.player.current_streak = 999

        expected = ScoreBoard.scaled(
            POINTS_CORRECT_GUESS
            + MAX_COMBO_MULTIPLIER * COMBO_BONUS
        )

        self.assertEqual(
            ScoreBoard.correct_guess(self.player),
            expected
        )

    # Wrong / duplicate guesses

    def test_wrong_guess_penalty(self):
        self.assertEqual(
            ScoreBoard.wrong_guess(),
            POINTS_WRONG_GUESS
        )

    def test_duplicate_guess_penalty(self):
        self.assertEqual(
            ScoreBoard.duplicate_guess(),
            POINTS_DUPLICATE_GUESS
        )

    # Hint penalty

    def test_hint_penalty_negative(self):
        self.assertLess(
            ScoreBoard.hint_used(),
            0
        )

    # Word completion

    def test_word_completed_bonus(self):
        expected = ScoreBoard.scaled(
            POINTS_WORD_COMPLETED
        )

        self.assertEqual(
            ScoreBoard.word_completed(),
            expected
        )

    # Win bonus

    def test_game_won_bonus(self):
        self.player.lives_remaining = 5

        expected = ScoreBoard.scaled(
            POINTS_GAME_WON
            + 5 * POINTS_PER_UNUSED_LIFE
        )

        self.assertEqual(
            ScoreBoard.game_won(self.player),
            expected
        )

    def test_game_won_positive(self):
        score = ScoreBoard.game_won(self.player)

        self.assertGreater(
            score,
            0
        )

    # Fast finish

    def test_fast_finish_bonus(self):
        expected = ScoreBoard.scaled(
            POINTS_FAST_FINISH
        )

        self.assertEqual(
            ScoreBoard.fast_finish(
                FAST_FINISH_TIME
            ),
            expected
        )

    def test_fast_finish_exact_boundary(self):
        self.assertGreater(
            ScoreBoard.fast_finish(
                FAST_FINISH_TIME
            ),
            0
        )

    def test_fast_finish_after_limit(self):
        self.assertEqual(
            ScoreBoard.fast_finish(
                FAST_FINISH_TIME + 1
            ),
            0
        )

    def test_fast_finish_far_after_limit(self):
        self.assertEqual(
            ScoreBoard.fast_finish(
                99999
            ),
            0
        )

    # Final score

    def test_calculate_final_score(self):
        self.player.lives_remaining = 3

        score = ScoreBoard.calculate_final_score(
            self.player,
            FAST_FINISH_TIME
        )

        self.assertGreater(
            score,
            0
        )

    def test_calculate_final_score_without_fast_bonus(self):
        score = ScoreBoard.calculate_final_score(
            self.player,
            FAST_FINISH_TIME + 100
        )

        self.assertGreater(
            score,
            0
        )

    # Formatting

    def test_score_formatting(self):
        self.assertEqual(
            ScoreBoard.format(15420),
            "15,420"
        )

    def test_zero_formatting(self):
        self.assertEqual(
            ScoreBoard.format(0),
            "0"
        )

    def test_large_number_formatting(self):
        self.assertEqual(
            ScoreBoard.format(123456789),
            "123,456,789"
        )

    # Preview

    def test_preview_runs(self):
        # Simply verify that preview executes without errors.
        ScoreBoard.preview(self.player)


if __name__ == "__main__":
    unittest.main() 

