# constants.py 
# Global Constants used throughout the game 

# IMPORTANT 
# This file only contains constants 
# No functions or classes belong here 

import string

# PROJECT INFORMATION 

PROJECT_NAME = "Advanced Hangman"
PROJECT_VERSION = "1.0.0"
AUTHOR = "Anay Kushwaha"

# FILE PATHS 

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

# TERMINAL LAYOUT

SCREEN_WIDTH = 80

MENU_WIDTH = 60

PANEL_WIDTH = 74

SEPARATOR = "=" * PANEL_WIDTH

THIN_SEPARATOR = "-" * PANEL_WIDTH

DOUBLE_SEPARATOR = "═" * PANEL_WIDTH

# GAME SETTINGS

MAX_HANGMAN_STAGE = 12

MIN_WORD_LENGTH = 3

MAX_WORD_LENGTH = 80

MAX_CATEGORY_NAME_LENGTH = 30

# INPUT

VALID_LETTERS = set(string.ascii_uppercase)

VALID_MENU_INPUT = {
    "1",
    "2",
    "3",
    "4",
    "5"
}

YES_RESPONSES = {
    "Y",
    "YES"
}

NO_RESPONSES = {
    "N",
    "NO"
}

QUIT_COMMANDS = {
    "QUIT",
    "EXIT",
    "Q"
}

SAVE_COMMAND = "SAVE"

LOAD_COMMAND = "LOAD"

HINT_COMMAND = "HINT"

# SCORING

# These are BASE values.
# Difficulty multipliers are applied later.

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

# COMBO SYSTEM 

COMBO_START = 3

COMBO_BONUS = 10

MAX_COMBO_MULTIPLIER = 5

# TIMER  

DEFAULT_TIME_LIMIT = 300

COUNTDOWN_WARNING = 60

FAST_FINISH_TIME = 120

# ANIMATIONS 

TYPEWRITER_DELAY = 0.02

FAST_TYPEWRITER_DELAY = 0.008

MENU_DELAY = 0.25

WIN_DELAY = 0.05

LOSE_DELAY = 0.08

LOADING_DELAY = 0.04

# MENUS

MAIN_MENU = (
    "New Game",
    "Load Saved Game",
    "Statistics",
    "Settings",
    "Quit"
)

SETTINGS_MENU = (
    "Difficulty",
    "Game Mode",
    "Theme",
    "Reset Statistics",
    "Back"
)

STATISTICS_MENU = (
    "Lifetime Statistics",
    "High Scores",
    "Back"
)

# GAME MODES

GAME_MODES = (
    "Classic",
    "Timed",
    "Endless",
    "Daily Challenge"
)

# CATEGORIES

WORD_CATEGORIES = (
    "Animals",
    "Countries",
    "Programming",
    "Movies",
    "Science",
    "History",
    "Food",
    "Space",
    "Technology"
)

# MESSAGES

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

# DEFAULT PLAYER

DEFAULT_PLAYER_NAME = "Player"

# JSON KEYS

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

# STATISTICS KEYS

STAT_GAMES_PLAYED = "games_played"

STAT_GAMES_WON = "games_won"

STAT_GAMES_LOST = "games_lost"

STAT_TOTAL_SCORE = "total_score"

STAT_HIGH_SCORE = "high_score"

STAT_FASTEST_WIN = "fastest_win"

STAT_LONGEST_STREAK = "longest_streak"

STAT_TOTAL_GUESSES = "total_guesses"

STAT_CORRECT_GUESSES = "correct_guesses"

STAT_WRONG_GUESSES = "wrong_guesses"