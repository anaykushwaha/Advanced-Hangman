# game_mode.py 
# Defines every game mode available in Advanced Hangman 

# Game modes are separate from difficulty 
# Example: 
# Hard + Classic 
# Easy + Endless 
# Impossible + Timed 

from dataclasses import dataclass
from enum import Enum
from typing import Dict


class GameMode(Enum):
    CLASSIC = "Classic"
    TIMED = "Timed"
    ENDLESS = "Endless"
    DAILY = "Daily Challenge"


@dataclass(frozen=True)
class GameModeSettings:
    # Stores every configurable property of a game mode 
    
    name: str

    description: str

    timed: bool

    endless: bool

    daily: bool

    allow_save: bool

    uses_score: bool

    time_limit: int | None


class GameModeManager:
    # Controls every available game mode 

    _MODES: Dict[GameMode, GameModeSettings] = {

        GameMode.CLASSIC: GameModeSettings(

            name="Classic",

            description=(
                "Traditional Hangman.\n"
                "Complete one word before running out of lives."
            ),

            timed=False,

            endless=False,

            daily=False,

            allow_save=True,

            uses_score=True,

            time_limit=None,
        ),

        GameMode.TIMED: GameModeSettings(

            name="Timed",

            description=(
                "Beat the clock before time runs out."
            ),

            timed=True,

            endless=False,

            daily=False,

            allow_save=True,

            uses_score=True,

            time_limit=300,
        ),

        GameMode.ENDLESS: GameModeSettings(

            name="Endless",

            description=(
                "Keep solving words until you lose.\n"
                "Your score keeps increasing."
            ),

            timed=False,

            endless=True,

            daily=False,

            allow_save=True,

            uses_score=True,

            time_limit=None,
        ),

        GameMode.DAILY: GameModeSettings(

            name="Daily Challenge",

            description=(
                "Everyone gets the same word today.\n"
                "One attempt per day."
            ),

            timed=False,

            endless=False,

            daily=True,

            allow_save=False,

            uses_score=True,

            time_limit=None,
        ),
    }

    _current = GameMode.CLASSIC

    @classmethod
    def set_mode(cls, mode: GameMode) -> None:
        # Sets the active game mode 

        cls._current = mode

    @classmethod
    def get_current(cls) -> GameMode:
        # Returns the current game mode 

        return cls._current

    @classmethod
    def get_settings(cls) -> GameModeSettings:
        # Returns the settings for the current mode 

        return cls._MODES[cls._current]

    @classmethod
    def get(cls, mode: GameMode) -> GameModeSettings:
        # Returns settings for any mode 

        return cls._MODES[mode]

    @classmethod
    def get_all(cls): 
        # Returns every mode 

        return list(cls._MODES.values())

    @classmethod
    def get_names(cls):
        # Returns all game mode names 

        return [
            mode.value
            for mode in GameMode
        ]

    @classmethod
    def from_string(cls, text: str) -> GameMode: 
        # Converts text into a GameMode enum 

        text = text.strip().lower()

        for mode in GameMode:

            if mode.value.lower() == text:
                return mode

        raise ValueError(
            f"Unknown game mode: {text}"
        )

    @classmethod
    def print_modes(cls) -> None: 
        # Prints every game mode 

        print("=" * 60)
        print("AVAILABLE GAME MODES")
        print("=" * 60)

        for mode in GameMode:

            settings = cls.get(mode)

            print(f"\n{settings.name}")
            print("-" * len(settings.name))

            print(settings.description)

            print(f"Timed       : {settings.timed}")
            print(f"Endless     : {settings.endless}")
            print(f"Daily       : {settings.daily}")
            print(f"Save Enabled: {settings.allow_save}")

            if settings.time_limit is None:
                print("Time Limit  : Unlimited")
            else:
                print(f"Time Limit  : {settings.time_limit} seconds")

        print("=" * 60)

    @classmethod
    def reset(cls) -> None: 
        # Resets to Classic mode 

        cls._current = GameMode.CLASSIC

    @classmethod
    def is_timed(cls) -> bool:
        # Returns True if the current mode uses a timer 

        return cls.get_settings().timed

    @classmethod
    def is_endless(cls) -> bool:
        # Returns True if the current mode is endless 

        return cls.get_settings().endless

    @classmethod
    def is_daily(cls) -> bool: 
        # Returns True if Daily Challenge is active 

        return cls.get_settings().daily

    @classmethod
    def save_allowed(cls) -> bool:
        # Returns whether saving is allowed 

        return cls.get_settings().allow_save

    @classmethod
    def get_time_limit(cls): 
        # Returns the active time limit 
        # Returns None if unlimited 

        return cls.get_settings().time_limit 