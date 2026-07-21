# 🎮 Advanced Hangman

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Terminal-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A feature-rich terminal-based Hangman game developed entirely in **Python** with a modular architecture, multiple game modes, persistent statistics, save/load functionality, customizable word databases, and a professional software engineering structure.

</div>

---

# 📖 Overview

Advanced Hangman is a complete reimagining of the classic Hangman game. Rather than implementing a basic word guessing program, this project was designed as a fully modular software application that demonstrates object-oriented programming, clean architecture, reusable utilities, data persistence, and maintainable code organization.

The project separates gameplay into multiple independent modules, allowing each component to focus on a single responsibility. Rendering, game logic, statistics, validation, word management, save handling, and player management are all isolated into dedicated classes, making the project significantly easier to maintain and extend.

Unlike traditional Hangman implementations, this project includes multiple gameplay modes, four difficulty levels, categorized word databases, persistent player statistics, save game support, animated terminal effects, leaderboards, and a structured testing suite.

The primary objective of this project is to demonstrate professional Python development practices while creating a polished and enjoyable terminal game.

---

# ✨ Features

## 🎲 Gameplay

- Classic Hangman gameplay
- Four difficulty levels
- Three unique game modes
- Multi-word phrase support
- Category hints
- Progressive ASCII Hangman animation
- Unlimited replayability

---

## 👤 Player System

- Custom player names
- Player profiles
- Persistent statistics
- Win streak tracking
- Best score tracking
- Accuracy calculation
- Time tracking

---

## 💾 Save System

- Save game support
- Continue previous game
- Automatic save handling
- Persistent JSON storage
- Safe loading and validation

---

## 📊 Statistics

- Games played
- Games won
- Games lost
- Win percentage
- Guess accuracy
- Total play time
- Average game duration
- Highest score
- Highest win streak
- Favourite difficulty
- Favourite game mode

---

## 🏆 Leaderboards

- High score tracking
- Sorted leaderboard
- Persistent scoreboard
- Player ranking

---

## 📚 Word Database

- 200 carefully selected words and phrases
- Four difficulty databases
- Multiple categories
- JSON-based storage
- Easily expandable
- Supports multi-word answers

---

## 🎨 User Experience

- Colored terminal output
- Animated text
- ASCII banners
- Progressive Hangman drawing
- Clear menus
- Input validation
- Clean interface

---

## 🛠 Software Engineering

- Object-Oriented Programming
- Modular architecture
- Separation of concerns
- Reusable utilities
- Comprehensive documentation
- Unit testing
- JSON persistence
- Clean project structure

---

# 🚀 Project Highlights

- **~2,700+ lines of Python code**
- **20+ Python modules**
- **200 categorized words and phrases**
- **4 difficulty levels**
- **3 game modes**
- **Persistent save system**
- **Persistent statistics**
- **Leaderboard support**
- **JSON data storage**
- **Professional modular architecture**
- **Extensive documentation**
- **Automated unit tests**

---

