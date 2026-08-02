# test_engine.py 
# Unit tests for engine.py 

import unittest
from unittest.mock import MagicMock, patch

from game.engine import Engine
from game.player import Player
from game.difficulty import Difficulty, DifficultyManager 
from game.game_mode import GameMode


class TestEngineInitialization(unittest.TestCase):

    def setUp(self):
        self.engine = Engine()

    # Initialization

    def test_engine_created(self):
        self.assertIsInstance(self.engine, Engine)

    def test_renderer_created(self):
        self.assertIsNotNone(self.engine.renderer)

    def test_word_manager_created(self):
        self.assertIsNotNone(self.engine.word_manager)

    def test_validator_created(self):
        self.assertIsNotNone(self.engine.validator)

    def test_scoreboard_created(self):
        self.assertIsNotNone(self.engine.scoreboard)

    def test_statistics_created(self):
        self.assertIsNotNone(self.engine.statistics)

    def test_save_system_created(self):
        self.assertIsNotNone(self.engine.save_system)

    def test_timer_created(self):
        self.assertIsNotNone(self.engine.timer)

    def test_player_created(self):
        self.assertIsInstance(self.engine.player, Player)

    def test_default_difficulty(self):
        self.assertEqual(
            self.engine.difficulty,
            Difficulty.EASY
        )

    def test_default_game_mode(self):
        self.assertEqual(
            self.engine.game_mode,
            GameMode.CLASSIC
        )

    def test_word_initially_empty(self):
        self.assertEqual(
            self.engine.word,
            ""
        )

    def test_category_initially_empty(self):
        self.assertEqual(
            self.engine.category,
            ""
        )

    def test_display_word_initially_empty(self):
        self.assertEqual(
            self.engine.display_word,
            ""
        )

    def test_correct_letters_initially_empty(self):
        self.assertEqual(
            self.engine.correct_letters,
            set()
        )

    def test_wrong_letters_initially_empty(self):
        self.assertEqual(
            self.engine.wrong_letters,
            set()
        )

    def test_initial_score_zero(self):
        self.assertEqual(
            self.engine.score,
            0
        )

    def test_initial_stage_zero(self):
        self.assertEqual(
            self.engine.hangman_stage,
            0
        )

    def test_game_not_running(self):
        self.assertFalse(
            self.engine.game_running
        )

    def test_game_not_won(self):
        self.assertFalse(
            self.engine.game_won
        )

    def test_game_not_over(self):
        self.assertFalse(
            self.engine.game_over
        )

    # reset_game()

    def test_reset_game_clears_everything(self):

        self.engine.word = "APPLE"
        self.engine.category = "Fruit"
        self.engine.display_word = "_ _ _ _ _"

        self.engine.correct_letters = {"A"}
        self.engine.wrong_letters = {"B"}

        self.engine.score = 100
        self.engine.hangman_stage = 4

        self.engine.game_running = True
        self.engine.game_won = True
        self.engine.game_over = True

        self.engine.timer.reset = MagicMock()

        self.engine.reset_game()

        self.assertEqual(self.engine.word, "")
        self.assertEqual(self.engine.category, "")
        self.assertEqual(self.engine.display_word, "")

        self.assertEqual(
            self.engine.correct_letters,
            set()
        )

        self.assertEqual(
            self.engine.wrong_letters,
            set()
        )

        self.assertEqual(
            self.engine.score,
            0
        )

        self.assertEqual(
            self.engine.hangman_stage,
            0
        )

        self.assertFalse(
            self.engine.game_running
        )

        self.assertFalse(
            self.engine.game_won
        )

        self.assertFalse(
            self.engine.game_over
        )

        self.engine.timer.reset.assert_called_once()

    # set_player()

    def test_set_player_changes_player(self):

        self.engine.set_player("Alex")

        self.assertEqual(
            self.engine.player.name,
            "Alex"
        )

    def test_set_player_creates_new_object(self):

        old_player = self.engine.player

        self.engine.set_player("Chris")

        self.assertIsNot(
            old_player,
            self.engine.player
        )

    # set_difficulty()

    def test_set_difficulty_easy(self):

        self.engine.set_difficulty(
            Difficulty.EASY
        )

        self.assertEqual(
            self.engine.difficulty,
            Difficulty.EASY
        )

    def test_set_difficulty_hard(self):

        self.engine.set_difficulty(
            Difficulty.HARD
        )

        self.assertEqual(
            self.engine.difficulty,
            Difficulty.HARD
        )

    def test_set_difficulty_impossible(self):

        self.engine.set_difficulty(
            Difficulty.IMPOSSIBLE
        )

        self.assertEqual(
            self.engine.difficulty,
            Difficulty.IMPOSSIBLE
        )

    # set_game_mode()

    def test_set_game_mode_classic(self):

        self.engine.set_game_mode(
            GameMode.CLASSIC
        )

        self.assertEqual(
            self.engine.game_mode,
            GameMode.CLASSIC
        )

    def test_set_game_mode_timed(self):

        self.engine.set_game_mode(
            GameMode.TIMED
        )

        self.assertEqual(
            self.engine.game_mode,
            GameMode.TIMED
        )

    def test_set_game_mode_endless(self):

        self.engine.set_game_mode(
            GameMode.ENDLESS
        )

        self.assertEqual(
            self.engine.game_mode,
            GameMode.ENDLESS
        )

    def test_set_game_mode_daily(self):

        self.engine.set_game_mode(
            GameMode.DAILY
        )

        self.assertEqual(
            self.engine.game_mode,
            GameMode.DAILY
        )

    # load_new_word()

    @patch("game.engine.WordManager")
    def test_load_new_word(
        self,
        mock_manager
    ):
        manager = mock_manager.return_value

        manager.get_random_word.return_value = (
            "python",
            "Programming"
        )

        manager.create_display_word.return_value = (
            "_ _ _ _ _ _"
        )

        self.engine.word_manager = manager

        self.engine.load_new_word()

        manager.get_random_word.assert_called_once_with(
            self.engine.difficulty
        )

        manager.create_display_word.assert_called_once_with(
            "PYTHON"
        )

        self.assertEqual(
            self.engine.word,
            "PYTHON"
        )

        self.assertEqual(
            self.engine.category,
            "Programming"
        )

        self.assertEqual(
            self.engine.display_word,
            "_ _ _ _ _ _"
        )

    # start_game()

    def test_start_game_calls_required_methods(self):

        self.engine.reset_game = MagicMock()
        self.engine.load_new_word = MagicMock()

        self.engine.timer.start = MagicMock()

        self.engine.start_game()

        self.engine.reset_game.assert_called_once()
        self.engine.load_new_word.assert_called_once()

        self.engine.timer.start.assert_called_once()

        self.assertTrue(
            self.engine.game_running
        ) 

