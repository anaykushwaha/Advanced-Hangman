# test_statistics.py
# Unit tests for statistics.py

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock 

from game.statistics import Statistics
from utils.constants import DEFAULT_STATISTICS


class TestStatistics(unittest.TestCase):
    # Unit tests for the Statistics class

    def setUp(self):
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

        self.statistics = Statistics()

    def tearDown(self):
        patch.stopall()

    # Constructor

    def test_statistics_created(self):
        self.assertIsInstance(
            self.statistics,
            Statistics
        )

    def test_default_games_played(self):
        self.assertEqual(
            self.statistics.games_played(),
            0
        )

    def test_default_games_won(self):
        self.assertEqual(
            self.statistics.games_won(),
            0
        )

    def test_default_games_lost(self):
        self.assertEqual(
            self.statistics.games_lost(),
            0
        )

    def test_default_total_score(self):
        self.assertEqual(
            self.statistics.total_score(),
            0
        )

    def test_default_highest_score(self):
        self.assertEqual(
            self.statistics.highest_score(),
            0
        )

    def test_default_words_completed(self):
        self.assertEqual(
            self.statistics.words_completed(),
            0
        )

    def test_default_letters_guessed(self):
        self.assertEqual(
            self.statistics.total_letters_guessed(),
            0
        )

    def test_default_hints_used(self):
        self.assertEqual(
            self.statistics.hints_used(),
            0
        )

    def test_default_fastest_game(self):
        self.assertEqual(
            self.statistics.fastest_game(),
            0
        )

    def test_default_total_play_time(self):
        self.assertEqual(
            self.statistics.total_play_time(),
            0
        )

    def test_default_longest_streak(self):
        self.assertEqual(
            self.statistics.longest_streak(),
            0
        )

    # Loading

    def test_load_when_file_missing(self):
        with patch(
            "utils.file_manager.FileManager.exists",
            return_value=False
        ):
            statistics = Statistics()

            self.assertIsInstance(
                statistics,
                Statistics
            )

    def test_load_existing_file(self):
        sample = DEFAULT_STATISTICS.copy()
        sample["games_played"] = 25
        sample["games_won"] = 18

        with patch(
            "utils.file_manager.FileManager.exists",
            return_value=True
        ), patch(
            "utils.file_manager.FileManager.load_json",
            return_value=sample
        ):
            statistics = Statistics()

            self.assertEqual(
                statistics.games_played(),
                25
            )

            self.assertEqual(
                statistics.games_won(),
                18
            )

    def test_load_invalid_data(self):
        with patch(
            "utils.file_manager.FileManager.exists",
            return_value=True
        ), patch(
            "utils.file_manager.FileManager.load_json",
            side_effect=Exception
        ):
            statistics = Statistics()

            self.assertEqual(
                statistics.games_played(),
                0
            )

    # Saving

    def test_save_calls_file_manager(self):
        with patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.statistics.save()

            mocked.assert_called_once()

    # Reset

    def test_reset_statistics(self):
        self.statistics.add_game_played()
        self.statistics.add_game_won()
        self.statistics.add_score(500)

        self.statistics.reset()

        self.assertEqual(
            self.statistics.games_played(),
            0
        )

        self.assertEqual(
            self.statistics.games_won(),
            0
        )

        self.assertEqual(
            self.statistics.highest_score(),
            0
        )

        self.assertEqual(
            self.statistics.total_score(),
            0
        )

    # Getter Methods

    def test_games_played_getter(self):
        self.statistics.data["games_played"] = 17

        self.assertEqual(
            self.statistics.games_played(),
            17
        )

    def test_games_won_getter(self):
        self.statistics.data["games_won"] = 11

        self.assertEqual(
            self.statistics.games_won(),
            11
        )

    def test_games_lost_getter(self):
        self.statistics.data["games_lost"] = 6

        self.assertEqual(
            self.statistics.games_lost(),
            6
        )

    def test_total_score_getter(self):
        self.statistics.data["total_score"] = 4500

        self.assertEqual(
            self.statistics.total_score(),
            4500
        )

    def test_highest_score_getter(self):
        self.statistics.data["highest_score"] = 980

        self.assertEqual(
            self.statistics.highest_score(),
            980
        )

    def test_fastest_game_getter(self):
        self.statistics.data["fastest_game"] = 73.5

        self.assertEqual(
            self.statistics.fastest_game(),
            73.5
        )

    def test_total_play_time_getter(self):
        self.statistics.data["total_play_time"] = 850

        self.assertEqual(
            self.statistics.total_play_time(),
            850
        )

    def test_longest_streak_getter(self):
        self.statistics.data["longest_streak"] = 12

        self.assertEqual(
            self.statistics.longest_streak(),
            12
        ) 

        # Increment Methods

    def test_add_game_played(self):
        self.statistics.add_game_played()

        self.assertEqual(
            self.statistics.games_played(),
            1
        )

    def test_add_game_won(self):
        self.statistics.add_game_won()

        self.assertEqual(
            self.statistics.games_won(),
            1
        )

    def test_add_game_lost(self):
        self.statistics.add_game_lost()

        self.assertEqual(
            self.statistics.games_lost(),
            1
        )

    def test_add_word_completed(self):
        self.statistics.add_word_completed()

        self.assertEqual(
            self.statistics.words_completed(),
            1
        )

    def test_add_letter_guess(self):
        self.statistics.add_letter_guess()

        self.assertEqual(
            self.statistics.total_letters_guessed(),
            1
        )

    def test_add_hint_used(self):
        self.statistics.add_hint_used()

        self.assertEqual(
            self.statistics.hints_used(),
            1
        )

    def test_add_play_time(self):
        self.statistics.add_play_time(125.5)

        self.assertEqual(
            self.statistics.total_play_time(),
            125.5
        )

    def test_add_score(self):
        self.statistics.add_score(400)

        self.assertEqual(
            self.statistics.total_score(),
            400
        )

    def test_highest_score_updated(self):
        self.statistics.add_score(300)
        self.statistics.add_score(900)

        self.assertEqual(
            self.statistics.highest_score(),
            900
        )

    def test_highest_score_not_replaced(self):
        self.statistics.add_score(900)
        self.statistics.add_score(500)

        self.assertEqual(
            self.statistics.highest_score(),
            900
        )

    # Record Methods

    def test_update_fastest_game_first_game(self):
        self.statistics.update_fastest_game(120)

        self.assertEqual(
            self.statistics.fastest_game(),
            120
        )

    def test_update_fastest_game_faster(self):
        self.statistics.update_fastest_game(150)
        self.statistics.update_fastest_game(90)

        self.assertEqual(
            self.statistics.fastest_game(),
            90
        )

    def test_update_fastest_game_slower(self):
        self.statistics.update_fastest_game(75)
        self.statistics.update_fastest_game(140)

        self.assertEqual(
            self.statistics.fastest_game(),
            75
        )

    def test_update_longest_streak(self):
        self.statistics.update_longest_streak(12)

        self.assertEqual(
            self.statistics.longest_streak(),
            12
        )

    def test_longest_streak_not_replaced(self):
        self.statistics.update_longest_streak(15)
        self.statistics.update_longest_streak(8)

        self.assertEqual(
            self.statistics.longest_streak(),
            15
        )

    # Calculated Statistics

    def test_win_percentage_no_games(self):
        self.assertEqual(
            self.statistics.win_percentage(),
            0.0
        )

    def test_win_percentage_half(self):
        self.statistics.data["games_played"] = 10
        self.statistics.data["games_won"] = 5

        self.assertEqual(
            self.statistics.win_percentage(),
            50
        )

    def test_win_percentage_all_games(self):
        self.statistics.data["games_played"] = 8
        self.statistics.data["games_won"] = 8

        self.assertEqual(
            self.statistics.win_percentage(),
            100
        )

    def test_average_score_no_games(self):
        self.assertEqual(
            self.statistics.average_score(),
            0.0
        )

    def test_average_score(self):
        self.statistics.data["games_played"] = 4
        self.statistics.data["total_score"] = 1000

        self.assertEqual(
            self.statistics.average_score(),
            250
        )

    def test_average_game_time(self):
        self.statistics.data["games_played"] = 4
        self.statistics.data["total_play_time"] = 600

        self.assertEqual(
            self.statistics.average_game_time(),
            150.0
        )

    def test_average_letters_per_game(self):
        self.statistics.data["games_played"] = 5
        self.statistics.data["letters_guessed"] = 60

        self.assertEqual(
            self.statistics.average_letters_per_game(),
            12.0
        ) 

        # Difficulty Statistics

    def test_add_difficulty_game(self):
        self.statistics.add_difficulty_game("Easy")

        self.assertEqual(
            self.statistics.data["difficulty_stats"]["Easy"]["played"],
            1
        )

    def test_add_difficulty_win(self):
        self.statistics.add_difficulty_win("Hard")

        self.assertEqual(
            self.statistics.data["difficulty_stats"]["Hard"]["won"],
            1
        )

    def test_add_difficulty_loss(self):
        self.statistics.add_difficulty_loss("Medium")

        self.assertEqual(
            self.statistics.data["difficulty_stats"]["Medium"]["lost"],
            1
        )

    def test_new_difficulty_created(self):
        self.statistics.add_difficulty_game("Impossible")

        self.assertIn(
            "Impossible",
            self.statistics.data["difficulty_stats"]
        )

        # Game Mode Statistics

    def test_add_game_mode(self):
        self.statistics.add_game_mode("Classic")

        self.assertEqual(
            self.statistics.data["mode_stats"]["Classic"]["played"],
            1
        )

    def test_add_mode_win(self):
        self.statistics.add_mode_win("Timed")

        self.assertEqual(
            self.statistics.data["mode_stats"]["Timed"]["won"],
            1
        )

    def test_add_mode_loss(self):
        self.statistics.add_mode_loss("Endless")

        self.assertEqual(
            self.statistics.data["mode_stats"]["Endless"]["lost"],
            1
        )

    def test_new_mode_created(self):
        self.statistics.add_game_mode("Daily Challenge")

        self.assertIn(
            "Daily Challenge",
            self.statistics.data["mode_stats"]
        )

        # Complete Game Recording

    def test_record_completed_game_win(self):
        self.statistics.record_completed_game(
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
            self.statistics.games_played(),
            1
        )

        self.assertEqual(
            self.statistics.games_won(),
            1
        )

        self.assertEqual(
            self.statistics.highest_score(),
            850
        )

        self.assertEqual(
            self.statistics.games_played(),
            1
        )

        self.assertEqual(
            self.statistics.games_won(),
            1
        )

        self.assertEqual(
            self.statistics.highest_score(),
            850
        ) 

    def test_record_completed_game_loss(self):
        self.statistics.record_completed_game(
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
            self.statistics.games_played(),
            1
        )

        self.assertEqual(
            self.statistics.games_lost(),
            1
        )

    def test_record_updates_total_score(self):
        self.statistics.record_completed_game(
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
            self.statistics.total_score(),
            1000
        )

    def test_record_updates_play_time(self):
        self.statistics.record_completed_game(
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
            self.statistics.total_play_time(),
            200
        )

    def test_record_updates_longest_streak(self):
        self.statistics.record_completed_game(
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
            self.statistics.longest_streak(),
            11
        )

    def test_record_updates_fastest_game(self):
        self.statistics.record_completed_game(
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
            self.statistics.fastest_game(),
            70
        )

    def test_record_updates_letters_guessed(self):
        self.statistics.record_completed_game(
            won=True,
            score=600,
            streak=5,
            play_time=70,
            letters_guessed=18,
            hints_used=0,
            difficulty="Easy",
            mode="Classic"
        )

        self.assertEqual(
            self.statistics.total_letters_guessed(),
            18
        )

    def test_record_updates_hints_used(self):
        self.statistics.record_completed_game(
            won=True,
            score=600,
            streak=5,
            play_time=70,
            letters_guessed=10,
            hints_used=4,
            difficulty="Easy",
            mode="Classic"
        )

        self.assertEqual(
            self.statistics.hints_used(),
            4
        )

    def test_record_adds_word_completed(self):
        self.statistics.record_completed_game(
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
            self.statistics.words_completed(),
            1
        )
    
    # Report Generation

    def test_generate_report_returns_list(self):
        report = self.statistics.generate_report()

        self.assertIsInstance(
            report,
            list
        )

    def test_generate_report_not_empty(self):
        report = self.statistics.generate_report()

        self.assertGreater(
            len(report),
            0
        )

    def test_generate_report_contains_heading(self):
        report = self.statistics.generate_report()

        self.assertIn(
            "LIFETIME STATISTICS",
            report
        )

    def test_generate_report_contains_games_played(self):
        report = self.statistics.generate_report()

        found = any(
            "Games Played" in line
            for line in report
        )

        self.assertTrue(found)

    # Time Formatting

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

    # Print Statistics

    @patch("builtins.print")
    def test_print_statistics(self, mocked_print):
        self.statistics.print_statistics()

        self.assertGreater(
            mocked_print.call_count,
            0
        )

    # Serialization

    def test_to_dict_returns_dictionary(self):
        data = self.statistics.to_dict()

        self.assertIsInstance(
            data,
            dict
        )

    def test_from_dict(self):
        new_data = DEFAULT_STATISTICS.copy()
        new_data["games_played"] = 25
        new_data["games_won"] = 18

        self.statistics.from_dict(new_data)

        self.assertEqual(
            self.statistics.games_played(),
            25
        )

        self.assertEqual(
            self.statistics.games_won(),
            18
        )

    def test_from_dict_invalid(self):
        self.statistics.from_dict("invalid")

        self.assertEqual(
            self.statistics.games_played(),
            0
        )

    # Utility Methods

    def test_clear(self):
        self.statistics.add_game_played()

        self.statistics.clear()

        self.assertEqual(
            self.statistics.games_played(),
            0
        )

    @patch.object(Statistics, "load")
    def test_reload(self, mocked_load):
        self.statistics.reload()

        mocked_load.assert_called_once()

    @patch.object(Statistics, "save") 
    def test_record_completed_game_calls_save(
        self,
        mocked_save
    ):
        self.statistics.record_completed_game(
            won=True,
            score=100,
            streak=1,
            play_time=60,
            letters_guessed=5,
            hints_used=0,
            difficulty="Easy",
            mode="Classic"
        )

        self.assertEqual(
            mocked_save.call_count,
            1
        )

    # String Representation

    def test_string_representation(self):
        text = str(self.statistics)

        self.assertIn(
            "Statistics",
            text
        )

    def test_repr(self):
        text = repr(self.statistics)

        self.assertEqual(
            text,
            str(self.statistics)
        )

    # Edge Cases

    def test_large_score(self):
        self.statistics.add_score(1_000_000)

        self.assertEqual(
            self.statistics.highest_score(),
            1_000_000
        )

    def test_large_play_time(self):
        self.statistics.add_play_time(100000)

        self.assertEqual(
            self.statistics.total_play_time(),
            100000
        )

    def test_zero_score(self):
        self.statistics.add_score(0)

        self.assertEqual(
            self.statistics.total_score(),
            0
        )

    def test_zero_play_time(self):
        self.statistics.add_play_time(0)

        self.assertEqual(
            self.statistics.total_play_time(),
            0
        )

    def test_multiple_games(self):
        for _ in range(10):
            self.statistics.add_game_played()

        self.assertEqual(
            self.statistics.games_played(),
            10
        )

    def test_multiple_wins(self):
        for _ in range(7):
            self.statistics.add_game_won()

        self.assertEqual(
            self.statistics.games_won(),
            7
        )

    def test_multiple_losses(self):
        for _ in range(4):
            self.statistics.add_game_lost()

        self.assertEqual(
            self.statistics.games_lost(),
            4
        )


if __name__ == "__main__":
    unittest.main() 