# test_statistics.py 
# Unit tests for statistics.py 

import unittest
from unittest.mock import patch
from game.statistics import Statistics
from utils.constants import DEFAULT_STATISTICS


class TestStatistics(unittest.TestCase):
    # Unit tests for the Statistics class 

    # Setup

    def setUp(self):
        """Create a fresh statistics object."""

        self.exists_patcher = patch(
            "utils.file_manager.FileManager.exists",
            return_value=False
        )

        self.save_patcher = patch(
            "utils.file_manager.FileManager.save_json"
        )

        self.load_patcher = patch(
            "utils.file_manager.FileManager.load_json",
            return_value=DEFAULT_STATISTICS.copy()
        )

        self.mock_exists = self.exists_patcher.start()
        self.mock_save = self.save_patcher.start()
        self.mock_load = self.load_patcher.start()

        self.stats = Statistics()

    def tearDown(self):
        """Stop all active patches."""

        patch.stopall()

    # Constructor

    def test_statistics_created(self):
        """Statistics object should be created."""

        self.assertIsInstance(
            self.stats,
            Statistics
        )

    def test_default_games_played(self):
        self.assertEqual(
            self.stats.games_played(),
            0
        )

    def test_default_games_won(self):
        self.assertEqual(
            self.stats.games_won(),
            0
        )

    def test_default_games_lost(self):
        self.assertEqual(
            self.stats.games_lost(),
            0
        )

    def test_default_total_score(self):
        self.assertEqual(
            self.stats.total_score(),
            0
        )

    def test_default_highest_score(self):
        self.assertEqual(
            self.stats.highest_score(),
            0
        )

    def test_default_words_completed(self):
        self.assertEqual(
            self.stats.words_completed(),
            0
        )

    # Loading

    def test_load_when_file_missing(self):
        """Missing statistics file should create one."""

        with patch(
            "utils.file_manager.FileManager.exists",
            return_value=False
        ):
            stats = Statistics()

            self.assertIsInstance(
                stats,
                Statistics
            )

    def test_load_existing_file(self):
        """Existing statistics should be loaded."""

        sample = DEFAULT_STATISTICS.copy()
        sample["games_played"] = 25

        with patch(
            "utils.file_manager.FileManager.exists",
            return_value=True
        ), patch(
            "utils.file_manager.FileManager.load_json",
            return_value=sample
        ):
            stats = Statistics()

            self.assertEqual(
                stats.games_played(),
                25
            )

    def test_load_invalid_data(self):
        """Invalid JSON should fall back to defaults."""

        with patch(
            "utils.file_manager.FileManager.exists",
            return_value=True
        ), patch(
            "utils.file_manager.FileManager.load_json",
            side_effect=Exception
        ):
            stats = Statistics()

            self.assertEqual(
                stats.games_played(),
                0
            )

    # Saving

    def test_save_calls_file_manager(self):
        """save() should write statistics."""

        with patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.stats.save()

            mocked.assert_called_once()

    # Reset

    def test_reset_statistics(self):
        """Reset should restore defaults."""

        self.stats.add_game_played()
        self.stats.add_game_won()
        self.stats.add_score(500)

        self.stats.reset()

        self.assertEqual(
            self.stats.games_played(),
            0
        )

        self.assertEqual(
            self.stats.games_won(),
            0
        )

        self.assertEqual(
            self.stats.highest_score(),
            0
        )

    # Getters

    def test_games_played_getter(self):
        self.stats.data["games_played"] = 17

        self.assertEqual(
            self.stats.games_played(),
            17
        )

    def test_games_won_getter(self):
        self.stats.data["games_won"] = 11

        self.assertEqual(
            self.stats.games_won(),
            11
        )

    def test_games_lost_getter(self):
        self.stats.data["games_lost"] = 6

        self.assertEqual(
            self.stats.games_lost(),
            6
        )

    def test_total_score_getter(self):
        self.stats.data["total_score"] = 4500

        self.assertEqual(
            self.stats.total_score(),
            4500
        )

    def test_highest_score_getter(self):
        self.stats.data["highest_score"] = 980

        self.assertEqual(
            self.stats.highest_score(),
            980
        )

    def test_fastest_game_getter(self):
        self.stats.data["fastest_game"] = 73.5

        self.assertEqual(
            self.stats.fastest_game(),
            73.5
        )

    def test_total_play_time_getter(self):
        self.stats.data["total_play_time"] = 850

        self.assertEqual(
            self.stats.total_play_time(),
            850
        )

    def test_longest_streak_getter(self):
        self.stats.data["longest_streak"] = 12

        self.assertEqual(
            self.stats.longest_streak(),
            12
        ) 

        # --------------------------------------------------
    # Increment Methods
    # --------------------------------------------------

    def test_add_game_played(self):
        self.stats.add_game_played()

        self.assertEqual(
            self.stats.games_played(),
            1
        )

    def test_add_game_won(self):
        self.stats.add_game_won()

        self.assertEqual(
            self.stats.games_won(),
            1
        )

    def test_add_game_lost(self):
        self.stats.add_game_lost()

        self.assertEqual(
            self.stats.games_lost(),
            1
        )

    def test_add_word_completed(self):
        self.stats.add_word_completed()

        self.assertEqual(
            self.stats.words_completed(),
            1
        )

    def test_add_letter_guess(self):
        self.stats.add_letter_guess()

        self.assertEqual(
            self.stats.total_letters_guessed(),
            1
        )

    def test_add_hint_used(self):
        self.stats.add_hint_used()

        self.assertEqual(
            self.stats.hints_used(),
            1
        )

    def test_add_play_time(self):
        self.stats.add_play_time(125.5)

        self.assertEqual(
            self.stats.total_play_time(),
            125.5
        )

    def test_add_score(self):
        self.stats.add_score(400)

        self.assertEqual(
            self.stats.total_score(),
            400
        )

    def test_highest_score_updated(self):
        self.stats.add_score(300)
        self.stats.add_score(900)

        self.assertEqual(
            self.stats.highest_score(),
            900
        )

    def test_highest_score_not_replaced(self):
        self.stats.add_score(900)
        self.stats.add_score(500)

        self.assertEqual(
            self.stats.highest_score(),
            900
        )

    # --------------------------------------------------
    # Record Functions
    # --------------------------------------------------

    def test_update_fastest_game_first_game(self):
        self.stats.update_fastest_game(120)

        self.assertEqual(
            self.stats.fastest_game(),
            120
        )

    def test_update_fastest_game_faster(self):
        self.stats.update_fastest_game(150)
        self.stats.update_fastest_game(90)

        self.assertEqual(
            self.stats.fastest_game(),
            90
        )

    def test_update_fastest_game_slower(self):
        self.stats.update_fastest_game(75)
        self.stats.update_fastest_game(140)

        self.assertEqual(
            self.stats.fastest_game(),
            75
        )

    def test_update_longest_streak(self):
        self.stats.update_longest_streak(12)

        self.assertEqual(
            self.stats.longest_streak(),
            12
        )

    def test_longest_streak_not_replaced(self):
        self.stats.update_longest_streak(15)
        self.stats.update_longest_streak(8)

        self.assertEqual(
            self.stats.longest_streak(),
            15
        )

    # --------------------------------------------------
    # Calculated Statistics
    # --------------------------------------------------

    def test_win_percentage_no_games(self):
        self.assertEqual(
            self.stats.win_percentage(),
            0.0
        )

    def test_win_percentage_half(self):
        self.stats.data["games_played"] = 10
        self.stats.data["games_won"] = 5

        self.assertEqual(
            self.stats.win_percentage(),
            50
        )

    def test_win_percentage_all_games(self):
        self.stats.data["games_played"] = 8
        self.stats.data["games_won"] = 8

        self.assertEqual(
            self.stats.win_percentage(),
            100
        )

    def test_average_score_no_games(self):
        self.assertEqual(
            self.stats.average_score(),
            0.0
        )

    def test_average_score(self):
        self.stats.data["games_played"] = 4
        self.stats.data["total_score"] = 1000

        self.assertEqual(
            self.stats.average_score(),
            250
        )

    def test_average_game_time(self):
        self.stats.data["games_played"] = 4
        self.stats.data["total_play_time"] = 600

        self.assertEqual(
            self.stats.average_game_time(),
            150.0
        )

    def test_average_letters_per_game(self):
        self.stats.data["games_played"] = 5
        self.stats.data["letters_guessed"] = 60

        self.assertEqual(
            self.stats.average_letters_per_game(),
            12.0
        ) 

        # --------------------------------------------------
    # Difficulty Statistics
    # --------------------------------------------------

    def test_add_difficulty_game(self):
        self.stats.add_difficulty_game("Easy")

        self.assertEqual(
            self.stats.data["difficulty_stats"]["Easy"]["played"],
            1
        )

    def test_add_difficulty_win(self):
        self.stats.add_difficulty_win("Hard")

        self.assertEqual(
            self.stats.data["difficulty_stats"]["Hard"]["won"],
            1
        )

    def test_add_difficulty_loss(self):
        self.stats.add_difficulty_loss("Medium")

        self.assertEqual(
            self.stats.data["difficulty_stats"]["Medium"]["lost"],
            1
        )

    def test_new_difficulty_created(self):
        self.stats.add_difficulty_game("Custom")

        self.assertIn(
            "Custom",
            self.stats.data["difficulty_stats"]
        )

    # --------------------------------------------------
    # Game Mode Statistics
    # --------------------------------------------------

    def test_add_game_mode(self):
        self.stats.add_game_mode("Classic")

        self.assertEqual(
            self.stats.data["mode_stats"]["Classic"]["played"],
            1
        )

    def test_add_mode_win(self):
        self.stats.add_mode_win("Timed")

        self.assertEqual(
            self.stats.data["mode_stats"]["Timed"]["won"],
            1
        )

    def test_add_mode_loss(self):
        self.stats.add_mode_loss("Survival")

        self.assertEqual(
            self.stats.data["mode_stats"]["Survival"]["lost"],
            1
        )

    def test_new_game_mode_created(self):
        self.stats.add_game_mode("Challenge")

        self.assertIn(
            "Challenge",
            self.stats.data["mode_stats"]
        )

    # --------------------------------------------------
    # Complete Game Recording
    # --------------------------------------------------

    def test_record_completed_game_win(self):
        self.stats.record_completed_game(
            won=True,
            score=850,
            streak=6,
            play_time=120,
            letters_guessed=15,
            hints_used=1,
            difficulty="Easy",
            mode="Classic"
        )

        self.assertEqual(
            self.stats.games_played(),
            1
        )

        self.assertEqual(
            self.stats.games_won(),
            1
        )

        self.assertEqual(
            self.stats.highest_score(),
            850
        )

    def test_record_completed_game_loss(self):
        self.stats.record_completed_game(
            won=False,
            score=250,
            streak=2,
            play_time=240,
            letters_guessed=20,
            hints_used=3,
            difficulty="Hard",
            mode="Timed"
        )

        self.assertEqual(
            self.stats.games_played(),
            1
        )

        self.assertEqual(
            self.stats.games_lost(),
            1
        )

    def test_record_updates_total_score(self):
        self.stats.record_completed_game(
            won=True,
            score=1000,
            streak=5,
            play_time=90,
            letters_guessed=12,
            hints_used=0,
            difficulty="Easy",
            mode="Classic"
        )

        self.assertEqual(
            self.stats.total_score(),
            1000
        )

    def test_record_updates_play_time(self):
        self.stats.record_completed_game(
            won=True,
            score=500,
            streak=4,
            play_time=200,
            letters_guessed=18,
            hints_used=2,
            difficulty="Medium",
            mode="Timed"
        )

        self.assertEqual(
            self.stats.total_play_time(),
            200
        )

    def test_record_updates_longest_streak(self):
        self.stats.record_completed_game(
            won=True,
            score=400,
            streak=11,
            play_time=150,
            letters_guessed=14,
            hints_used=0,
            difficulty="Easy",
            mode="Classic"
        )

        self.assertEqual(
            self.stats.longest_streak(),
            11
        )

    def test_record_updates_fastest_game(self):
        self.stats.record_completed_game(
            won=True,
            score=600,
            streak=5,
            play_time=70,
            letters_guessed=10,
            hints_used=0,
            difficulty="Easy",
            mode="Classic"
        )

        self.assertEqual(
            self.stats.fastest_game(),
            70
        )

    def test_record_adds_word_completed(self):
        self.stats.record_completed_game(
            won=True,
            score=500,
            streak=2,
            play_time=100,
            letters_guessed=15,
            hints_used=1,
            difficulty="Medium",
            mode="Classic"
        )

        self.assertEqual(
            self.stats.words_completed(),
            1
        ) 

        # --------------------------------------------------
    # Report Generation
    # --------------------------------------------------

    def test_generate_report_returns_list(self):
        report = self.stats.generate_report()

        self.assertIsInstance(
            report,
            list
        )

    def test_generate_report_not_empty(self):
        report = self.stats.generate_report()

        self.assertGreater(
            len(report),
            0
        )

    def test_generate_report_contains_heading(self):
        report = self.stats.generate_report()

        self.assertIn(
            "LIFETIME STATISTICS",
            report
        )

    def test_generate_report_contains_games_played(self):
        report = self.stats.generate_report()

        found = any(
            "Games Played" in line
            for line in report
        )

        self.assertTrue(found)

    # --------------------------------------------------
    # Time Formatting
    # --------------------------------------------------

    def test_format_time_zero(self):
        self.assertEqual(
            Statistics.format_time(0),
            "00:00:00"
        )

    def test_format_time_seconds(self):
        self.assertEqual(
            Statistics.format_time(59),
            "00:00:59"
        )

    def test_format_time_minutes(self):
        self.assertEqual(
            Statistics.format_time(125),
            "00:02:05"
        )

    def test_format_time_hours(self):
        self.assertEqual(
            Statistics.format_time(3661),
            "01:01:01"
        )

    # --------------------------------------------------
    # Print Statistics
    # --------------------------------------------------

    @patch("builtins.print")
    def test_print_statistics(self, mocked_print):
        self.stats.print_statistics()

        self.assertGreater(
            mocked_print.call_count,
            0
        )

    # --------------------------------------------------
    # Serialization
    # --------------------------------------------------

    def test_to_dict_returns_dictionary(self):
        data = self.stats.to_dict()

        self.assertIsInstance(
            data,
            dict
        )

    def test_from_dict(self):
        new_data = DEFAULT_STATISTICS.copy()
        new_data["games_played"] = 25
        new_data["games_won"] = 18

        self.stats.from_dict(new_data)

        self.assertEqual(
            self.stats.games_played(),
            25
        )

        self.assertEqual(
            self.stats.games_won(),
            18
        )

    def test_from_dict_invalid(self):
        self.stats.from_dict("invalid")

        self.assertEqual(
            self.stats.games_played(),
            0
        )

    # --------------------------------------------------
    # Utility Methods
    # --------------------------------------------------

    def test_clear(self):
        self.stats.add_game_played()

        self.stats.clear()

        self.assertEqual(
            self.stats.games_played(),
            0
        )

    @patch.object(Statistics, "load")
    def test_reload(self, mocked_load):
        self.stats.reload()

        mocked_load.assert_called_once()

    # --------------------------------------------------
    # String Representation
    # --------------------------------------------------

    def test_string_representation(self):
        text = str(self.stats)

        self.assertIn(
            "Statistics",
            text
        )

    def test_repr(self):
        text = repr(self.stats)

        self.assertEqual(
            text,
            str(self.stats)
        )

    # --------------------------------------------------
    # Edge Cases
    # --------------------------------------------------

    def test_large_score(self):
        self.stats.add_score(1_000_000)

        self.assertEqual(
            self.stats.highest_score(),
            1_000_000
        )

    def test_large_play_time(self):
        self.stats.add_play_time(100000)

        self.assertEqual(
            self.stats.total_play_time(),
            100000
        )

    def test_zero_score(self):
        self.stats.add_score(0)

        self.assertEqual(
            self.stats.total_score(),
            0
        )

    def test_zero_play_time(self):
        self.stats.add_play_time(0)

        self.assertEqual(
            self.stats.total_play_time(),
            0
        )

    def test_multiple_games(self):
        for _ in range(10):
            self.stats.add_game_played()

        self.assertEqual(
            self.stats.games_played(),
            10
        )

    def test_multiple_wins(self):
        for _ in range(7):
            self.stats.add_game_won()

        self.assertEqual(
            self.stats.games_won(),
            7
        )

    def test_multiple_losses(self):
        for _ in range(4):
            self.stats.add_game_lost()

        self.assertEqual(
            self.stats.games_lost(),
            4
        )


if __name__ == "__main__":
    unittest.main()