class TestEngineGameplayLogic(unittest.TestCase):
    def setUp(self):
        self.engine = Engine()

    # update_display_word()

    def test_update_display_word(self):

        self.engine.word = "APPLE"
        self.engine.correct_letters = {"A", "P"}

        self.engine.word_manager.create_display_word = MagicMock(
            return_value="A P P _ _"
        )

        self.engine.update_display_word()

        self.engine.word_manager.create_display_word.assert_called_once_with(
            "APPLE",
            {"A", "P"},
        )

        self.assertEqual(
            self.engine.display_word,
            "A P P _ _"
        )

    # process_guess()

    def test_process_guess_correct(self):

        self.engine.word = "APPLE"

        self.engine.validator.validate_letter = MagicMock(
            return_value="A"
        )

        self.engine.handle_correct_guess = MagicMock()

        result = self.engine.process_guess("a")

        self.assertTrue(result)

        self.engine.handle_correct_guess.assert_called_once_with(
            "A"
        )

    def test_process_guess_wrong(self):

        self.engine.word = "APPLE"

        self.engine.validator.validate_letter = MagicMock(
            return_value="Z"
        )

        self.engine.handle_wrong_guess = MagicMock()

        result = self.engine.process_guess("z")

        self.assertFalse(result)

        self.engine.handle_wrong_guess.assert_called_once_with(
            "Z"
        )

    def test_process_guess_duplicate_correct(self):

        self.engine.correct_letters = {"A"}

        self.engine.validator.validate_letter = MagicMock(
            return_value="A"
        )

        self.engine.handle_correct_guess = MagicMock()

        result = self.engine.process_guess("A")

        self.assertFalse(result)

        self.engine.handle_correct_guess.assert_not_called()

    def test_process_guess_duplicate_wrong(self):

        self.engine.wrong_letters = {"Z"}

        self.engine.validator.validate_letter = MagicMock(
            return_value="Z"
        )

        self.engine.handle_wrong_guess = MagicMock()

        result = self.engine.process_guess("Z")

        self.assertFalse(result)

        self.engine.handle_wrong_guess.assert_not_called()

    def test_process_guess_invalid_letter(self):

        self.engine.validator.validate_letter = MagicMock(
            side_effect=ValueError
        )

        result = self.engine.process_guess("11")

        self.assertFalse(result)

    # handle_correct_guess()

    def test_handle_correct_guess_adds_letter(self):

        self.engine.word = "APPLE"

        self.engine.update_display_word = MagicMock()

        self.engine.scoreboard.correct_guess = MagicMock(
            return_value=25
        )

        self.engine.handle_correct_guess("A")

        self.assertIn(
            "A",
            self.engine.correct_letters
        )

        self.engine.update_display_word.assert_called()

        self.assertEqual(
            self.engine.score,
            25
        )

    def test_handle_correct_guess_multiple_occurrences(self):

        self.engine.word = "LETTER"

        self.engine.scoreboard.correct_guess = MagicMock(
            return_value=10
        )

        self.engine.update_display_word = MagicMock()

        self.engine.handle_correct_guess("T")

        self.assertEqual(
            self.engine.score,
            20
        )

        self.assertEqual(
            self.engine.scoreboard.correct_guess.call_count,
            2
        )

    # handle_wrong_guess()

    def test_handle_wrong_guess(self):

        self.engine.remaining_lives = 6
        self.engine.hangman_stage = 1

        self.engine.handle_wrong_guess("X")

        self.assertIn(
            "X",
            self.engine.wrong_letters
        )

        self.assertEqual(
            self.engine.remaining_lives,
            5
        )

        self.assertEqual(
            self.engine.hangman_stage,
            2
        )

    # reveal_word()

    def test_reveal_word(self):

        self.engine.word = "PYTHON"

        self.engine.reveal_word()

        self.assertEqual(
            self.engine.display_word,
            "PYTHON"
        )

    # is_word_complete()

    def test_word_complete_true(self):

        self.engine.word = "DOG"

        self.engine.correct_letters = {
            "D",
            "O",
            "G"
        }

        self.assertTrue(
            self.engine.is_word_complete()
        )

    def test_word_complete_false(self):

        self.engine.word = "DOG"

        self.engine.correct_letters = {
            "D",
            "O"
        }

        self.assertFalse(
            self.engine.is_word_complete()
        )

    def test_word_complete_ignores_spaces(self):

        self.engine.word = "ICE CREAM"

        self.engine.correct_letters = {
            "I",
            "C",
            "E",
            "R",
            "A",
            "M"
        }

        self.assertTrue(
            self.engine.is_word_complete()
        )

    # is_game_won()

    def test_is_game_won_true(self):

        self.engine.is_word_complete = MagicMock(
            return_value=True
        )

        self.assertTrue(
            self.engine.is_game_won()
        )

    def test_is_game_won_false(self):

        self.engine.is_word_complete = MagicMock(
            return_value=False
        )

        self.assertFalse(
            self.engine.is_game_won()
        )

    # is_game_over()

    def test_is_game_over_true(self):

        self.engine.difficulty = Difficulty.EASY

        self.engine.hangman_stage = (
            DifficultyManager.get(
                Difficulty.EASY
            ).max_lives
        )

        self.assertTrue(
            self.engine.is_game_over()
        )

    def test_is_game_over_false(self):

        self.engine.difficulty = Difficulty.EASY

        self.engine.hangman_stage = 3

        self.assertFalse(
            self.engine.is_game_over()
        )

    # finish_game()

    def test_finish_game(self):

        self.engine.game_running = True

        self.engine.timer.stop = MagicMock()

        self.engine.finish_game()

        self.assertFalse(
            self.engine.game_running
        )

        self.assertTrue(
            self.engine.game_over
        )

        self.engine.timer.stop.assert_called_once()

    # finish_victory()

    def test_finish_victory(self):

        self.engine.finish_game = MagicMock()

        self.engine.scoreboard.word_completed = MagicMock(
            return_value=100
        )

        self.engine.scoreboard.calculate_final_score = MagicMock(
            return_value=250
        )

        self.engine.elapsed_time = MagicMock(
            return_value=40
        )

        self.engine.finish_victory()

        self.assertTrue(
            self.engine.game_won
        )

        self.assertEqual(
            self.engine.score,
            350
        )

        self.engine.finish_game.assert_called_once()

    # finish_defeat()

    def test_finish_defeat(self):

        self.engine.reveal_word = MagicMock()

        self.engine.finish_game = MagicMock()

        self.engine.finish_defeat()

        self.assertFalse(
            self.engine.game_won
        )

        self.engine.reveal_word.assert_called_once()

        self.engine.finish_game.assert_called_once() 

