# test_renderer.py
# Unit tests for renderer.py

import unittest
from unittest.mock import patch, Mock 

from game.renderer import Renderer
from assets.colors import Colors


class TestRenderer(unittest.TestCase):
    # Unit tests for the Renderer class

    def setUp(self):
        self.renderer = Renderer()

    # Constructor

    def test_renderer_created(self):
        self.assertIsInstance(
            self.renderer,
            Renderer
        )

    def test_default_width(self):
        self.assertGreater(
            self.renderer.width,
            0
        )

    # Generic Helpers

    @patch("game.renderer.Animation.clear_screen")
    def test_clear(
        self,
        mocked_clear
    ):
        self.renderer.clear()

        self.assertEqual(
            mocked_clear.call_count,
            1
        )

    @patch("game.renderer.Animation.pause")
    def test_pause(
        self,
        mocked_pause
    ):
        self.renderer.pause(2)

        mocked_pause.assert_called_with(2)

    @patch("builtins.print")
    def test_separator(
        self,
        mocked_print
    ):
        self.renderer.separator()

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_blank_line(
        self,
        mocked_print
    ):
        self.renderer.blank_line(3)

        self.assertEqual(
            mocked_print.call_count,
            3
        )

    @patch("builtins.print")
    def test_centered(
        self,
        mocked_print
    ):
        self.renderer.centered(
            "Hello"
        )

        mocked_print.assert_called_once()

    @patch.object(Renderer, "separator")
    @patch.object(Renderer, "centered")
    @patch.object(Renderer, "blank_line")
    def test_title(
        self,
        mocked_blank,
        mocked_centered,
        mocked_separator
    ):
        self.renderer.title(
            "TITLE"
        )

        self.assertEqual(
            mocked_separator.call_count,
            2
        )

        mocked_centered.assert_called_once()

    @patch.object(Renderer, "centered")
    @patch.object(Renderer, "separator")
    def test_subtitle(
        self,
        mocked_separator,
        mocked_centered
    ):
        self.renderer.subtitle(
            "Subtitle"
        )

        mocked_centered.assert_called_once()

        mocked_separator.assert_called_once()

    # Logo

    @patch("game.renderer.Banner.show")
    def test_logo(
        self,
        mocked_banner
    ):
        self.renderer.logo()

        mocked_banner.assert_called_once()

    # Menus

    @patch("builtins.print")
    def test_menu_option(
        self,
        mocked_print
    ):
        self.renderer.menu_option(
            1,
            "Play"
        )

        mocked_print.assert_called_once()

    @patch(
        "builtins.input",
        return_value=""
    )
    def test_wait_for_enter(
        self,
        mocked_input
    ):
        self.renderer.wait_for_enter()

        mocked_input.assert_called_once()

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "logo")
    @patch.object(Renderer, "blank_line")
    @patch.object(Renderer, "centered")
    @patch("game.renderer.Animation.loading_bar")
    def test_loading_screen(
        self,
        mocked_loading,
        mocked_centered,
        mocked_blank,
        mocked_logo,
        mocked_clear
    ):
        self.renderer.loading_screen()

        mocked_clear.assert_called_once()
        mocked_logo.assert_called_once()
        mocked_loading.assert_called_once()
        mocked_centered.assert_called_once()

    @patch.object(Renderer, "centered")
    def test_message(
        self,
        mocked_centered
    ):
        self.renderer.message(
            "Hello"
        )

        mocked_centered.assert_called_once()

    @patch.object(Renderer, "message")
    def test_success(
        self,
        mocked_message
    ):
        self.renderer.success(
            "Done"
        )

        mocked_message.assert_called_once_with(
            "Done",
            Colors.GREEN
        )

    @patch.object(Renderer, "message")
    def test_warning(
        self,
        mocked_message
    ):
        self.renderer.warning(
            "Warning"
        )

        mocked_message.assert_called_once_with(
            "Warning",
            Colors.YELLOW
        )

    @patch.object(Renderer, "message")
    def test_error(
        self,
        mocked_message
    ):
        self.renderer.error(
            "Error"
        )

        mocked_message.assert_called_once_with(
            "Error",
            Colors.RED
        )

    @patch.object(Renderer, "message")
    def test_info(
        self,
        mocked_message
    ):
        self.renderer.info(
            "Info"
        )

        mocked_message.assert_called_once_with(
            "Info",
            Colors.CYAN
        ) 

        # Gameplay Rendering

    @patch("builtins.print")
    @patch("game.renderer.HangmanFrames.get_frame")
    def test_draw_hangman(
        self,
        mocked_frame,
        mocked_print
    ):
        mocked_frame.return_value = "FRAME"

        self.renderer.draw_hangman(3)

        mocked_frame.assert_called_once_with(3)
        mocked_print.assert_called_once_with("FRAME")

    @patch.object(Renderer, "centered")
    def test_draw_hidden_word(
        self,
        mocked_centered
    ):
        self.renderer.draw_hidden_word(
            "_ A _ G _ A N"
        )

        mocked_centered.assert_called_once()

    @patch("builtins.print")
    def test_draw_category(
        self,
        mocked_print
    ):
        self.renderer.draw_category(
            "Animals"
        )

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_difficulty(
        self,
        mocked_print
    ):
        self.renderer.draw_difficulty(
            "Hard"
        )

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_score(
        self,
        mocked_print
    ):
        self.renderer.draw_score(
            500
        )

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_timer(
        self,
        mocked_print
    ):
        self.renderer.draw_timer(
            125
        )

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_remaining_lives(
        self,
        mocked_print
    ):
        self.renderer.draw_remaining_lives(
            5
        )

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_player(
        self,
        mocked_print
    ):
        self.renderer.draw_player(
            "Anay"
        )

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_correct_letters_empty(
        self,
        mocked_print
    ):
        self.renderer.draw_correct_letters([])

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_correct_letters(
        self,
        mocked_print
    ):
        self.renderer.draw_correct_letters(
            ["C", "A", "T"]
        )

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_wrong_letters_empty(
        self,
        mocked_print
    ):
        self.renderer.draw_wrong_letters([])

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_wrong_letters(
        self,
        mocked_print
    ):
        self.renderer.draw_wrong_letters(
            ["X", "Z"]
        )

        mocked_print.assert_called_once()

    @patch("builtins.print")
    def test_draw_guess_count(
        self,
        mocked_print
    ):
        self.renderer.draw_guess_count(
            17
        )

        mocked_print.assert_called_once()

    @patch(
        "builtins.input",
        return_value="a"
    )
    def test_prompt_guess(
        self,
        mocked_input
    ):
        result = self.renderer.prompt_guess()

        self.assertEqual(
            result,
            "A"
        )

    @patch(
        "builtins.input",
        return_value="3"
    )
    def test_prompt_menu_choice(
        self,
        mocked_input
    ):
        result = self.renderer.prompt_menu_choice()

        self.assertEqual(
            result,
            "3"
        ) 

        # Complete Game Screen Rendering

    @patch.object(Renderer, "separator")
    @patch.object(Renderer, "draw_player")
    @patch.object(Renderer, "draw_difficulty")
    @patch.object(Renderer, "draw_category")
    @patch.object(Renderer, "draw_score")
    @patch.object(Renderer, "draw_remaining_lives")
    @patch.object(Renderer, "draw_timer")
    def test_draw_status_panel(
        self,
        mocked_timer,
        mocked_lives,
        mocked_score,
        mocked_category,
        mocked_difficulty,
        mocked_player,
        mocked_separator
    ):
        self.renderer.draw_status_panel(
            player="Anay",
            difficulty="Hard",
            category="Animals",
            score=500,
            lives=5,
            elapsed_time=120
        )

        self.assertEqual(
            mocked_separator.call_count,
            2
        )

        mocked_player.assert_called_once()
        mocked_difficulty.assert_called_once()
        mocked_category.assert_called_once()
        mocked_score.assert_called_once()
        mocked_lives.assert_called_once()
        mocked_timer.assert_called_once()

    @patch.object(Renderer, "draw_correct_letters")
    @patch.object(Renderer, "draw_wrong_letters")
    def test_draw_letter_panels(
        self,
        mocked_wrong,
        mocked_correct
    ):
        self.renderer.draw_letter_panels(
            ["A", "B"],
            ["X", "Y"]
        )

        mocked_correct.assert_called_once_with(
            ["A", "B"]
        )

        mocked_wrong.assert_called_once_with(
            ["X", "Y"]
        )

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "logo")
    @patch.object(Renderer, "blank_line")
    @patch.object(Renderer, "draw_status_panel")
    @patch.object(Renderer, "draw_hangman")
    @patch.object(Renderer, "draw_hidden_word")
    @patch.object(Renderer, "draw_letter_panels")
    def test_draw_game_screen(
        self,
        mocked_letters,
        mocked_word,
        mocked_hangman,
        mocked_status,
        mocked_blank,
        mocked_logo,
        mocked_clear
    ):
        self.renderer.draw_game_screen(
            player="Anay",
            difficulty="Easy",
            category="Animals",
            score=100,
            lives=6,
            elapsed_time=45,
            hangman_stage=2,
            display_word="_ A _",
            correct_letters=["A"],
            wrong_letters=["X"]
        )

        mocked_clear.assert_called_once()
        mocked_logo.assert_called_once()
        mocked_status.assert_called_once()
        mocked_hangman.assert_called_once_with(2)
        mocked_word.assert_called_once_with("_ A _")
        mocked_letters.assert_called_once_with(
            ["A"],
            ["X"]
        )

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "menu_option")
    def test_draw_pause_screen(
        self,
        mocked_option,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_pause_screen()

        mocked_clear.assert_called_once()
        mocked_title.assert_called_once()

        self.assertEqual(
            mocked_option.call_count,
            4
        )

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "blank_line")
    @patch("builtins.print")
    def test_draw_help_screen(
        self,
        mocked_print,
        mocked_blank,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_help_screen()

        mocked_clear.assert_called_once()
        mocked_title.assert_called_once()
        mocked_blank.assert_called_once()

        self.assertEqual(
            mocked_print.call_count,
            6
        )

    @patch.object(Renderer, "title")
    @patch.object(Renderer, "blank_line")
    @patch("builtins.print")
    def test_draw_statistics_summary(
        self,
        mocked_print,
        mocked_blank,
        mocked_title
    ):
        self.renderer.draw_statistics_summary(
            games_played=20,
            wins=12,
            losses=8,
            win_rate=60.0,
            highest_score=1500
        )

        mocked_title.assert_called_once()
        mocked_blank.assert_called_once()

        self.assertEqual(
            mocked_print.call_count,
            5
        )

    @patch.object(Renderer, "title")
    @patch.object(Renderer, "blank_line")
    @patch("builtins.print")
    def test_draw_player_summary(
        self,
        mocked_print,
        mocked_blank,
        mocked_title
    ):
        self.renderer.draw_player_summary(
            player="Anay",
            score=1000,
            streak=6
        )

        mocked_title.assert_called_once()
        mocked_blank.assert_called_once()

        self.assertEqual(
            mocked_print.call_count,
            3
        ) 

    @patch(
        "builtins.input",
        return_value="Y"
    )
    def test_draw_confirmation_yes(
        self,
        mocked_input
    ):
        result = self.renderer.draw_confirmation(
            "Continue?"
        )

        self.assertTrue(result)

    @patch(
        "builtins.input",
        return_value="N"
    )
    def test_draw_confirmation_no(
        self,
        mocked_input
    ):
        result = self.renderer.draw_confirmation(
            "Continue?"
        )

        self.assertFalse(result)

    @patch.object(Renderer, "blank_line")
    @patch.object(Renderer, "centered")
    def test_draw_notification(
        self,
        mocked_centered,
        mocked_blank
    ):
        self.renderer.draw_notification(
            "Saved Successfully"
        )

        self.assertEqual(
            mocked_blank.call_count,
            2
        )

        mocked_centered.assert_called_once()

    # Main Menu Screens

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "logo")
    @patch.object(Renderer, "blank_line")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "menu_option")
    def test_draw_main_menu(
        self,
        mocked_option,
        mocked_title,
        mocked_blank,
        mocked_logo,
        mocked_clear
    ):
        self.renderer.draw_main_menu()

        mocked_clear.assert_called_once()
        mocked_logo.assert_called_once()
        mocked_title.assert_called_once()

        self.assertEqual(
            mocked_option.call_count,
            7
        )

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "menu_option")
    @patch.object(Renderer, "blank_line")
    def test_draw_new_game_menu(
        self,
        mocked_blank,
        mocked_option,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_new_game_menu()

        mocked_clear.assert_called_once()
        mocked_title.assert_called_once()

        self.assertEqual(
            mocked_option.call_count,
            4
        )

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "menu_option")
    @patch.object(Renderer, "blank_line")
    def test_draw_difficulty_menu(
        self,
        mocked_blank,
        mocked_option,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_difficulty_menu()

        mocked_clear.assert_called_once()
        mocked_title.assert_called_once()

        self.assertEqual(
            mocked_option.call_count,
            5
        )

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "menu_option")
    @patch.object(Renderer, "blank_line")
    def test_draw_game_mode_menu(
        self,
        mocked_blank,
        mocked_option,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_game_mode_menu()

        mocked_clear.assert_called_once()
        mocked_title.assert_called_once()

        self.assertEqual(
            mocked_option.call_count,
            4
        )

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "blank_line")
    @patch.object(Renderer, "menu_option")
    @patch("builtins.print")
    def test_draw_continue_menu(
        self,
        mocked_print,
        mocked_option,
        mocked_blank,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_continue_menu(
            "Anay"
        )

        mocked_clear.assert_called_once()
        mocked_title.assert_called_once()

        mocked_print.assert_called_once()

        self.assertEqual(
            mocked_option.call_count,
            3
        )

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "menu_option")
    @patch.object(Renderer, "blank_line")
    def test_draw_settings_menu(
        self,
        mocked_blank,
        mocked_option,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_settings_menu()

        mocked_clear.assert_called_once()
        mocked_title.assert_called_once()

        self.assertEqual(
            mocked_option.call_count,
            4
        )

        # End Game Screens

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "blank_line")
    @patch.object(Renderer, "success")
    @patch.object(Renderer, "draw_timer")
    @patch("builtins.print")
    @patch("game.renderer.Animation.victory_animation")
    def test_draw_victory_screen(
        self,
        mocked_animation,
        mocked_print,
        mocked_timer,
        mocked_success,
        mocked_blank,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_victory_screen(
            player="Anay",
            word="PYTHON",
            score=1200,
            elapsed_time=95
        )

        mocked_clear.assert_called_once()
        mocked_animation.assert_called_once()
        mocked_title.assert_called_once()
        mocked_timer.assert_called_once_with(95)
        mocked_success.assert_called_once()

        self.assertEqual(
            mocked_print.call_count,
            3
        )

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "blank_line")
    @patch.object(Renderer, "error")
    @patch("builtins.print")
    @patch("game.renderer.Animation.game_over_animation")
    def test_draw_game_over_screen(
        self,
        mocked_animation,
        mocked_print,
        mocked_error,
        mocked_blank,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_game_over_screen(
            player="Anay",
            word="PYTHON",
            score=450
        )

        mocked_clear.assert_called_once()
        mocked_animation.assert_called_once()
        mocked_title.assert_called_once()
        mocked_error.assert_called_once()

        self.assertEqual(
            mocked_print.call_count,
            3
        )

    @patch.object(Renderer, "title")
    @patch.object(Renderer, "centered")
    @patch.object(Renderer, "blank_line")
    def test_draw_final_score(
        self,
        mocked_blank,
        mocked_centered,
        mocked_title
    ):
        self.renderer.draw_final_score(
            2000
        )

        mocked_title.assert_called_once()
        mocked_centered.assert_called_once()
        mocked_blank.assert_called_once()

    @patch.object(Renderer, "title")
    @patch.object(Renderer, "warning")
    def test_draw_leaderboard_empty(
        self,
        mocked_warning,
        mocked_title
    ):
        self.renderer.draw_leaderboard([])

        mocked_title.assert_called_once()
        mocked_warning.assert_called_once()

    @patch.object(Renderer, "title")
    @patch.object(Renderer, "separator")
    @patch.object(Renderer, "blank_line")
    @patch("builtins.print")
    def test_draw_leaderboard(
        self,
        mocked_print,
        mocked_blank,
        mocked_separator,
        mocked_title
    ):
        leaderboard = [
            ("Alice", 2000),
            ("Bob", 1800),
            ("Charlie", 1500)
        ]

        self.renderer.draw_leaderboard(
            leaderboard
        )

        mocked_title.assert_called_once()
        mocked_separator.assert_called_once()
        mocked_blank.assert_called_once()

        self.assertEqual(
            mocked_print.call_count,
            4
        )

    @patch.object(Renderer, "title")
    @patch.object(Renderer, "warning")
    def test_draw_statistics_screen_empty(
        self,
        mocked_warning,
        mocked_title
    ):
        self.renderer.draw_statistics_screen(
            {}
        )

        mocked_title.assert_called_once()
        mocked_warning.assert_called_once()

    @patch.object(Renderer, "title")
    @patch.object(Renderer, "blank_line")
    @patch("builtins.print")
    def test_draw_statistics_screen(
        self,
        mocked_print,
        mocked_blank,
        mocked_title
    ):
        statistics = {
            "Games Played": 10,
            "Wins": 8,
            "Losses": 2
        }

        self.renderer.draw_statistics_screen(
            statistics
        )

        mocked_title.assert_called_once()
        mocked_blank.assert_called_once()

        self.assertEqual(
            mocked_print.call_count,
            3
        ) 

    @patch("builtins.print")
    def test_draw_box(
        self,
        mocked_print
    ):
        self.renderer.draw_box(
            "TITLE",
            [
                "Line 1",
                "Line 2"
            ]
        )

        self.assertGreater(
            mocked_print.call_count,
            0
        )

    @patch.object(Renderer, "separator")
    @patch.object(Renderer, "centered")
    def test_draw_footer(
        self,
        mocked_centered,
        mocked_separator
    ):
        self.renderer.draw_footer(
            "Good Luck!"
        )

        self.assertEqual(
            mocked_separator.call_count,
            2
        )

        mocked_centered.assert_called_once()

    # Dialog Boxes

    @patch.object(Renderer, "draw_box")
    def test_draw_info_box(
        self,
        mocked_box
    ):
        self.renderer.draw_info_boxes(
            "Information"
        )

        mocked_box.assert_called_once_with(
            "INFORMATION",
            ["Information"]
        )

    @patch.object(Renderer, "draw_box")
    def test_draw_success_box(
        self,
        mocked_box
    ):
        self.renderer.draw_success_box(
            "Success"
        )

        mocked_box.assert_called_once_with(
            "SUCCESS",
            ["Success"]
        )

    @patch.object(Renderer, "draw_box")
    def test_draw_warning_box(
        self,
        mocked_box
    ):
        self.renderer.draw_warning_box(
            "Warning"
        )

        mocked_box.assert_called_once_with(
            "WARNING",
            ["Warning"]
        )

    @patch.object(Renderer, "draw_box")
    def test_draw_error_box(
        self,
        mocked_box
    ):
        self.renderer.draw_error_box(
            "Error"
        )

        mocked_box.assert_called_once_with(
            "ERROR",
            ["Error"]
        )

    # Miscellaneous Screens

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "logo")
    @patch.object(Renderer, "blank_line")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "centered")
    @patch("game.renderer.Animation.type_text")
    def test_draw_goodbye_screen(
        self,
        mocked_type,
        mocked_centered,
        mocked_title,
        mocked_blank,
        mocked_logo,
        mocked_clear
    ):
        self.renderer.draw_goodbye_screen()

        mocked_clear.assert_called_once()
        mocked_logo.assert_called_once()
        mocked_title.assert_called_once()

        self.assertEqual(
            mocked_centered.call_count,
            2
        )

        mocked_type.assert_called_once()

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "title")
    @patch.object(Renderer, "centered")
    @patch.object(Renderer, "blank_line")
    def test_draw_credits_screen(
        self,
        mocked_blank,
        mocked_centered,
        mocked_title,
        mocked_clear
    ):
        self.renderer.draw_credits_screen()

        mocked_clear.assert_called_once()
        mocked_title.assert_called_once()
        mocked_blank.assert_called_once()

        self.assertGreater(
            mocked_centered.call_count,
            0
        )

    @patch(
        "builtins.input",
        return_value=""
    )
    def test_wait_for_key(
        self,
        mocked_input
    ):
        self.renderer.wait_for_key()

        mocked_input.assert_called_once()

    @patch.object(Renderer, "clear")
    @patch.object(Renderer, "logo")
    @patch.object(Renderer, "blank_line")
    @patch("game.renderer.Animation.loading_bar")
    def test_splash_screen(
        self,
        mocked_loading,
        mocked_blank,
        mocked_logo,
        mocked_clear
    ):
        self.renderer.splash_screen()

        mocked_clear.assert_called_once()
        mocked_logo.assert_called_once()
        mocked_loading.assert_called_once()

    # String Representation

    def test_string_representation(self):
        text = str(
            self.renderer
        )

        self.assertIn(
            "Renderer",
            text
        )

    def test_repr(self):
        self.assertEqual(
            repr(self.renderer),
            str(self.renderer)
        )


if __name__ == "__main__":
    unittest.main() 

