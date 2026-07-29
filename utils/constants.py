# constants.py
# Global constants used throughout the game

# IMPORTANT
# This file only contains constants 
# No functions or classes belong here 

import string

# Project Information

PROJECT_NAME = "Advanced Hangman"
PROJECT_VERSION = "1.0.0"
AUTHOR = "Anay Kushwaha"

# File Paths

ASSETS_FOLDER = "assets"

DATA_FOLDER = "data"

SAVE_FOLDER = "data/saves"

EASY_WORDS_FILE = "data/easy_words.json"
MEDIUM_WORDS_FILE = "data/medium_words.json"
HARD_WORDS_FILE = "data/hard_words.json"
IMPOSSIBLE_WORDS_FILE = "data/impossible_words.json"

STATISTICS_FILE = "data/statistics.json"
SAVE_FILE = "data/saves/savegame.json"

LOGO_FILE = "assets/logo.txt"

JSON_EXTENSION = ".json"
TEXT_EXTENSION = ".txt"

# Terminal Layout

SCREEN_WIDTH = 80
MENU_WIDTH = 60
PANEL_WIDTH = 74
REPORT_WIDTH = 50

SEPARATOR = "=" * PANEL_WIDTH
THIN_SEPARATOR = "-" * PANEL_WIDTH
DOUBLE_SEPARATOR = "═" * PANEL_WIDTH

# Game Settings

MAX_HANGMAN_STAGE = 12

DEFAULT_LIVES = 12

DEFAULT_SCORE = 0
DEFAULT_HIGH_SCORE = 0

DEFAULT_STREAK = 0
DEFAULT_HINTS_USED = 0

MIN_WORD_LENGTH = 3
MAX_WORD_LENGTH = 80

MAX_PLAYER_NAME_LENGTH = 20
MAX_CATEGORY_NAME_LENGTH = 30

DEFAULT_PLAYER_NAME = "Player"

# Difficulties

DIFFICULTY_NAMES = (
    "Easy",
    "Medium",
    "Hard",
    "Impossible",
)

EASY_SCORE_MULTIPLIER = 1.0
MEDIUM_SCORE_MULTIPLIER = 1.5
HARD_SCORE_MULTIPLIER = 2.0
IMPOSSIBLE_SCORE_MULTIPLIER = 3.0

# Input

VALID_LETTERS = set(string.ascii_uppercase)

VALID_MENU_INPUT = {
    "1",
    "2",
    "3",
    "4",
    "5",
}

YES_RESPONSES = {
    "Y",
    "YES",
}

NO_RESPONSES = {
    "N",
    "NO",
}

QUIT_COMMANDS = {
    "QUIT",
    "EXIT",
    "Q",
}

SAVE_COMMAND = "SAVE"
LOAD_COMMAND = "LOAD"
HINT_COMMAND = "HINT"

# Scoring

# Base values before the difficulty multiplier is applied.

POINTS_CORRECT_GUESS = 50

POINTS_WORD_COMPLETED = 500

POINTS_GAME_WON = 1000

POINTS_FAST_FINISH = 250

POINTS_PER_UNUSED_LIFE = 75

POINTS_STREAK_BONUS = 25

POINTS_HINT_PENALTY = 150

POINTS_WRONG_GUESS = -15

POINTS_DUPLICATE_GUESS = -10

POINTS_INVALID_INPUT = 0

# Combo System

COMBO_START = 3

COMBO_BONUS = 10

MAX_COMBO_MULTIPLIER = 5

# Timer

DEFAULT_TIME_LIMIT = 300

COUNTDOWN_WARNING = 60

FAST_FINISH_TIME = 120

# Animations

TYPEWRITER_DELAY = 0.02

FAST_TYPEWRITER_DELAY = 0.008

MENU_DELAY = 0.25

WIN_DELAY = 0.05

LOSE_DELAY = 0.08

LOADING_DELAY = 0.04 

# Menus

MAIN_MENU = (
    "New Game",
    "Load Saved Game",
    "Statistics",
    "Settings",
    "Quit",
)

SETTINGS_MENU = (
    "Difficulty",
    "Game Mode",
    "Theme",
    "Reset Statistics",
    "Back",
)

STATISTICS_MENU = (
    "Lifetime Statistics",
    "High Scores",
    "Back",
)

# Game Modes

GAME_MODES = (
    "Classic",
    "Timed",
    "Endless",
    "Daily Challenge",
)

# Categories

WORD_CATEGORIES = (
    "Animals",
    "Countries",
    "Programming",
    "Movies",
    "Science",
    "History",
    "Food",
    "Space",
    "Technology",
)

# Messages

WELCOME_MESSAGE = (
    "Welcome to Advanced Hangman!"
)

GOODBYE_MESSAGE = (
    "Thank you for playing!"
)

SAVE_SUCCESS = (
    "Game saved successfully."
)

LOAD_SUCCESS = (
    "Game loaded successfully."
)

WIN_MESSAGE = (
    "Congratulations! You won!"
)

LOSS_MESSAGE = (
    "Game Over!"
)

# JSON Keys

JSON_PLAYER = "player"

JSON_SCORE = "score"

JSON_LIVES = "lives"

JSON_WORD = "word"

JSON_VISIBLE = "visible"

JSON_CORRECT = "correct_letters"

JSON_WRONG = "wrong_letters"

JSON_DIFFICULTY = "difficulty"

JSON_MODE = "mode"

JSON_TIME = "time"

JSON_HINTS = "hints_used"

# Statistics Keys

STAT_GAMES_PLAYED = "games_played"

STAT_GAMES_WON = "games_won"

STAT_GAMES_LOST = "games_lost"

STAT_TOTAL_SCORE = "total_score"

STAT_HIGHEST_SCORE = "highest_score"

STAT_TOTAL_PLAY_TIME = "total_play_time"

STAT_FASTEST_GAME = "fastest_game"

STAT_LONGEST_STREAK = "longest_streak"

STAT_WORDS_COMPLETED = "words_completed"

STAT_LETTERS_GUESSED = "letters_guessed"

STAT_HINTS_USED = "hints_used"

STAT_DIFFICULTY_STATS = "difficulty_stats"

STAT_MODE_STATS = "mode_stats" 

# Default Statistics

DEFAULT_STATISTICS = {
    "games_played": 0,
    "games_won": 0,
    "games_lost": 0,

    "highest_score": 0,
    "total_score": 0,

    "total_play_time": 0.0,
    "fastest_game": 0.0,

    "longest_streak": 0,

    "words_completed": 0,
    "letters_guessed": 0,
    "hints_used": 0,

    "difficulty_stats": {
        "Easy": {
            "played": 0,
            "won": 0,
            "lost": 0,
        },
        "Medium": {
            "played": 0,
            "won": 0,
            "lost": 0,
        },
        "Hard": {
            "played": 0,
            "won": 0,
            "lost": 0,
        },
        "Impossible": {
            "played": 0,
            "won": 0,
            "lost": 0,
        },
    },

    "mode_stats": {
        "Classic": {
            "played": 0,
            "won": 0,
            "lost": 0,
        },
        "Timed": {
            "played": 0,
            "won": 0,
            "lost": 0,
        },
        "Endless": {
            "played": 0,
            "won": 0,
            "lost": 0,
        },
        "Daily Challenge": {
            "played": 0,
            "won": 0,
            "lost": 0,
        },
    },
} 