class TestEngineGameplayLoop(unittest.TestCase):
    def setUp(self):
        self.engine = Engine()

    # elapsed_time()

    def test_elapsed_time(self):

        self.engine.timer.elapsed = MagicMock(
            return_value=125
        )

        self.assertEqual(
            self.engine.elapsed_time(),
            125
        )

    # remaining_guess_count()

    def test_remaining_guess_count(self):

        self.engine.remaining_lives = 7

        self.assertEqual(
            self.engine.remaining_guess_count(),
            7
        )

    # total_guesses()

    def test_total_guesses(self):

        self.engine.correct_letters = {
            "A",
            "B",
            "C"
        }

        self.engine.wrong_letters = {
            "X",
            "Y"
        }

        self.assertEqual(
            self.engine.total_guesses(),
            5
        )

    # build_render_state()

    def test_build_render_state(self):

        self.engine.player.name = "Alex"

        self.engine.difficulty = Difficulty.HARD

        self.engine.category = "Animals"

        self.engine.score = 450

        self.engine.remaining_lives = 5

        self.engine.elapsed_time = MagicMock(
            return_value=84
        )

        self.engine.hangman_stage = 2

        self.engine.display_word = "_ A _"

        self.engine.correct_letters = {
            "A"
        }

        self.engine.wrong_letters = {
            "Z"
        }

        state = self.engine.build_render_state()

        self.assertEqual(
            state["player"],
            "Alex"
        )

        self.assertEqual(
            state["difficulty"],
            "Hard"
        )

        self.assertEqual(
            state["category"],
            "Animals"
        )

        self.assertEqual(
            state["score"],
            450
        )

        self.assertEqual(
            state["lives"],
            5
        )

        self.assertEqual(
            state["elapsed_time"],
            84
        )

        self.assertEqual(
            state["hangman_stage"],
            2
        )

        self.assertEqual(
            state["display_word"],
            "_ A _"
        )

        self.assertEqual(
            state["correct_letters"],
            ["A"]
        )

        self.assertEqual(
            state["wrong_letters"],
            ["Z"]
        )

    # render_game()

    def test_render_game(self):

        self.engine.build_render_state = MagicMock(
            return_value={
                "player": "Alex",
                "difficulty": "Easy",
                "category": "Animals",
                "score": 0,
                "lives": 10,
                "elapsed_time": 5,
                "hangman_stage": 0,
                "display_word": "_ _ _",
                "correct_letters": [],
                "wrong_letters": [],
            }
        )

        self.engine.renderer.draw_game_screen = MagicMock()

        self.engine.render_game()

        self.engine.renderer.draw_game_screen.assert_called_once()

    # get_player_guess()

    def test_get_player_guess(self):

        self.engine.renderer.prompt_guess = MagicMock(
            return_value="A"
        )

        self.assertEqual(
            self.engine.get_player_guess(),
            "A"
        )

    # process_turn()

    def test_process_turn_empty_input(self):

        self.engine.get_player_guess = MagicMock(
            return_value=""
        )

        self.engine.process_guess = MagicMock()

        self.engine.process_turn()

        self.engine.process_guess.assert_not_called()

    def test_process_turn_invalid_letter(self):

        self.engine.get_player_guess = MagicMock(
            return_value="11"
        )

        self.engine.validator.is_single_letter = MagicMock(
            return_value=False
        )

        self.engine.renderer.error = MagicMock()
        self.engine.renderer.pause = MagicMock()

        self.engine.process_turn()

        self.engine.renderer.error.assert_called_once()

        self.engine.renderer.pause.assert_called_once()

    def test_process_turn_duplicate_guess(self):

        self.engine.correct_letters = {
            "A"
        }

        self.engine.get_player_guess = MagicMock(
            return_value="A"
        )

        self.engine.validator.is_single_letter = MagicMock(
            return_value=True
        )

        self.engine.renderer.warning = MagicMock()
        self.engine.renderer.pause = MagicMock()

        self.engine.process_turn()

        self.engine.renderer.warning.assert_called_once()

    def test_process_turn_correct_guess(self):

        self.engine.get_player_guess = MagicMock(
            return_value="A"
        )

        self.engine.validator.is_single_letter = MagicMock(
            return_value=True
        )

        self.engine.process_guess = MagicMock(
            return_value=True
        )

        self.engine.renderer.success = MagicMock()
        self.engine.renderer.pause = MagicMock()

        self.engine.process_turn()

        self.engine.process_guess.assert_called_once_with("A")

        self.engine.renderer.success.assert_called_once()

    def test_process_turn_wrong_guess(self):

        self.engine.get_player_guess = MagicMock(
            return_value="Z"
        )

        self.engine.validator.is_single_letter = MagicMock(
            return_value=True
        )

        self.engine.process_guess = MagicMock(
            return_value=False
        )

        self.engine.renderer.error = MagicMock()
        self.engine.renderer.pause = MagicMock()

        self.engine.process_turn()

        self.engine.renderer.error.assert_called_once()

    # update_game_state()
 
    def test_update_game_state_victory(self):

        self.engine.is_game_won = MagicMock(
            return_value=True
        )

        self.engine.finish_victory = MagicMock()

        self.engine.update_game_state()

        self.engine.finish_victory.assert_called_once()

    def test_update_game_state_defeat(self):

        self.engine.is_game_won = MagicMock(
            return_value=False
        )

        self.engine.is_game_over = MagicMock(
            return_value=True
        )

        self.engine.finish_defeat = MagicMock()

        self.engine.update_game_state()

        self.engine.finish_defeat.assert_called_once()

    def test_update_game_state_continue(self):

        self.engine.is_game_won = MagicMock(
            return_value=False
        )

        self.engine.is_game_over = MagicMock(
            return_value=False
        )

        self.engine.finish_victory = MagicMock()
        self.engine.finish_defeat = MagicMock()

        self.engine.update_game_state()

        self.engine.finish_victory.assert_not_called()

        self.engine.finish_defeat.assert_not_called()

    # end_game()

    def test_end_game_victory(self):

        self.engine.game_won = True

        self.engine.handle_victory = MagicMock()

        self.engine.end_game()

        self.engine.handle_victory.assert_called_once()

    def test_end_game_defeat(self):

        self.engine.game_won = False

        self.engine.handle_defeat = MagicMock()

        self.engine.end_game()

        self.engine.handle_defeat.assert_called_once()

    # play()

    def test_play_runs_one_iteration(self):

        self.engine.render_game = MagicMock()

        self.engine.process_turn = MagicMock()

        self.engine.update_game_state = MagicMock(
            side_effect=lambda: setattr(
                self.engine,
                "game_running",
                False,
            )
        )

        self.engine.end_game = MagicMock()

        self.engine.play()

        self.engine.render_game.assert_called_once()

        self.engine.process_turn.assert_called_once()

        self.engine.update_game_state.assert_called_once()

        self.engine.end_game.assert_called_once() 

