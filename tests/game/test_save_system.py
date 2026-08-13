# test_save_system.py
# Unit tests for save_system.py

import unittest
from unittest.mock import patch

from game.save_system import SaveSystem


class TestSaveSystem(unittest.TestCase):
    # Unit tests for the SaveSystem class

    def setUp(self):
        self.exists_patcher = patch(
            "utils.file_manager.FileManager.exists",
            return_value=False
        )

        self.load_patcher = patch(
            "utils.file_manager.FileManager.load_json"
        )

        self.save_patcher = patch(
            "utils.file_manager.FileManager.save_json"
        )

        self.mock_exists = self.exists_patcher.start()
        self.mock_load = self.load_patcher.start()
        self.mock_save = self.save_patcher.start()

        self.save_system = SaveSystem()

    def tearDown(self):
        patch.stopall()

    # Constructor

    def test_save_system_created(self):
        self.assertIsInstance(
            self.save_system,
            SaveSystem
        )

    # Default Save Structure

    def test_default_save_returns_dictionary(self):
        save = SaveSystem.default_save()

        self.assertIsInstance(
            save,
            dict
        )

    def test_default_save_contains_player_name(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "player_name",
            save
        )

    def test_default_save_contains_word(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "word",
            save
        )

    def test_default_save_contains_category(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "category",
            save
        )

    def test_default_save_contains_score(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "score",
            save
        )

    def test_default_save_contains_difficulty(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "difficulty",
            save
        )

    def test_default_save_contains_game_mode(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "game_mode",
            save
        )

    def test_default_save_contains_remaining_lives(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "remaining_lives",
            save
        )

    def test_default_save_contains_guessed_letters(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "guessed_letters",
            save
        )

    def test_default_save_contains_correct_letters(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "correct_letters",
            save
        )

    def test_default_save_contains_wrong_letters(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "wrong_letters",
            save
        )

    def test_default_save_contains_game_over(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "game_over",
            save
        )

    def test_default_save_contains_victory(self):
        save = SaveSystem.default_save()

        self.assertIn(
            "victory",
            save
        )

    def test_default_player_name(self):
        save = SaveSystem.default_save()

        self.assertEqual(
            save["player_name"],
            ""
        )

    def test_default_score(self):
        save = SaveSystem.default_save()

        self.assertEqual(
            save["score"],
            0
        )

    def test_default_game_over(self):
        save = SaveSystem.default_save()

        self.assertFalse(
            save["game_over"]
        )

    def test_default_victory(self):
        save = SaveSystem.default_save()

        self.assertFalse(
            save["victory"]
        )

    # Save File Status

    def test_exists_true(self):
        with patch(
            "utils.file_manager.FileManager.exists",
            return_value=True
        ):
            self.assertTrue(
                self.save_system.exists()
            )

    def test_exists_false(self):
        with patch(
            "utils.file_manager.FileManager.exists",
            return_value=False
        ):
            self.assertFalse(
                self.save_system.exists()
            )

    def test_delete_existing_save(self):
        with patch.object(
            SaveSystem,
            "exists",
            return_value=True
        ), patch.object(
            self.save_system.file_path,
            "unlink"
        ) as mocked_unlink:

            deleted = self.save_system.delete()

            self.assertTrue(deleted)

            self.assertEqual(
                mocked_unlink.call_count,
                1
            )

    def test_delete_missing_save(self):
        with patch.object(
            SaveSystem,
            "exists",
            return_value=False
        ):
            self.assertFalse(
                self.save_system.delete()
            )

    def test_create_empty_save_calls_save_json(self):
        self.save_system.create_empty_save()

        self.assertEqual(
            self.mock_save.call_count,
            1
        ) 

        # Saving

    def test_save_calls_file_manager(self):
        self.save_system.save(
            player_name="Alex",
            difficulty="Medium",
            game_mode="Classic",
            word="PYTHON",
            category="Programming",
            guessed_letters=["P", "Y"],
            correct_letters=["P", "Y"],
            wrong_letters=["A"],
            remaining_lives=8,
            score=250,
            current_streak=2,
            elapsed_time=90,
            hint_used=False,
            game_over=False,
            victory=False
        )

        self.assertEqual(
            self.mock_save.call_count,
            1
        )

    def test_save_player_name(self):
        with patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.save_system.save(
                player_name="Julia",
                difficulty="Easy",
                game_mode="Classic",
                word="APPLE",
                category="Food",
                guessed_letters=[],
                correct_letters=[],
                wrong_letters=[],
                remaining_lives=10,
                score=0,
                current_streak=0,
                elapsed_time=0,
                hint_used=False,
                game_over=False,
                victory=False
            )

            saved_data = mocked.call_args.args[1]

            self.assertEqual(
                saved_data["player_name"],
                "Julia"
            )

    def test_save_score(self):
        with patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.save_system.save(
                player_name="Alex",
                difficulty="Hard",
                game_mode="Classic",
                word="PYTHON",
                category="Programming",
                guessed_letters=[],
                correct_letters=[],
                wrong_letters=[],
                remaining_lives=5,
                score=900,
                current_streak=6,
                elapsed_time=240,
                hint_used=True,
                game_over=False,
                victory=False
            )

            saved_data = mocked.call_args.args[1]

            self.assertEqual(
                saved_data["score"],
                900
            )

    # Loading

    def test_load_existing_save(self):
        sample = SaveSystem.default_save()
        sample["player_name"] = "Alex"
        sample["score"] = 750

        with patch.object(
            SaveSystem,
            "exists",
            return_value=True
        ), patch(
            "utils.file_manager.FileManager.load_json",
            return_value=sample
        ):

            data = self.save_system.load()

            self.assertEqual(
                data["player_name"],
                "Alex"
            )

            self.assertEqual(
                data["score"],
                750
            )

    def test_load_missing_file_creates_save(self):
        with patch.object(
            SaveSystem,
            "exists",
            return_value=False
        ), patch.object(
            SaveSystem,
            "create_empty_save"
        ) as mocked_create, patch(
            "utils.file_manager.FileManager.load_json",
            return_value=SaveSystem.default_save()
        ):

            self.save_system.load()

            self.assertEqual(
                mocked_create.call_count,
                1
            )

    def test_load_invalid_dictionary(self):
        with patch.object(
            SaveSystem,
            "exists",
            return_value=True
        ), patch(
            "utils.file_manager.FileManager.load_json",
            return_value=[]
        ):

            data = self.save_system.load()

            self.assertEqual(
                data,
                SaveSystem.default_save()
            )

    def test_load_exception_returns_default(self):
        with patch.object(
            SaveSystem,
            "exists",
            return_value=True
        ), patch(
            "utils.file_manager.FileManager.load_json",
            side_effect=Exception
        ):

            data = self.save_system.load()

            self.assertEqual(
                data,
                SaveSystem.default_save()
            )

    def test_load_preserves_missing_default_fields(self):
        sample = {
            "player_name": "Alex"
        }

        with patch.object(
            SaveSystem,
            "exists",
            return_value=True
        ), patch(
            "utils.file_manager.FileManager.load_json",
            return_value=sample
        ):

            data = self.save_system.load()

            self.assertEqual(
                data["player_name"],
                "Alex"
            )

            self.assertEqual(
                data["score"],
                0
            )

            self.assertEqual(
                data["remaining_lives"],
                10
            )

    def test_reload_returns_loaded_data(self):
        sample = SaveSystem.default_save()
        sample["player_name"] = "Player"

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            data = self.save_system.reload()

            self.assertEqual(
                data["player_name"],
                "Player"
            ) 

        # Getter Methods

    def test_player_name_getter(self):
        sample = SaveSystem.default_save()
        sample["player_name"] = "Alex"

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.player_name(),
                "Alex"
            )

    def test_word_getter(self):
        sample = SaveSystem.default_save()
        sample["word"] = "PYTHON"

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.word(),
                "PYTHON"
            )

    def test_category_getter(self):
        sample = SaveSystem.default_save()
        sample["category"] = "Programming"

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.category(),
                "Programming"
            )

    def test_difficulty_getter(self):
        sample = SaveSystem.default_save()
        sample["difficulty"] = "Hard"

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.difficulty(),
                "Hard"
            )

    def test_game_mode_getter(self):
        sample = SaveSystem.default_save()
        sample["game_mode"] = "Timed"

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.game_mode(),
                "Timed"
            )

    def test_guessed_letters_getter(self):
        sample = SaveSystem.default_save()
        sample["guessed_letters"] = [
            "A",
            "B",
            "C"
        ]

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.guessed_letters(),
                ["A", "B", "C"]
            )

    def test_correct_letters_getter(self):
        sample = SaveSystem.default_save()
        sample["correct_letters"] = [
            "P",
            "Y"
        ]

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.correct_letters(),
                ["P", "Y"]
            )

    def test_wrong_letters_getter(self):
        sample = SaveSystem.default_save()
        sample["wrong_letters"] = [
            "X",
            "Z"
        ]

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.wrong_letters(),
                ["X", "Z"]
            )

    def test_score_getter(self):
        sample = SaveSystem.default_save()
        sample["score"] = 1250

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.score(),
                1250
            )

    def test_current_streak_getter(self):
        sample = SaveSystem.default_save()
        sample["current_streak"] = 8

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.current_streak(),
                8
            )

    def test_elapsed_time_getter(self):
        sample = SaveSystem.default_save()
        sample["elapsed_time"] = 340

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.elapsed_time(),
                340
            )

    def test_remaining_lives_getter(self):
        sample = SaveSystem.default_save()
        sample["remaining_lives"] = 4

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertEqual(
                self.save_system.remaining_lives(),
                4
            )

    def test_hint_used_getter(self):
        sample = SaveSystem.default_save()
        sample["hint_used"] = True

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertTrue(
                self.save_system.hint_used()
            )

    def test_game_over_getter(self):
        sample = SaveSystem.default_save()
        sample["game_over"] = True

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertTrue(
                self.save_system.game_over()
            )

    def test_victory_getter(self):
        sample = SaveSystem.default_save()
        sample["victory"] = True

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):
            self.assertTrue(
                self.save_system.victory()
            ) 

        # Updating Existing Saves

    def test_update_single_field(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ), patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.save_system.update(
                score=500
            )

            saved_data = mocked.call_args.args[1]

            self.assertEqual(
                saved_data["score"],
                500
            )

    def test_update_multiple_fields(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ), patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.save_system.update(
                score=900,
                player_name="Alex",
                current_streak=6
            )

            saved_data = mocked.call_args.args[1]

            self.assertEqual(
                saved_data["score"],
                900
            )

            self.assertEqual(
                saved_data["player_name"],
                "Alex"
            )

            self.assertEqual(
                saved_data["current_streak"],
                6
            )

    def test_update_ignores_invalid_keys(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ), patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.save_system.update(
                invalid_key=100
            )

            saved_data = mocked.call_args.args[1]

            self.assertNotIn(
                "invalid_key",
                saved_data
            )

    # Resetting Save Data

    def test_clear_progress(self):
        with patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.save_system.clear_progress()

            saved_data = mocked.call_args.args[1]

            self.assertEqual(
                saved_data,
                SaveSystem.default_save()
            )

    # Active Game Checks

    def test_has_active_game_true(self):
        sample = SaveSystem.default_save()
        sample["word"] = "PYTHON"
        sample["game_over"] = False

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertTrue(
                self.save_system.has_active_game()
            )

    def test_has_active_game_false_no_word(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertFalse(
                self.save_system.has_active_game()
            )

    def test_has_active_game_false_finished(self):
        sample = SaveSystem.default_save()
        sample["word"] = "PYTHON"
        sample["game_over"] = True

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertFalse(
                self.save_system.has_active_game()
            )

    def test_is_finished_true(self):
        sample = SaveSystem.default_save()
        sample["game_over"] = True

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertTrue(
                self.save_system.is_finished()
            )

    def test_is_finished_false(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertFalse(
                self.save_system.is_finished()
            )

    def test_is_victory_true(self):
        sample = SaveSystem.default_save()
        sample["game_over"] = True
        sample["victory"] = True

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertTrue(
                self.save_system.is_victory()
            )

    def test_is_victory_false(self):
        sample = SaveSystem.default_save()
        sample["game_over"] = True
        sample["victory"] = False

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertFalse(
                self.save_system.is_victory()
            )

    def test_is_defeat_true(self):
        sample = SaveSystem.default_save()
        sample["game_over"] = True
        sample["victory"] = False

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertTrue(
                self.save_system.is_defeat()
            )

    def test_is_defeat_false(self):
        sample = SaveSystem.default_save()
        sample["game_over"] = True
        sample["victory"] = True

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertFalse(
                self.save_system.is_defeat()
            ) 

        # Export Helpers

    def test_to_dict_returns_dictionary(self):
        sample = SaveSystem.default_save()
        sample["player_name"] = "Alex"

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            data = self.save_system.to_dict()

            self.assertIsInstance(
                data,
                dict
            )

            self.assertEqual(
                data["player_name"],
                "Alex"
            )

    def test_to_dict_returns_copy(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            data = self.save_system.to_dict()
            data["player_name"] = "Modified"

            self.assertNotEqual(
                data["player_name"],
                sample["player_name"]
            )

    def test_from_dict(self):
        sample = SaveSystem.default_save()
        sample["player_name"] = "Chris"
        sample["score"] = 2500

        with patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.save_system.from_dict(sample)

            saved_data = mocked.call_args.args[1]

            self.assertEqual(
                saved_data["player_name"],
                "Chris"
            )

            self.assertEqual(
                saved_data["score"],
                2500
            )

    def test_from_dict_invalid(self):
        with patch(
            "utils.file_manager.FileManager.save_json"
        ) as mocked:

            self.save_system.from_dict("invalid")

            saved_data = mocked.call_args.args[1]

            self.assertEqual(
                saved_data,
                SaveSystem.default_save()
            )

    # Utility Methods

    def test_reload(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            data = self.save_system.reload()

            self.assertEqual(
                data,
                sample
            )

    def test_save_game(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "from_dict"
        ) as mocked:

            result = self.save_system.save_game(sample)

            self.assertTrue(result)

            self.assertEqual(
                mocked.call_count,
                1
            )

    def test_load_game(self):
        sample = SaveSystem.default_save()
        sample["score"] = 100

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertEqual(
                self.save_system.load_game(),
                sample
            )

    def test_delete_save(self):
        with patch.object(
            SaveSystem,
            "exists",
            return_value=True
        ), patch.object(
            SaveSystem,
            "delete"
        ) as mocked:

            result = self.save_system.delete_save()

            self.assertTrue(result)

            self.assertEqual(
                mocked.call_count,
                1
            )

    def test_delete_save_when_missing(self):
        with patch.object(
            SaveSystem,
            "exists",
            return_value=False
        ):

            self.assertFalse(
                self.save_system.delete_save()
            )

    def test_save_exists(self):
        with patch.object(
            SaveSystem,
            "exists",
            return_value=True
        ):

            self.assertTrue(
                self.save_system.save_exists()
            )

    # String Representation

    def test_string_representation(self):
        sample = SaveSystem.default_save()
        sample["player_name"] = "Alex"
        sample["difficulty"] = "Hard"
        sample["game_mode"] = "Classic"
        sample["score"] = 750
        sample["game_over"] = False

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            text = str(self.save_system)

            self.assertIn(
                "SaveSystem",
                text
            )

            self.assertIn(
                "Alex",
                text
            )

    def test_repr(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertEqual(
                repr(self.save_system),
                str(self.save_system)
            )

    # Edge Cases

    def test_large_score(self):
        sample = SaveSystem.default_save()
        sample["score"] = 99999999

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertEqual(
                self.save_system.score(),
                99999999
            )

    def test_empty_player_name(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertEqual(
                self.save_system.player_name(),
                ""
            )

    def test_empty_word(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertEqual(
                self.save_system.word(),
                ""
            )

    def test_empty_letter_lists(self):
        sample = SaveSystem.default_save()

        with patch.object(
            SaveSystem,
            "load",
            return_value=sample
        ):

            self.assertEqual(
                self.save_system.correct_letters(),
                []
            )

            self.assertEqual(
                self.save_system.wrong_letters(),
                []
            )


if __name__ == "__main__":
    unittest.main() 