# 📂 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Requirements](#-requirements)
- [Running the Game](#-running-the-game)
- [Controls](#-controls)
- [Gameplay](#-gameplay)
- [Difficulty Levels](#-difficulty-levels)
- [Game Modes](#-game-modes)
- [Project Structure](#-project-structure)
- [Architecture](#-architecture)
- [Core Modules](#-core-modules)
- [Word Database](#-word-database)
- [Statistics System](#-statistics-system)
- [Save System](#-save-system)
- [Testing](#-testing)
- [Future Improvements](#-future-improvements)
- [License](#-license)
- [Author](#-author)

---

# 🎯 Project Goals

This project was created with the following objectives:

- Build a complete object-oriented Python application.
- Demonstrate clean software architecture and modular design.
- Practice file handling using JSON.
- Implement persistent player statistics and save functionality.
- Design reusable components with low coupling.
- Create a polished terminal-based user experience.
- Develop a GitHub-ready portfolio project showcasing software engineering principles.

---

# 💻 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Advanced-Hangman.git
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## 2. Navigate to the Project

```bash
cd Advanced-Hangman
```

---

## 3. (Optional) Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

This project only uses Python's Standard Library.

```bash
pip install -r requirements.txt
```

No external packages are required.

---

## 5. Launch the Game

```bash
python main.py
```

---

# 📋 Requirements

| Requirement | Version |
|-------------|---------|
| Python | 3.10 or newer |
| Operating System | Windows, macOS, Linux |
| External Packages | None |

---

# ▶️ Running the Game

Once the application starts, the Main Menu is displayed.

```
===============================
       ADVANCED HANGMAN
===============================

1. New Game
2. Continue Saved Game
3. Statistics
4. Leaderboard
5. Help
6. Settings
7. Quit
```

From here the player can navigate through every feature of the application.

---

# 🎮 Controls

The game is intentionally designed to use simple keyboard input.

| Action | Input |
|---------|-------|
| Select menu option | Number |
| Guess a letter | Alphabet key |
| Confirm selections | Enter |
| Return to menus | Enter |
| Exit application | Ctrl + C or Quit |

---

# 🎲 Gameplay

The objective of Hangman is to correctly guess every letter of a hidden word before running out of lives.

Each incorrect guess gradually draws another section of the Hangman figure.

The game ends when either:

- The player successfully guesses the complete word or phrase.
- The Hangman drawing is completed.

Unlike traditional Hangman games, this implementation supports:

- Multi-word phrases
- Category hints
- Multiple game modes
- Persistent statistics
- Save and resume functionality
- High score tracking

---

# ❤️ Lives System

Players begin each game with a fixed number of lives depending on the selected difficulty.

Every incorrect guess removes one life.

Correct guesses reveal every occurrence of that letter within the word.

Duplicate guesses are detected automatically and do not count as additional mistakes.

When all lives are lost, the full Hangman figure is displayed and the correct answer is revealed.

---

# 🔤 Word Display

Words are displayed using underscores.

Example:

```
Category: Animals

_ _ _ _ _

Wrong Letters:
A  T

Correct Letters:
E
```

For multi-word phrases, spaces are preserved.

Example:

```
_ _ _ _    _ _ _ _ _

```

This allows the player to identify the number of words while still needing to guess each individual letter.

---

# 🎯 Difficulty Levels

The game contains four progressively challenging difficulty levels.

| Difficulty | Description |
|------------|-------------|
| Easy | Common everyday words that are short and easy to recognize. |
| Medium | Longer vocabulary and simple multi-word phrases. |
| Hard | Technical terminology, geography, astronomy, programming concepts, mythology, and famous scientists. |
| Impossible | Long academic phrases, advanced scientific concepts, historical events, mathematical terminology, and world landmarks. |

Each difficulty uses its own dedicated JSON database.

---

# 🎮 Game Modes

Advanced Hangman includes three unique game modes.

## 🟢 Classic Mode

The traditional Hangman experience.

Features:

- Standard gameplay
- No time limit
- Ideal for casual play

---

## ⏱ Timed Mode

Players must solve the word before the timer expires.

Additional Features

- Countdown timer
- Faster decision making
- Time contributes to the final score

---

## 🔥 Survival Mode

Designed for experienced players.

Features

- Continuous gameplay
- Multiple consecutive rounds
- Win streak tracking
- Increasing challenge
- High-score focused gameplay

---

# 🏅 Scoring

Scores are calculated using multiple factors, including:

- Difficulty level
- Remaining lives
- Number of incorrect guesses
- Completion time
- Active game mode

Higher difficulties reward significantly more points, encouraging players to take on greater challenges.

---

# 📂 Save Progress

Players may save their progress and continue playing later.

Saved information includes:

- Player name
- Current word
- Category
- Correct letters
- Incorrect letters
- Remaining lives
- Difficulty
- Game mode
- Elapsed time

All save data is stored locally using JSON.

---

# 📈 Persistent Statistics

Every completed game contributes to long-term player statistics.

Tracked metrics include:

- Games played
- Games won
- Games lost
- Guess accuracy
- Total guesses
- Total play time
- Highest score
- Win streaks
- Favourite difficulty
- Favourite game mode

Statistics remain available even after closing the application.

---

# 📁 Project Structure

```
Advanced-Hangman/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── main.py
│
├── assets/
│   ├── __init__.py
│   ├── logo.txt
│   ├── colors.py
│   └── hangman_frames.py
│
├── game/
│   ├── __init__.py
│   ├── engine.py
│   ├── renderer.py
│   ├── player.py
│   ├── difficulty.py
│   ├── word_manager.py
│   ├── scoreboard.py
│   ├── statistics.py
│   ├── save_system.py
│   ├── validator.py
│   ├── game_mode.py
│   └── timer.py
│
├── data/
│   ├── easy_words.json
│   ├── medium_words.json
│   ├── hard_words.json
│   ├── impossible_words.json
│   ├── statistics.json
│   └── saves/
│       └── savegame.json
│
├── utils/
│   ├── __init__.py
│   ├── helper.py
│   ├── constants.py
│   ├── animations.py
│   ├── banner.py
│   └── file_manager.py
│
└── tests/
    ├── test_engine.py
    ├── test_player.py
    ├── test_validator.py
    ├── test_word_manager.py
    ├── test_scoreboard.py
    └── test_statistics.py
```

---

# 🏗 Project Architecture

Advanced Hangman follows a modular architecture where every component has a clearly defined responsibility. Instead of placing all game logic inside a single file, the application separates gameplay, rendering, persistence, validation, utilities, and player management into independent modules.

This design improves readability, maintainability, and scalability while making future feature additions significantly easier.

The project loosely follows the **Single Responsibility Principle (SRP)**, where each module focuses on one primary task.

```
                    main.py
                        │
                        ▼
                 Game Engine
                        │
 ┌──────────────┬───────────────┬───────────────┐
 │              │               │               │
 ▼              ▼               ▼               ▼
Renderer    Word Manager    Save System    Statistics
 │              │               │               │
 ▼              ▼               ▼               ▼
Assets       JSON Files     Save Files     JSON Data
```

---

# 📦 Package Overview

The project is divided into five primary packages.

| Package | Responsibility |
|----------|----------------|
| `assets` | Visual resources such as colors, banners, and Hangman drawings |
| `game` | Core gameplay logic and game management |
| `utils` | Shared helper functions and reusable utilities |
| `data` | JSON databases for words, saves, and statistics |
| `tests` | Automated unit tests |

---

# 📂 Root Directory

The root directory contains the files responsible for launching and documenting the application.

| File | Purpose |
|------|---------|
| `main.py` | Application entry point |
| `README.md` | Project documentation |
| `requirements.txt` | Python requirements |
| `.gitignore` | Git ignore rules |
| `LICENSE` | Open-source license |

---

# 📁 assets/

The **assets** package contains every visual resource used by the application.

Unlike a graphical game, terminal applications still require reusable visual components. These resources are isolated inside their own package to keep rendering logic separate from gameplay.

Contents:

| File | Description |
|------|-------------|
| `logo.txt` | ASCII title displayed during startup |
| `colors.py` | ANSI color definitions |
| `hangman_frames.py` | Progressive Hangman ASCII artwork |
| `__init__.py` | Package documentation |

---

# 🎮 game/

The **game** package contains the heart of the application.

Every gameplay mechanic is implemented here, including rendering, player management, validation, statistics, scoring, saving, timing, and word management.

| Module | Responsibility |
|---------|----------------|
| `engine.py` | Coordinates the complete gameplay loop |
| `renderer.py` | Draws every screen shown to the player |
| `player.py` | Stores player information |
| `difficulty.py` | Difficulty enumeration |
| `game_mode.py` | Game mode enumeration |
| `validator.py` | Input validation |
| `timer.py` | Tracks elapsed game time |
| `word_manager.py` | Loads and manages words |
| `statistics.py` | Player statistics |
| `scoreboard.py` | Leaderboard management |
| `save_system.py` | Save and load functionality |

---

# 🧰 utils/

The **utils** package contains helper modules that can be reused throughout the project.

These modules reduce duplicated code and provide common functionality shared by multiple parts of the application.

| Module | Responsibility |
|---------|----------------|
| `helper.py` | General helper functions |
| `constants.py` | Global constants |
| `animations.py` | Terminal animations |
| `banner.py` | Startup banners |
| `file_manager.py` | File and directory utilities |

---

# 💾 data/

The **data** directory contains every persistent resource used by the application.

Unlike the Python modules, these files store runtime information and game content.

Contents include:

- Word databases
- Statistics
- Save files

The game automatically reads from and writes to these files whenever necessary.

---

# 🧪 tests/

The **tests** package contains automated unit tests covering the major components of the project.

Each test module focuses on one system to ensure correctness and improve long-term maintainability.

Current test coverage includes:

- Player
- Engine
- Validator
- Word Manager
- Statistics
- Scoreboard

---

# 🧩 Design Principles

Several software engineering principles guided the design of this project.

### Modular Design

Each feature exists inside its own module.

This makes the code easier to understand and reduces coupling between unrelated systems.

---

### Separation of Concerns

Rendering, gameplay, persistence, validation, and utilities all exist independently.

As a result, modifying one subsystem rarely affects another.

---

### Reusability

Utility functions are centralized inside the `utils` package instead of being duplicated throughout the project.

---

### Maintainability

Smaller modules are significantly easier to debug, extend, and test than one large program.

The project intentionally avoids unnecessary complexity while remaining highly organized.

---

### Scalability

Adding new game modes, difficulties, word categories, or rendering improvements requires minimal modification to the existing codebase.

The architecture was designed to support future expansion without major restructuring. 

---

# ⚙️ Core Modules

The Advanced Hangman project is composed of several independent systems that work together to provide a complete gameplay experience. Each module has a clearly defined responsibility, making the project easier to understand, maintain, and extend.

---

# 🎮 Game Engine (`engine.py`)

The **Engine** is the heart of the application.

It coordinates every aspect of gameplay and acts as the central controller between all other modules.

### Responsibilities

- Starts new games
- Controls the gameplay loop
- Processes player guesses
- Updates player statistics
- Calculates scores
- Saves and loads games
- Detects victory and defeat
- Coordinates rendering
- Communicates with every major subsystem

The Engine intentionally contains very little display code. Instead, it delegates all visual output to the Renderer, allowing game logic and presentation to remain completely independent.

---

# 🖥 Renderer (`renderer.py`)

The Renderer is responsible for every screen shown to the player.

Instead of scattering `print()` statements throughout the project, every menu, game screen, animation, leaderboard, and statistics page is generated from this module.

### Responsibilities

- Main menu
- Difficulty selection
- Game mode selection
- Gameplay screen
- Leaderboard
- Statistics
- Help pages
- Settings pages
- End-game summaries

Separating rendering from gameplay makes future improvements significantly easier. The game's appearance can be redesigned without modifying gameplay logic.

---

# 📖 Word Manager (`word_manager.py`)

The Word Manager handles all interaction with the word databases.

Rather than hardcoding words directly into the application, every difficulty level loads its words from external JSON files.

### Responsibilities

- Load JSON databases
- Select random words
- Retrieve categories
- Validate loaded data
- Support multi-word phrases
- Allow future expansion without code changes

Current databases include:

- Easy
- Medium
- Hard
- Impossible

Together they provide over **200 categorized words and phrases**.

---

# 👤 Player (`player.py`)

The Player module stores information specific to the current player.

Instead of using scattered variables throughout the project, player-related information is encapsulated inside a dedicated class.

### Stored Information

- Player name
- Current score
- Correct guesses
- Incorrect guesses
- Remaining lives
- Current streak
- Accuracy
- Session statistics

Keeping player data inside its own object greatly improves organization and readability.

---

# 🏆 Scoreboard (`scoreboard.py`)

The Scoreboard manages persistent high scores.

Whenever a game ends, the player's performance can be added to the leaderboard.

### Features

- High score tracking
- Score sorting
- Duplicate handling
- JSON storage
- Ranking display

The leaderboard remains available between sessions.

---

# 📊 Statistics (`statistics.py`)

The Statistics module records long-term player performance.

Unlike session statistics, these values persist across multiple executions of the application.

Tracked information includes:

- Games played
- Games won
- Games lost
- Total guesses
- Correct guesses
- Incorrect guesses
- Accuracy
- Play time
- Win streaks
- Favourite difficulty
- Favourite game mode

These statistics allow players to monitor their progress over time.

---

# 💾 Save System (`save_system.py`)

The Save System allows interrupted games to be resumed later.

Instead of relying on temporary memory, complete game state information is serialized into JSON.

Saved information includes:

- Current word
- Category
- Difficulty
- Game mode
- Remaining lives
- Correct guesses
- Incorrect guesses
- Elapsed time
- Current player

This design allows a game to be restored exactly as it was before closing the application.

---

# ✅ Validator (`validator.py`)

Every player input passes through the Validator before reaching the game engine.

This prevents invalid input from affecting gameplay.

Validation includes:

- Empty input
- Multiple characters
- Duplicate guesses
- Invalid menu options
- Alphabetic characters only

Centralizing validation removes duplicated error checking throughout the project.

---

# ⏱ Timer (`timer.py`)

The Timer measures game duration.

It supports Timed Mode while also providing timing information used for statistics and score calculation.

Features include:

- Start timer
- Stop timer
- Pause timer
- Resume timer
- Elapsed time calculation
- Time formatting

---

# 🎬 Animations (`animations.py`)

Animations improve the terminal experience by making menus and transitions feel more polished.

Effects include:

- Typing animations
- Delayed printing
- Loading animations
- Countdown effects

Although entirely terminal-based, these additions create a smoother and more engaging user experience.

---

# 🛠 Utility Modules

Several supporting modules simplify the rest of the project.

## `constants.py`

Contains shared configuration values used throughout the application.

Examples include:

- Default lives
- File paths
- Scoring values
- Menu constants
- Timing constants

---

## `helper.py`

Provides reusable helper functions such as:

- Screen clearing
- Input helpers
- String formatting
- General utility functions

---

## `banner.py`

Responsible for displaying startup banners and decorative headers.

This keeps visual presentation separate from application logic.

---

## `file_manager.py`

Handles low-level file operations used throughout the project.

Responsibilities include:

- Creating directories
- Reading files
- Writing files
- JSON serialization
- Safe file handling

---

# 🔄 Module Interaction

The following diagram illustrates how the major components communicate.

```
                 main.py
                     │
                     ▼
              HangmanApplication
                     │
                     ▼
                 Game Engine
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Renderer      Word Manager    Save System
      │              │              │
      ▼              ▼              ▼
 Assets        JSON Database   Save Files

             ▼
        Statistics
             │
             ▼
      statistics.json

             ▼
        Scoreboard
             │
             ▼
       Leaderboard Data
```

The Engine acts as the coordinator for nearly every subsystem, while the remaining modules focus on one clearly defined responsibility.

This separation of concerns keeps the project organized, scalable, and significantly easier to maintain. 

---

# 🗂 Data Files

Advanced Hangman stores all persistent information using JSON. This approach keeps the project lightweight, human-readable, and easy to maintain without requiring an external database.

The application automatically loads and updates these files during gameplay.

---

# 📚 Word Databases

The game includes four independent word databases.

| File | Difficulty | Description |
|------|------------|-------------|
| `easy_words.json` | Easy | Common everyday words for beginners |
| `medium_words.json` | Medium | Longer words and simple phrases |
| `hard_words.json` | Hard | Technical vocabulary, geography, astronomy, programming, mythology and famous scientists |
| `impossible_words.json` | Impossible | Long phrases and advanced academic concepts |

Every entry contains both a word (or phrase) and its category.

Example:

```json
{
    "word": "BLACK HOLE",
    "category": "Astronomy"
}
```

Using JSON instead of hardcoding words makes expanding the game extremely easy.

Adding new words requires no code changes.

---

# 📊 Statistics Database

Player statistics are stored inside

```
data/statistics.json
```

This file is automatically updated after every completed game.

Tracked values include:

- Games Played
- Games Won
- Games Lost
- Correct Guesses
- Incorrect Guesses
- Total Guesses
- Best Score
- Total Play Time
- Win Streak
- Favourite Difficulty
- Favourite Game Mode

Because statistics are stored separately from gameplay, they remain available even after restarting the application.

---

# 💾 Save File

The Save System stores game progress inside

```
data/saves/savegame.json
```

The save file contains enough information to completely reconstruct a game.

Stored values include:

- Player Name
- Difficulty
- Game Mode
- Current Word
- Category
- Remaining Lives
- Correct Letters
- Wrong Letters
- Elapsed Time
- Current Game State

This allows players to continue exactly where they left off.

---

# 🔒 Data Validation

Every JSON file loaded by the project is validated before use.

Validation includes checking:

- File existence
- Valid JSON syntax
- Required keys
- Correct data types
- Missing values
- Empty databases

These checks reduce the likelihood of runtime errors caused by corrupted or incomplete data.

---

# 🧪 Testing

Advanced Hangman includes a dedicated automated test suite to verify the correctness of the major components.

Current test modules include:

| Test File | Purpose |
|-----------|---------|
| `test_engine.py` | Engine functionality |
| `test_player.py` | Player class |
| `test_validator.py` | Input validation |
| `test_word_manager.py` | Word loading and selection |
| `test_scoreboard.py` | Leaderboard management |
| `test_statistics.py` | Statistics calculations |

The tests are designed to verify both expected behavior and common edge cases.

---

# ▶️ Running the Tests

Execute the complete test suite using:

```bash
python -m unittest discover tests
```

Or execute an individual test file:

```bash
python -m unittest tests.test_engine
```

Running the test suite before publishing changes helps ensure that new features do not introduce regressions.

---

# 🚀 Future Improvements

Although the project is fully functional, there are many opportunities for future expansion.

Potential improvements include:

### Gameplay

- Achievement system
- Daily challenges
- Difficulty customization
- Hint system
- Bonus rounds
- Multiplayer support

---

### User Experience

- Sound effects
- Background music
- Better terminal animations
- Color themes
- Accessibility improvements

---

### Technical Improvements

- SQLite database support
- Cloud save synchronization
- Configuration file
- Plugin system
- Performance profiling
- Continuous Integration (CI)

---

### Graphical Version

A future version could replace the terminal interface with:

- Tkinter
- PyQt
- Pygame
- Custom OpenGL renderer

Because the project separates rendering from gameplay, very little game logic would need to change.

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve Advanced Hangman:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

Please ensure that:

- Existing functionality continues to work.
- New features include appropriate tests.
- Code follows the project's structure and style.

---

# 📈 What This Project Demonstrates

This project showcases practical software engineering skills including:

- Object-Oriented Programming
- Modular software architecture
- Clean code principles
- File handling
- JSON serialization
- Input validation
- Persistent storage
- Terminal UI development
- Software documentation
- Automated testing
- Version control using Git
- Repository organization

The project was intentionally designed to resemble a real software application rather than a simple programming exercise. 