class TestEngineEndGame(unittest.TestCase):
    def setUp(self):
        self.engine = Engine()

    def test_record_statistics(self):

        self.engine.game_won = True
        self.engine.score = 750

        self.engine.player.current_streak = 4
        self.engine.player.hints_used = 2

        self.engine.elapsed_time = MagicMock(
            return_value=150
        )

        self.engine.total_guesses = MagicMock(
            return_value=12
        )

        self.engine.statistics.record_completed_game = MagicMock()

        self.engine.record_statistics()

        self.engine.statistics.record_completed_game.assert_called_once_with(
            won=True,
            score=750,
            streak=4,
            play_time=150,
            letters_guessed=12,
            hints_used=2,
            difficulty=self.engine.difficulty.name,
            mode=self.engine.game_mode.value,
        )

    def test_update_player_profile_win(self):

        self.engine.game_won = True
        self.engine.score = 900

        self.engine.update_player_profile()

        self.assertEqual(
            self.engine.player.score,
            900
        )

        self.assertEqual(
            self.engine.player.games_played,
            1
        )

        self.assertEqual(
            self.engine.player.games_won,
            1
        )

        self.assertEqual(
            self.engine.player.games_lost,
            0
        )

    def test_update_player_profile_loss(self):

        self.engine.game_won = False

        self.engine.update_player_profile()

        self.assertEqual(
            self.engine.player.games_played,
            1
        )

        self.assertEqual(
            self.engine.player.games_lost,
            1
        )

    def test_save_statistics(self):

        self.engine.statistics.save = MagicMock()

        self.engine.save_statistics()

        self.engine.statistics.save.assert_called_once()

    def test_finalize_results(self):

        self.engine.update_player_profile = MagicMock()

        self.engine.record_statistics = MagicMock()

        self.engine.save_statistics = MagicMock()

        self.engine.finalize_results()

        self.engine.update_player_profile.assert_called_once()

        self.engine.record_statistics.assert_called_once()

        self.engine.save_statistics.assert_called_once()

    def test_handle_victory(self):

        self.engine.player.name = "Alex"
        self.engine.word = "PYTHON"
        self.engine.score = 800

        self.engine.elapsed_time = MagicMock(
            return_value=95
        )

        self.engine.finalize_results = MagicMock()

        self.engine.renderer.draw_victory_screen = MagicMock()

        self.engine.renderer.wait_for_key = MagicMock()

        self.engine.handle_victory()

        self.engine.finalize_results.assert_called_once()

        self.engine.renderer.draw_victory_screen.assert_called_once_with(
            player="Alex",
            word="PYTHON",
            score=800,
            elapsed_time=95,
        )

        self.engine.renderer.wait_for_key.assert_called_once()

    def test_handle_defeat(self):

        self.engine.player.name = "Alex"
        self.engine.word = "PYTHON"
        self.engine.score = 100

        self.engine.finalize_results = MagicMock()

        self.engine.renderer.draw_game_over_screen = MagicMock()

        self.engine.renderer.wait_for_key = MagicMock()

        self.engine.handle_defeat()

        self.engine.finalize_results.assert_called_once()

        self.engine.renderer.draw_game_over_screen.assert_called_once_with(
            player="Alex",
            word="PYTHON",
            score=100,
        )

        self.engine.renderer.wait_for_key.assert_called_once()

    def test_show_statistics(self):

        report = {
            "Games": 10,
            "Wins": 8,
        }

        self.engine.statistics.generate_report = MagicMock(
            return_value=report
        )

        self.engine.renderer.draw_statistics_screen = MagicMock()

        self.engine.renderer.wait_for_key = MagicMock()

        self.engine.show_statistics()

        self.engine.renderer.draw_statistics_screen.assert_called_once_with(
            report
        )

        self.engine.renderer.wait_for_key.assert_called_once() 

