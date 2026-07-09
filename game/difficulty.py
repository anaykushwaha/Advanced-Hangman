# difficulty.py 
# Contains every difficulty preset used by the Advanced-Hangman game 

# Other modules should NOT hardcode values such as lives, 
# hint penalties, or score multipliers 
# Always retrieve them from DifficultyManager 

from dataclasses import dataclass 
from enum import Enum 
from typing import Dict 

class Difficulty(Enum): 
    EASY = "Easy" 
    MEDIUM = " Medium" 
    HARD = "Hard" 
    IMPOSSIBLE = "Impossible" 


@dataclass(frozen=True) 
class DifficultySettings: 
    # Stores all configurable settings for a difficulty 

    name: str 
    max_lives: int 
    score_multiplier: float 
    hint_penalty: int 
    hints_allowed: int 
    allow_duplicate_hint: bool 
    word_file: str 
    description: str 

class DifficultyManager: 
    # Central difficulty controller 

    _DIFFICULTIES: Dict[Difficulty, DifficultySettings] = {
        Difficulty.EASY: DifficultySettings(
            name="Easy",
            max_lives=12,
            score_multiplier=1.0,
            hint_penalty=50,
            hints_allowed=5,
            allow_duplicate_hint=False,
            word_file="data/easy_words.json",
            description=(
                "Perfect for beginners.\n"
                "Plenty of lives and several hints."
            ),
        ),

        Difficulty.MEDIUM: DifficultySettings(
            name="Medium",
            max_lives=10,
            score_multiplier=1.5,
            hint_penalty=100,
            hints_allowed=3,
            allow_duplicate_hint=False,
            word_file="data/medium_words.json",
            description=(
                "Balanced difficulty.\n"
                "Average word complexity."
            ),
        ),

        Difficulty.HARD: DifficultySettings(
            name="Hard",
            max_lives=8,
            score_multiplier=2.0,
            hint_penalty=150,
            hints_allowed=2,
            allow_duplicate_hint=False,
            word_file="data/hard_words.json",
            description=(
                "Longer words.\n"
                "Fewer lives.\n"
                "Higher rewards."
            ),
        ),

        Difficulty.IMPOSSIBLE: DifficultySettings(
            name="Impossible",
            max_lives=6,
            score_multiplier=3.5,
            hint_penalty=300,
            hints_allowed=0,
            allow_duplicate_hint=False,
            word_file="data/impossible_words.json",
            description=(
                "No hints.\n"
                "Very difficult vocabulary.\n"
                "Highest score multiplier."
            ),
        ),
    }

    _current = Difficulty.MEDIUM 

    @classmethod 
    def set_difficulty(cls, difficulty: Difficulty) -> None: 
        # Set the current difficulty 

        cls._current = difficulty 

    
    @classmethod 
    def get_settings(cls) -> DifficultySettings: 
        # Returns the settings object for the current difficulty 

        return cls._DIFFICULTIES[cls._current] 
    

    @classmethod 
    def get(cls, difficulty: Difficulty) -> DifficultySettings: 
        # Returns settings for a specific difficulty 

        return cls._DIFFICULTIES[difficulty] 
    

    @classmethod 
    def get_all(cls): 
        # Returns all difficulties 

        return list(cls._DIFFICULTIES.values()) 
    
    @classmethod 
    def get_names(cls): 
        # Returns a list of difficulty names 

        return [
            difficulty.value 
            for difficulty in Difficulty 
        ]
    

    @classmethod 
    def from_string(cls, text: str) -> Difficulty: 
        # Converts a string into a Difficulty enum 
        # Also raises ValueError if invalid 

        text = text.strip().lower() 

        for difficulty in Difficulty: 
            if difficulty.value.lower() == text: 
                return difficulty 
        
        raise ValueError(
            f"Unknown difficulty: {text}" 
        )
    
    
    @classmethod 
    def print_difficulties(cls) -> None: 
        # Prints all available difficulties 

        print ("=" * 60) 
        print ("AVAILABLE DIFFICULTIES") 
        print ("=" * 60) 

        for difficulty in Difficulty: 
            settings = cls.get(difficulty) 

            print (f"\n{settings.name}") 
            print ("-" * len(settings.name)) 

            print (settings.description) 

            print(f"Lives            : {settings.max_lives}")
            print(f"Hints            : {settings.hints_allowed}")
            print(f"Hint Penalty     : {settings.hint_penalty}")
            print(
                f"Score Multiplier : x{settings.score_multiplier}"
            )

            print ("=" * 60) 

    
    @classmethod 
    def reset(cls) -> None: 
        # Resets to default difficulty 

        cls._current = Difficulty.MEDIUM 