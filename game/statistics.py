# statistics.py 
# Manages lifetime player statistics for the game 

# Tracks: 
# 1. Games played 
# 2. Wins / Losses 
# 3. Win percentage 
# 4. Highest score 
# 5. Longest streak 
# 6. Fastest Completion 
# 7. Total play time 
# 8. Letters guessed 
# 9. Words completed 

# Statistics are also stored in the JSON files 

from __future__ import annotations 
from pathlib import Path 
from typing import Any 
from utils.constants import (
    STATISTICS_FILE, 
    DEFAULT_STATISTICS, 
)
from utils.file_manager import FileManager 

class Statistics: 
    # Stores and manages lifetime player statistics 

    def __init__(self) -> None: 
        self.file_path = Path(STATISTICS_FILE) 
        self.data: dict[str, Any] = DEFAULT_STATISTICS.copy() 

        self.load() 
    

    ## Loading / Saving 

    def load(self) -> None: 
        # Loads statistics from disk 

        if not FileManager.exists(self.file_path): 
            self.save() 
            return 
        
        try: 
            loaded = FileManager.load_json(self.file_path) 

            if isinstance(loaded, dict): 
                self.data.update(loaded) 
            
        except Exception: 
            self.data = DEFAULT_STATISTICS.copy() 
            self.save() 
    
    def save(self) -> None: 
        # Saves statistics to disk 

        FileManager.save_json(
            self.file_path, 
            self.data 
        ) 
    

    ## Reset 

    def reset(self) -> None: 
        # Resets every statistic 

        self.data = DEFAULT_STATISTICS.copy() 
        self.save() 
    

    ## Getters 

    def games_played(self) -> int: 
        return self.data["games_played"] 
    
    def games_won(self) -> int: 
        return self.data["games_won"] 
    
    def games_lost(self) -> int: 
        return self.data["games_lost"]
    
    def highest_score(self) -> int:
        return self.data["highest_score"]

    def total_score(self) -> int:
        return self.data["total_score"]

    def total_play_time(self) -> float:
        return self.data["total_play_time"]

    def longest_streak(self) -> int:
        return self.data["longest_streak"]

    def words_completed(self) -> int:
        return self.data["words_completed"]

    def total_letters_guessed(self) -> int:
        return self.data["letters_guessed"]

    def hints_used(self) -> int:
        return self.data["hints_used"]

    def fastest_game(self) -> float:
        return self.data["fastest_game"] 
    

    ## Basic increment functions 

    def add_game_played(self) -> None:
        self.data["games_played"] += 1

    def add_game_won(self) -> None:
        self.data["games_won"] += 1

    def add_game_lost(self) -> None:
        self.data["games_lost"] += 1

    def add_word_completed(self) -> None:
        self.data["words_completed"] += 1

    def add_letter_guess(self) -> None:
        self.data["letters_guessed"] += 1

    def add_hint_used(self) -> None:
        self.data["hints_used"] += 1

    def add_play_time(self, seconds: float) -> None:
        self.data["total_play_time"] += seconds

    def add_score(self, score: int) -> None:
        self.data["total_score"] += score

        if score > self.data["highest_score"]:
            self.data["highest_score"] = score
    

    ## Record functions 

    def update_fastest_game(self, seconds: float) -> None: 
        # Stores fastes completion time 

        current = self.data["fastest_game"] 

        if current == 0: 
            self.data["fastest_game"] = seconds 
            return 
        
        if seconds < current: 
            self.data["fastest_game"] = seconds 
    
    def update_longest_streak(self, streak: int) -> None: 
        if streak > self.data["longest_streak"]: 
            self.data["longest_streak"] = streak 
    

    ## Calculated statistics 

    def win_percentage(self) -> float: 
        # Returns the player's overall win percentage 

        if self.data["games_played"] == 0: 
            return 0.0 
        
        return round(
            (self.data["games_won"] / self.data["games_played"]) * 100 
        ) 
    
    def average_score(self) -> float: 
        # Returns the player's average score per game 

        if self.data["games_played"] == 0: 
            return 0.0 
        
        return round(
            self.data["total_score"] / self.data["games_played"] 
        ) 
    
    def average_game_time(self) -> float: 
        # Returns the average duration of completed games 

        if self.data["games_played"] == 0: 
            return 0.0 
        
        return round( 
            self.data["total_play_time"] / self.data["games_played"], 2 
        ) 
    
    def average_letters_per_game(self) -> float: 
        # Returns the average number of guessed letters 

        if self.data["games_played"] == 0: 
            return 0.0 
        
        return round( 
            self.data["letters_guessed"] / self.data["games_played"], 2 
        ) 
    
    
    ## Difficulty statistics 

    def add_difficulty_game(self, difficulty: str) -> None: 
        # Record a complete game for the given difficulty 

        difficulty = difficulty.title() 

        if difficulty not in self.data["difficulty_stats"]: 
            self.data["difficulty_stats"][difficulty] = {
                "played": 0,
                "won": 0,
                "lost": 0
            } 
        
        self.data["difficulty_stats"][difficulty]["[played"] += 1 

    def add_difficulty_win(self, difficulty: str) -> None: 
        difficulty = difficulty.title() 

        if difficulty not in self.data["difficulty_stats"]: 
            self.add_difficulty_game(difficulty) 

        self.data["difficulty_stats"][difficulty]["won"] += 1 
    
    def add_difficulty_loss(self, difficulty: str) -> None: 
        difficulty = difficulty.title() 

        if difficulty not in self.data["difficulty_stats"]: 
            self.add_difficulty_game(difficulty) 
        
        self.data["difficulty_stats"][difficulty]["lost"] += 1 

    
    ## Game mode statistics 

    def add_game_mode(self, mode: str) -> None: 
        mode = mode.title() 

        if mode not in self.data["mode_stats"]: 
            self.data["mode_stats"][mode] = {
                "played": 0, 
                "won": 0, 
                "lost": 0 
            } 
        
        self.data["mode_stats"][mode]["played"] += 1 
    
    def add_mode_win(self, mode: str) -> None: 
        mode = mode.title() 

        if mode not in self.data["mode_stats"]: 
            self.add_game_mode(mode) 
        
        self.data["mode_stats"][mode]["won"] += 1 
    
    def add_mode_loss(self, mode: str) -> None: 
        mode = mode.tite() 

        if mode not in self.data["mode_stats"]: 
            self.add_mode_game(mode) 
        
        self.data["mode_stats"][mode]["lost"] += 1 
    

    ## Full game processing 

    def record_completed_game(
            self,
        *,
        won: bool,
        score: int,
        streak: int,
        play_time: float,
        letters_guessed: int,
        hints_used: int,
        difficulty: str,
        mode: str 
    ) -> None: 
        # Records every statistic generated after a completed game 

        self.add_game_played() 

        if won: 
            self.add_game_won() 
        else: 
            self.add_game_lost() 
        
        self.add_score(score) 
        self.add_play_time(play_time) 
        self.data["letters_guessed"] += letters_guessed 
        self.data["hints_used"] += hints_used 
        self.add_word_completed() 
        self.update_longest_streak(streak) 
        self.update_fastest_game(play_time)
        self.add_difficulty_game(difficulty)

        if won:
            self.add_difficulty_win(difficulty)
        else:
            self.add_difficulty_loss(difficulty)

        self.add_mode_game(mode)

        if won:
            self.add_mode_win(mode)
        else:
            self.add_mode_loss(mode)

        self.save() 

    
    ## Formatting helpers 

    @staticmethod 
    def format_time(seconds: float) -> str: 
        # Converts seconds into HH:MM:SS 

        total_seconds = int(seconds) 
        hours = total_seconds // 3600 
        minutes = (total_seconds % 3600) // 60 
        secs = total_seconds % 60 

    
    ## Report generation 

    def generate_report(self) -> list[str]: 
        # Returns a formatted statistics report that can be displayed by the renderer 

        report = [
             "=" * 50,
            "LIFETIME STATISTICS",
            "=" * 50,
            "",
            f"Games Played       : {self.games_played()}",
            f"Games Won          : {self.games_won()}",
            f"Games Lost         : {self.games_lost()}",
            f"Win Percentage     : {self.win_percentage():.2f}%",
            "",
            f"Highest Score      : {self.highest_score()}",
            f"Total Score        : {self.total_score()}",
            f"Average Score      : {self.average_score():.2f}",
            "",
            f"Words Completed    : {self.words_completed()}",
            f"Letters Guessed    : {self.total_letters_guessed()}",
            f"Hints Used         : {self.hints_used()}",
            "",
            f"Longest Streak     : {self.longest_streak()}",
            f"Fastest Game       : {self.format_time(self.fastest_game())}",
            f"Average Game Time  : {self.format_time(self.average_game_time())}",
            f"Total Play Time    : {self.format_time(self.total_play_time())}",
            "",
            "=" * 50,
            "Difficulty Statistics",
            "=" * 50,
        ]

        for difficulty, values in self.data["difficulty_stats"].items():
            report.append(
                f"{difficulty:<12}"
                f" Played: {values['played']:<3}"
                f" Won: {values['won']:<3}"
                f" Lost: {values['lost']:<3}"
            )

        report.extend([
            "",
            "=" * 50,
            "Game Mode Statistics",
            "=" * 50,
        ])

        for mode, values in self.data["mode_stats"].items():
            report.append(
                f"{mode:<12}"
                f" Played: {values['played']:<3}"
                f" Won: {values['won']:<3}"
                f" Lost: {values['lost']:<3}"
            )

        report.append("")
        report.append("=" * 50)

        return report 
    

    ## Display 

    def print_statistics(self) -> None: 
        # Prints the formatted statistics report 

        for line in self.generate_report(): 
            print (line) 
        
    
    ## Serialization 

    def to_dict(self) -> dict[str, Any]: 
        # Returns the statistics dictionary 

        return self.data.copy() 
    
    def from_dict(self, statistics: dict[str, Any]) -> None: 
        # Restores statistics from a dictionary 

        self.data = DEFAULT_STATISTICS.copy() 

        if isinstance(statistics, dict): 
            self.data.update(statistics) 
    

    ## Utility methods 

    def clear(self) -> None: 
        # Alias for reset() 

        self.reset() 
    
    def reload(self) -> None: 
        # Reloads statistics from disk 

        self.load() 

    
    ## String representation 

    def __str__(self) -> str: 
        # Returns a short summary 

        return (
            f"Statistics(" 
            f"Played={self.games_played()}, " 
            f"Won={self.games_won()}, " 
            f"HighestScore={self.highest_score()})" 
        ) 
    
    def __repr__(self) -> str: 
        return self.__str__() 