class TestEngineSaveLoad(unittest.TestCase):

    def setUp(self):
        self.engine = Engine()

    def test_build_save_data(self):

        self.engine.player.name = "Alex"
        self.engine.difficulty = Difficulty.HARD
        self.engine.game_mode = GameMode.TIMED
        self.engine.word = "PYTHON"
        self.engine.category = "Programming"
        self.engine.display_word = "P _ _ _ _ _"
        self.engine.correct_letters = {"P"}
        self.engine.wrong_letters = {"A", "B"}
        self.engine.score = 500
        self.engine.hangman_stage = 2
        self.engine.remaining_lives = 6

        self.engine.elapsed_time = MagicMock(
            return_value=75
        )

        data = self.engine.build_save_data()

        self.assertEqual(
            data["player_name"],
            "Alex"
        )

        self.assertEqual(
            data["difficulty"],
            "HARD"
        )

        self.assertEqual(
            data["game_mode"],
            "TIMED"
        )

        self.assertEqual(
            data["word"],
            "PYTHON"
        )

        self.assertEqual(
            data["category"],
            "Programming"
        )

        self.assertEqual(
            data["display_word"],
            "P _ _ _ _ _"
        )

        self.assertEqual(
            data["correct_letters"],
            ["P"]
        )

        self.assertEqual(
            data["wrong_letters"],
            ["A", "B"]
        )

        self.assertEqual(
            data["score"],
            500
        )

        self.assertEqual(
            data["hangman_stage"],
            2
        )

        self.assertEqual(
            data["remaining_lives"],
            6
        )

        self.assertEqual(
            data["elapsed_time"],
            75
        )

    def test_save_game_success(self):

        self.engine.build_save_data = MagicMock(
            return_value={"score": 100}
        )

        self.engine.save_system.save_game = MagicMock(
            return_value=True
        )

        self.engine.renderer.success = MagicMock()
        self.engine.renderer.error = MagicMock()

        result = self.engine.save_game()

        self.assertTrue(result)

        self.engine.save_system.save_game.assert_called_once_with(
            {"score": 100}
        )

        self.engine.renderer.success.assert_called_once_with(
            "Game saved successfully"
        )

        self.engine.renderer.error.assert_not_called()

    def test_save_game_failure(self):

        self.engine.build_save_data = MagicMock(
            return_value={}
        )

        self.engine.save_system.save_game = MagicMock(
            return_value=False
        )

        self.engine.renderer.success = MagicMock()
        self.engine.renderer.error = MagicMock()

        result = self.engine.save_game()

        self.assertFalse(result)

        self.engine.renderer.error.assert_called_once_with(
            "Failed to save game"
        )

    def test_load_game_success(self):

        save_data = {
            "player_name": "Alex",
            "difficulty": "EASY",
            "game_mode": "CLASSIC",
            "word": "PYTHON",
            "category": "Programming",
            "display_word": "P _ _ _ _ _",
            "correct_letters": ["P"],
            "wrong_letters": ["A"],
            "score": 250,
            "hangman_stage": 1,
            "remaining_lives": 9,
        }

        self.engine.save_system.load_game = MagicMock(
            return_value=save_data
        )

        self.engine.timer.reset = MagicMock()
        self.engine.timer.start = MagicMock()

        self.engine.renderer.success = MagicMock()

        result = self.engine.load_game()

        self.assertTrue(result)

        self.assertEqual(
            self.engine.player.name,
            "Alex"
        )

        self.assertEqual(
            self.engine.word,
            "PYTHON"
        )

        self.assertEqual(
            self.engine.category,
            "Programming"
        )

        self.assertEqual(
            self.engine.score,
            250
        )

        self.assertEqual(
            self.engine.correct_letters,
            {"P"}
        )

        self.assertEqual(
            self.engine.wrong_letters,
            {"A"}
        )

        self.engine.timer.reset.assert_called_once()

        self.engine.timer.start.assert_called_once()

        self.engine.renderer.success.assert_called_once_with(
            "Save loaded successfully"
        )

    def test_load_game_failure(self):

        self.engine.save_system.load_game = MagicMock(
            return_value={}
        )

        self.engine.renderer.warning = MagicMock()

        result = self.engine.load_game()

        self.assertFalse(result)

        self.engine.renderer.warning.assert_called_once_with(
            "No save file found"
        )

    def test_delete_save_success(self):

        self.engine.save_system.delete_save = MagicMock(
            return_value=True
        )

        self.engine.renderer.success = MagicMock()

        result = self.engine.delete_save()

        self.assertTrue(result)

        self.engine.renderer.success.assert_called_once_with(
            "Save deleted"
        )

    def test_delete_save_failure(self):

        self.engine.save_system.delete_save = MagicMock(
            return_value=False
        )

        self.engine.renderer.warning = MagicMock()

        result = self.engine.delete_save()

        self.assertFalse(result)

        self.engine.renderer.warning.assert_called_once_with(
            "No save file exists"
        )

    def test_autosave(self):

        self.engine.build_save_data = MagicMock(
            return_value={"score": 100}
        )

        self.engine.save_system.save_game = MagicMock()

        self.engine.autosave()

        self.engine.save_system.save_game.assert_called_once_with(
            {"score": 100}
        )

    def test_has_saved_game(self):

        self.engine.save_system.save_exists = MagicMock(
            return_value=True
        )

        self.assertTrue(
            self.engine.has_saved_game()
        )

        self.engine.save_system.save_exists.assert_called_once()

    def test_continue_game_success(self):

        self.engine.load_game = MagicMock(
            return_value=True
        )

        self.engine.play = MagicMock()

        result = self.engine.continue_game()

        self.assertTrue(result)

        self.assertTrue(
            self.engine.game_running
        )

        self.engine.play.assert_called_once()

    def test_continue_game_failure(self):

        self.engine.load_game = MagicMock(
            return_value=False
        )

        self.engine.play = MagicMock()

        result = self.engine.continue_game()

        self.assertFalse(result)

        self.engine.play.assert_not_called() 

