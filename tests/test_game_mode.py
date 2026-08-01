# test_game_mode.py
# Unit tests for game_mode.py

import unittest
from unittest.mock import patch

from game.game_mode import (
    GameMode,
    GameModeManager,
    GameModeSettings,
)


class TestGameMode(unittest.TestCase):
    # Unit tests for the GameModeManager class

    def setUp(self):
        GameModeManager.reset()

    # Enum Tests

    def test_classic_enum(self):
        self.assertEqual(
            GameMode.CLASSIC.value,
            "Classic"
        )

    def test_timed_enum(self):
        self.assertEqual(
            GameMode.TIMED.value,
            "Timed"
        )

    def test_endless_enum(self):
        self.assertEqual(
            GameMode.ENDLESS.value,
            "Endless"
        )

    def test_daily_enum(self):
        self.assertEqual(
            GameMode.DAILY.value,
            "Daily Challenge"
        )

    # Default Mode

    def test_default_mode(self):
        self.assertEqual(
            GameModeManager.get_current(),
            GameMode.CLASSIC
        )

    def test_get_settings_returns_settings(self):
        settings = GameModeManager.get_settings()

        self.assertIsInstance(
            settings,
            GameModeSettings
        )

    def test_default_name(self):
        self.assertEqual(
            GameModeManager.get_settings().name,
            "Classic"
        )

    # set_mode()

    def test_set_classic(self):
        GameModeManager.set_mode(
            GameMode.CLASSIC
        )

        self.assertEqual(
            GameModeManager.get_current(),
            GameMode.CLASSIC
        )

    def test_set_timed(self):
        GameModeManager.set_mode(
            GameMode.TIMED
        )

        self.assertEqual(
            GameModeManager.get_current(),
            GameMode.TIMED
        )

    def test_set_endless(self):
        GameModeManager.set_mode(
            GameMode.ENDLESS
        )

        self.assertEqual(
            GameModeManager.get_current(),
            GameMode.ENDLESS
        )

    def test_set_daily(self):
        GameModeManager.set_mode(
            GameMode.DAILY
        )

        self.assertEqual(
            GameModeManager.get_current(),
            GameMode.DAILY
        )

    # get()

    def test_get_classic(self):
        settings = GameModeManager.get(
            GameMode.CLASSIC
        )

        self.assertEqual(
            settings.name,
            "Classic"
        )

    def test_get_timed(self):
        settings = GameModeManager.get(
            GameMode.TIMED
        )

        self.assertTrue(
            settings.timed
        )

    def test_get_endless(self):
        settings = GameModeManager.get(
            GameMode.ENDLESS
        )

        self.assertTrue(
            settings.endless
        )

    def test_get_daily(self):
        settings = GameModeManager.get(
            GameMode.DAILY
        )

        self.assertTrue(
            settings.daily
        )

    # get_all()

    def test_get_all_returns_list(self):
        modes = GameModeManager.get_all()

        self.assertIsInstance(
            modes,
            list
        )

    def test_get_all_length(self):
        modes = GameModeManager.get_all()

        self.assertEqual(
            len(modes),
            4
        )

    # get_names()

    def test_get_names(self):
        self.assertEqual(
            GameModeManager.get_names(),
            [
                "Classic",
                "Timed",
                "Endless",
                "Daily Challenge"
            ]
        ) 

        # from_string()

    def test_from_string_classic(self):
        self.assertEqual(
            GameModeManager.from_string(
                "Classic"
            ),
            GameMode.CLASSIC
        )

    def test_from_string_timed(self):
        self.assertEqual(
            GameModeManager.from_string(
                "Timed"
            ),
            GameMode.TIMED
        )

    def test_from_string_endless(self):
        self.assertEqual(
            GameModeManager.from_string(
                "Endless"
            ),
            GameMode.ENDLESS
        )

    def test_from_string_daily(self):
        self.assertEqual(
            GameModeManager.from_string(
                "Daily Challenge"
            ),
            GameMode.DAILY
        )

    def test_from_string_case_insensitive(self):
        self.assertEqual(
            GameModeManager.from_string(
                "cLaSsIc"
            ),
            GameMode.CLASSIC
        )

    def test_from_string_with_spaces(self):
        self.assertEqual(
            GameModeManager.from_string(
                "   Timed   "
            ),
            GameMode.TIMED
        )

    def test_from_string_invalid(self):
        with self.assertRaises(ValueError):
            GameModeManager.from_string(
                "Impossible"
            )

    # print_modes()

    @patch("builtins.print")
    def test_print_modes(self, mocked_print):
        GameModeManager.print_modes()

        self.assertGreater(
            mocked_print.call_count,
            0
        )

    # reset()

    def test_reset(self):
        GameModeManager.set_mode(
            GameMode.ENDLESS
        )

        GameModeManager.reset()

        self.assertEqual(
            GameModeManager.get_current(),
            GameMode.CLASSIC
        )

    # is_timed()

    def test_is_timed_true(self):
        GameModeManager.set_mode(
            GameMode.TIMED
        )

        self.assertTrue(
            GameModeManager.is_timed()
        )

    def test_is_timed_false(self):
        GameModeManager.set_mode(
            GameMode.CLASSIC
        )

        self.assertFalse(
            GameModeManager.is_timed()
        )

    # is_endless()

    def test_is_endless_true(self):
        GameModeManager.set_mode(
            GameMode.ENDLESS
        )

        self.assertTrue(
            GameModeManager.is_endless()
        )

    def test_is_endless_false(self):
        GameModeManager.set_mode(
            GameMode.CLASSIC
        )

        self.assertFalse(
            GameModeManager.is_endless()
        )

    # is_daily()

    def test_is_daily_true(self):
        GameModeManager.set_mode(
            GameMode.DAILY
        )

        self.assertTrue(
            GameModeManager.is_daily()
        )

    def test_is_daily_false(self):
        GameModeManager.set_mode(
            GameMode.CLASSIC
        )

        self.assertFalse(
            GameModeManager.is_daily()
        )

    # save_allowed()

    def test_save_allowed_true(self):
        GameModeManager.set_mode(
            GameMode.CLASSIC
        )

        self.assertTrue(
            GameModeManager.save_allowed()
        )

    def test_save_allowed_false(self):
        GameModeManager.set_mode(
            GameMode.DAILY
        )

        self.assertFalse(
            GameModeManager.save_allowed()
        ) 

        # get_time_limit()

    def test_time_limit_classic(self):
        GameModeManager.set_mode(
            GameMode.CLASSIC
        )

        self.assertIsNone(
            GameModeManager.get_time_limit()
        )

    def test_time_limit_timed(self):
        GameModeManager.set_mode(
            GameMode.TIMED
        )

        self.assertEqual(
            GameModeManager.get_time_limit(),
            300
        )

    def test_time_limit_endless(self):
        GameModeManager.set_mode(
            GameMode.ENDLESS
        )

        self.assertIsNone(
            GameModeManager.get_time_limit()
        )

    def test_time_limit_daily(self):
        GameModeManager.set_mode(
            GameMode.DAILY
        )

        self.assertIsNone(
            GameModeManager.get_time_limit()
        )

    # Settings Verification

    def test_classic_settings(self):
        settings = GameModeManager.get(
            GameMode.CLASSIC
        )

        self.assertEqual(
            settings.name,
            "Classic"
        )

        self.assertFalse(
            settings.timed
        )

        self.assertFalse(
            settings.endless
        )

        self.assertFalse(
            settings.daily
        )

        self.assertTrue(
            settings.allow_save
        )

        self.assertTrue(
            settings.uses_score
        )

        self.assertIsNone(
            settings.time_limit
        )

    def test_timed_settings(self):
        settings = GameModeManager.get(
            GameMode.TIMED
        )

        self.assertEqual(
            settings.name,
            "Timed"
        )

        self.assertTrue(
            settings.timed
        )

        self.assertFalse(
            settings.endless
        )

        self.assertFalse(
            settings.daily
        )

        self.assertTrue(
            settings.allow_save
        )

        self.assertTrue(
            settings.uses_score
        )

        self.assertEqual(
            settings.time_limit,
            300
        )

    def test_endless_settings(self):
        settings = GameModeManager.get(
            GameMode.ENDLESS
        )

        self.assertEqual(
            settings.name,
            "Endless"
        )

        self.assertFalse(
            settings.timed
        )

        self.assertTrue(
            settings.endless
        )

        self.assertFalse(
            settings.daily
        )

        self.assertTrue(
            settings.allow_save
        )

        self.assertTrue(
            settings.uses_score
        )

        self.assertIsNone(
            settings.time_limit
        )

    def test_daily_settings(self):
        settings = GameModeManager.get(
            GameMode.DAILY
        )

        self.assertEqual(
            settings.name,
            "Daily Challenge"
        )

        self.assertFalse(
            settings.timed
        )

        self.assertFalse(
            settings.endless
        )

        self.assertTrue(
            settings.daily
        )

        self.assertFalse(
            settings.allow_save
        )

        self.assertTrue(
            settings.uses_score
        )

        self.assertIsNone(
            settings.time_limit
        )

    # Dataclass

    def test_settings_are_dataclass(self):
        self.assertIsInstance(
            GameModeManager.get_settings(),
            GameModeSettings
        )

    # Edge Cases

    def test_multiple_mode_changes(self):
        GameModeManager.set_mode(
            GameMode.TIMED
        )

        GameModeManager.set_mode(
            GameMode.ENDLESS
        )

        GameModeManager.set_mode(
            GameMode.DAILY
        )

        self.assertEqual(
            GameModeManager.get_current(),
            GameMode.DAILY
        )

    def test_reset_after_multiple_changes(self):
        GameModeManager.set_mode(
            GameMode.TIMED
        )

        GameModeManager.set_mode(
            GameMode.ENDLESS
        )

        GameModeManager.reset()

        self.assertEqual(
            GameModeManager.get_current(),
            GameMode.CLASSIC
        )


if __name__ == "__main__":
    unittest.main() 

