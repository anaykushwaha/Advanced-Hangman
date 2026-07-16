# save_system.py 
# Handles saving and loading game progress for the game 

from __future__ import annotations 
from pathlib import Path 
from typing import Any 
from utils.constants import SAVE_FILE 
from utils.file_manager import FileManager 

class SaveSystem: 
    # Handles serialization and persistence of game save files 

    def __init__(self) -> None: 
        self.file_path = Path(SAVE_FILE) 

    
    ## Save file status 

    def exists(self) -> bool: 
        # Returns True if a save file exists 

        return FileManager.exists(self.file_path) 
    
    def delete(self) -> None: 
        # Deletes the save file 

        if self.exists(): 
            self.file_path.unlink() 

    def create_empty_save(self) -> None: 
        # Creates a blank save file 

        FileManager.save_json(
            self.file_path, 
            self.default_save() 
        ) 
    

    ## Default save structure 

    @staticmethod 
    def default_save() -> dict[str, Any]: 
        # Returns the default save structure 

        return {
            "player_name": "", 
            "difficulty": "Easy", 
            "game_mode": "Classic", 
            "word": "", 
            "category": "", 
            "guessed_letters": [], 
            "correct_letters": [], 
            "wrong_letters": [], 
            "remaining_lives": 10, 
            "score": 0, 
            "current_streak": 0, 
            "elapsed_time": 0, 
            "hint_used": False, 
            "game_over": False, 
            "victory": False 
        } 
    

    ## Saving 

    def save(
            self, 
            *, 
            player_name: str, 
            difficulty: str, 
            game_mode: str, 
            word: str, 
            category: str, 
            guessed_letters: list[str], 
            correct_letters: list[str], 
            wrong_letters: list[str], 
            remaining_lives: int, 
            score: int, 
            current_streak: int, 
            elapsed_time: float, 
            hint_used: bool, 
            game_over: bool, 
            victory: bool, 
    ) -> None: 
        # Saves the current game 

        data = {
            "player_name": player_name, 
            "difficulty": difficulty, 
            "game_mode": game_mode, 
            "word": word, 
            "category": category, 
            "guessed_letters": guessed_letters, 
            "correct_letters": correct_letters, 
            "wrong_letters": wrong_letters, 
            "remaining_lives": remaining_lives, 
            "score": score, 
            "current_streak": current_streak, 
            "elapsed_time": elapsed_time, 
            "hint_used": hint_used, 
            "game_over": game_over, 
            "victory": victory 
        } 

        FileManager.save_json(
            self.file_path, 
            data 
        ) 

    
    ## Loading 

    def load(self) -> dict[str, Any]: 
        # Loads the save file 

        if not self.exists(): 
            self.create_empty_save() 
        
        try: 
            data = FileManager.load_json(self.file_path) 

            if not isinstance(data, dict): 
                return self.default_save() 
            
            default = self.default_save() 
            default.update(data) 
            return default 
        except Exception: 
            return self.default_save() 
    
    
    ## Quick access functions 

    def player_name(self) -> str: 
        return self.load()["player_name"] 

    def word(self) -> str: 
        return self.load()["word"] 

    def category(self) -> str: 
        return self.load()["category"] 

    def difficulty(self) -> str: 
        return self.load()["difficulty"] 

    def game_mode(self) -> str: 
        return self.load()["game_mode"] 

    def guessed_letters(self) -> list[str]: 
        return self.load()["guessed_letters"] 

    def correct_letters(self) -> list[str]: 
        return self.load()["correct_letters"] 

    def wrong_letters(self) -> list[str]: 
        return self.load()["wrong_letters"] 

    def score(self) -> int: 
        return self.load()["score"] 
    
    def current_streak(self) -> int: 
        return self.load()["current_streak"] 

    def elapsed_time(self) -> float: 
        return self.load()["elapsed_time"] 

    def remaining_lives(self) -> int: 
        return self.load()["remaining_lives"] 

    def hint_used(self) -> bool: 
        return self.load()["hint_used"] 

    def game_over(self) -> bool: 
        return self.load()["game_over"] 

    def victory(self) -> bool: 
        return self.load()["victory"] 
    

    ## Updating existing saves 

    def update(self, **changes: Any) -> None: 
        # Updates selected fields of the current save without overwriting the remaining data 

        data = self.load() 

        for key, value in changes.items(): 
            if key in data: 
                data[key] = value 
        
        FileManager.save_json(
            self.file_path, 
            data 
        ) 
    

    ## Resetting save data 

    def clear_progress(self) -> None: 
        # Clears the current save file 

        FileManager.save_json(
            self.file_path, 
            self.default_save() 
        ) 
    
    def has_active_game(self) -> bool: 
        # Returns True if a game is currently stored 

        data = self.load() 

        return (
            data["word"] != "" 
            and not data["game_over"] 
        ) 
    
    def is_finished(self) -> bool: 
        # Returns whether the saved game has ended 

        return self.load()["game_over"] 
    
    def is_victory(self) -> bool: 
        # Returns whether the save game ended in victory 

        data = self.load() 

        return (
            data["game_over"] 
            and data["victory"] 
        ) 
    
    def is_defeat(self) -> bool: 
        # Returns whether the saved game has ended in defeat 

        data = self.load() 

        return (
            data["game_over"] 
            and not data["victory"] 
        ) 
    

    ## Export helpers 

    def to_dict(self,) -> dict[str, Any]: 
        # Returns a copy of the save data 

        return self.load().copy() 
    
    def from_dict(self, data: dict[str, Any]) -> None: 
        # Restores save data from an existing dictionary 

        save = self.default_save() 
        if isinstance(data, dict): 
            save.update(data) 
        FileManager.save_json(
            self.file_path, 
            save 
        ) 
    

    ## Utility methods 
    
    def reload(self) -> dict[str, Any]: 
        # Reloads and returns the save data 

        return self.load() 
    
    def __str__(self) -> str: 
        # Returns a short summary of the current save 

        data = self.load() 

        return (
            "SaveSystem(" 
            f"Player='{data['player_name']}', " 
            f"Difficulty='{data['difficulty']}', " 
            f"Mode='{data['game_mode']}', " 
            f"Score={data['score']}, " 
            f"GameOver={data['game_over']})" 
        ) 
    
    def __repr__(self) -> str: 
        return self.__Str__() 