class TestEngineMenus(unittest.TestCase):

    def setUp(self):
        self.engine = Engine()

    def test_create_new_game(self):

        self.engine.set_player = MagicMock()
        self.engine.set_difficulty = MagicMock()
        self.engine.set_game_mode = MagicMock()
        self.engine.start_game = MagicMock()
        self.engine.play = MagicMock()

        self.engine.create_new_game(
            player_name="Alex",
            difficulty=Difficulty.HARD,
            game_mode=GameMode.TIMED,
        )

        self.engine.set_player.assert_called_once_with(
            "Alex"
        )

        self.engine.set_difficulty.assert_called_once_with(
            Difficulty.HARD
        )

        self.engine.set_game_mode.assert_called_once_with(
            GameMode.TIMED
        )

        self.engine.start_game.assert_called_once()

        self.engine.play.assert_called_once()

    def test_pause_game_resume(self):

        self.engine.renderer.draw_pause_screen = MagicMock()

        self.engine.renderer.prompt_menu_choice = MagicMock(
            return_value="1"
        )

        self.engine.pause_game()

        self.engine.renderer.draw_pause_screen.assert_called_once()

    def test_pause_game_save(self):

        self.engine.renderer.draw_pause_screen = MagicMock()

        self.engine.renderer.prompt_menu_choice = MagicMock(
            side_effect=["2", "1"]
        )

        self.engine.save_game = MagicMock()

        self.engine.renderer.wait_for_key = MagicMock()

        self.engine.pause_game()

        self.engine.save_game.assert_called_once()

        self.engine.renderer.wait_for_key.assert_called_once()

    def test_pause_game_return_menu(self):

        self.engine.game_running = True

        self.engine.renderer.draw_pause_screen = MagicMock()

        self.engine.renderer.prompt_menu_choice = MagicMock(
            return_value="3"
        )

        self.engine.pause_game()

        self.assertFalse(
            self.engine.game_running
        )

    def test_pause_game_quit(self):

        self.engine.renderer.draw_pause_screen = MagicMock()

        self.engine.renderer.prompt_menu_choice = MagicMock(
            return_value="4"
        )

        self.engine.finish_defeat = MagicMock()

        self.engine.pause_game()

        self.engine.finish_defeat.assert_called_once()

    def test_pause_game_invalid_choice(self):

        self.engine.renderer.draw_pause_screen = MagicMock()

        self.engine.renderer.prompt_menu_choice = MagicMock(
            side_effect=["9", "1"]
        )

        self.engine.renderer.warning = MagicMock()

        self.engine.renderer.pause = MagicMock()

        self.engine.pause_game()

        self.engine.renderer.warning.assert_called_once_with(
            "Invalid option"
        )

        self.engine.renderer.pause.assert_called_once_with(
            1
        )

    def test_choose_difficulty_valid(self):

        self.assertTrue(
            self.engine.choose_difficulty("1")
        )

        self.assertEqual(
            self.engine.difficulty,
            Difficulty.EASY
        )

        self.assertTrue(
            self.engine.choose_difficulty("2")
        )

        self.assertEqual(
            self.engine.difficulty,
            Difficulty.MEDIUM
        )

        self.assertTrue(
            self.engine.choose_difficulty("3")
        )

        self.assertEqual(
            self.engine.difficulty,
            Difficulty.HARD
        )

        self.assertTrue(
            self.engine.choose_difficulty("4")
        )

        self.assertEqual(
            self.engine.difficulty,
            Difficulty.IMPOSSIBLE
        )

    def test_choose_difficulty_invalid(self):

        result = self.engine.choose_difficulty(
            "99"
        )

        self.assertFalse(result)

    def test_choose_game_mode_valid(self):

        self.assertTrue(
            self.engine.choose_game_mode("1")
        )

        self.assertEqual(
            self.engine.game_mode,
            GameMode.CLASSIC
        )

        self.assertTrue(
            self.engine.choose_game_mode("2")
        )

        self.assertEqual(
            self.engine.game_mode,
            GameMode.TIMED
        )

        self.assertTrue(
            self.engine.choose_game_mode("3")
        )

        self.assertEqual(
            self.engine.game_mode,
            GameMode.ENDLESS
        )

        self.assertTrue(
            self.engine.choose_game_mode("4")
        )

        self.assertEqual(
            self.engine.game_mode,
            GameMode.DAILY
        )

    def test_choose_game_mode_invalid(self):

        result = self.engine.choose_game_mode(
            "99"
        )

        self.assertFalse(result)

    def test_show_help(self):

        self.engine.renderer.draw_help_screen = MagicMock()

        self.engine.renderer.wait_for_key = MagicMock()

        self.engine.show_help()

        self.engine.renderer.draw_help_screen.assert_called_once()

        self.engine.renderer.wait_for_key.assert_called_once()

    def test_show_settings(self):

        self.engine.renderer.draw_settings_menu = MagicMock()

        self.engine.renderer.wait_for_key = MagicMock()

        self.engine.show_settings()

        self.engine.renderer.draw_settings_menu.assert_called_once()

        self.engine.renderer.wait_for_key.assert_called_once()

    def test_reset_progress(self):

        self.engine.reset_game = MagicMock()

        self.engine.reset_progress()

        self.engine.reset_game.assert_called_once()

        self.assertEqual(
            self.engine.player.name,
            DEFAULT_PLAYER_NAME
        )

    def test_reset_everything(self):

        self.engine.reset_progress = MagicMock()

        self.engine.statistics.reset = MagicMock()

        self.engine.scoreboard.clear = MagicMock()

        self.engine.save_system.delete_save = MagicMock()

        self.engine.reset_everything()

        self.engine.reset_progress.assert_called_once()

        self.engine.statistics.reset.assert_called_once()

        self.engine.scoreboard.clear.assert_called_once()

        self.engine.save_system.delete_save.assert_called_once()

    def test_current_state(self):

        self.engine.player.name = "Alex"
        self.engine.word = "PYTHON"
        self.engine.display_word = "P _ _ _ _ _"
        self.engine.correct_letters = {"P"}
        self.engine.wrong_letters = {"A"}
        self.engine.score = 400
        self.engine.remaining_lives = 8
        self.engine.game_running = True

        state = self.engine.current_state()

        self.assertEqual(
            state["player"],
            "Alex"
        )

        self.assertEqual(
            state["word"],
            "PYTHON"
        )

        self.assertEqual(
            state["display_word"],
            "P _ _ _ _ _"
        )

        self.assertEqual(
            state["score"],
            400
        )

        self.assertEqual(
            state["remaining_lives"],
            8
        )

        self.assertTrue(
            state["game_running"]
        ) 

class TestEngineUtilities(unittest.TestCase):

    def setUp(self):
        self.engine = Engine()

    def test_is_running_true(self):

        self.engine.game_running = True

        self.assertTrue(
            self.engine.is_running()
        )

    def test_is_running_false(self):

        self.engine.game_running = False

        self.assertFalse(
            self.engine.is_running()
        )

    def test_has_won_true(self):

        self.engine.game_won = True

        self.assertTrue(
            self.engine.has_won()
        )

    def test_has_won_false(self):

        self.engine.game_won = False

        self.assertFalse(
            self.engine.has_won()
        )

    def test_has_lost_true(self):

        self.engine.game_over = True
        self.engine.game_won = False

        self.assertTrue(
            self.engine.has_lost()
        )

    def test_has_lost_false_when_game_not_over(self):

        self.engine.game_over = False
        self.engine.game_won = False

        self.assertFalse(
            self.engine.has_lost()
        )

    def test_has_lost_false_when_player_won(self):

        self.engine.game_over = True
        self.engine.game_won = True

        self.assertFalse(
            self.engine.has_lost()
        )

    def test_guessed_letters(self):

        self.engine.correct_letters = {
            "P",
            "Y",
        }

        self.engine.wrong_letters = {
            "A",
            "Z",
        }

        letters = self.engine.guessed_letters()

        self.assertEqual(
            letters,
            ["A", "P", "Y", "Z"]
        )

    def test_guess_count(self):

        self.engine.correct_letters = {
            "A",
            "B",
        }

        self.engine.wrong_letters = {
            "C",
            "D",
            "E",
        }

        self.assertEqual(
            self.engine.guess_count(),
            5
        )

    def test_accuracy_no_guesses(self):

        self.assertEqual(
            self.engine.accuracy(),
            0.0
        )

    def test_accuracy_partial(self):

        self.engine.correct_letters = {
            "A",
            "B",
            "C",
        }

        self.engine.wrong_letters = {
            "X",
        }

        self.assertEqual(
            self.engine.accuracy(),
            75.0
        )

    def test_accuracy_all_correct(self):

        self.engine.correct_letters = {
            "A",
            "B",
            "C",
        }

        self.engine.wrong_letters = set()

        self.assertEqual(
            self.engine.accuracy(),
            100.0
        )

    def test_accuracy_all_wrong(self):

        self.engine.correct_letters = set()

        self.engine.wrong_letters = {
            "A",
            "B",
            "C",
        }

        self.assertEqual(
            self.engine.accuracy(),
            0.0
        )

    def test_str(self):

        self.engine.player.name = "Alex"
        self.engine.difficulty = Difficulty.HARD
        self.engine.game_mode = GameMode.TIMED
        self.engine.score = 900
        self.engine.game_running = True

        text = str(self.engine)

        self.assertIn(
            "Alex",
            text
        )

        self.assertIn(
            "HARD",
            text
        )

        self.assertIn(
            "TIMED",
            text
        )

        self.assertIn(
            "900",
            text
        )

    def test_repr(self):

        self.assertEqual(
            repr(self.engine),
            str(self.engine)
        )


if __name__ == "__main__":
    unittest.main() 

