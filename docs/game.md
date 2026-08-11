# Game Folder Documentation

## Overview

The `game/` folder contains the core gameplay systems of **Advanced Hangman**. It is responsible for managing the player's game state, selecting words, validating guesses, calculating scores, tracking statistics, handling saves, managing timers, controlling difficulty and game modes, and rendering the game's terminal interface.

The central component of this folder is `engine.py`. The engine coordinates the other game modules and controls the overall gameplay flow.

The modules are intentionally separated by responsibility. Each module handles a specific part of the game rather than placing all functionality inside one large class.

## Folder Structure

```text
game/
├── __init__.py
├── engine.py
├── renderer.py
├── player.py
├── difficulty.py
├── word_manager.py
├── scoreboard.py
├── statistics.py
├── save_system.py
├── validator.py
├── game_mode.py
└── timer.py
```

## Architectural Role

The `game/` folder acts as the application's main gameplay layer.

A simplified relationship between the major systems is:

```text
                    Engine
                      │
        ┌─────────────┼─────────────┐
        │             │             │
      Player       WordManager   Validator
        │             │             │
        └─────────────┼─────────────┘
                      │
                 ScoreBoard
                      │
                 Statistics
                      │
                 SaveSystem
                      │
                   Timer
                      │
                GameMode /
                Difficulty
                      │
                  Renderer
                      │
                   Terminal
```

The engine coordinates these systems rather than duplicating their responsibilities.

## `__init__.py`

### Purpose

The `__init__.py` file identifies `game/` as a Python package and allows its modules to be imported throughout the project.

### Responsibilities

It provides the package boundary required for imports such as:

```python
from game.engine import Engine
from game.player import Player
from game.validator import Validator
```

The file should remain lightweight and should not contain substantial gameplay logic.

## `engine.py`

### Purpose

`engine.py` contains the `Engine` class, which is the central controller of Advanced Hangman.

The engine coordinates the game's major subsystems and manages the complete gameplay lifecycle from game initialization through victory or defeat.

### Main Responsibilities

The engine manages:

* Player initialization.
* Difficulty selection.
* Game-mode selection.
* Word loading.
* Display-word generation.
* Guess processing.
* Correct and incorrect guesses.
* Lives.
* Hangman stages.
* Score updates.
* Game state.
* Timers.
* Rendering.
* Save and load operations.
* Statistics recording.
* Victory handling.
* Defeat handling.
* Menu-related game setup.

### Important State

The engine maintains information such as:

```text
Player
Difficulty
Game Mode
Word
Category
Display Word
Correct Letters
Wrong Letters
Score
Hangman Stage
Remaining Lives
Game Running
Game Won
Game Over
```

### Gameplay Flow

A typical game follows this sequence:

```text
Engine created
      ↓
Player / difficulty / mode selected
      ↓
New word loaded
      ↓
Timer starts
      ↓
Gameplay screen rendered
      ↓
Player enters guess
      ↓
Guess validated
      ↓
Correct or incorrect guess processed
      ↓
Game state updated
      ↓
Check victory / defeat
      ↓
Repeat until game ends
      ↓
Record statistics
      ↓
Update player
      ↓
Display result
```

### Design Principle

`Engine` should coordinate other systems rather than reimplement their functionality.

For example, it should ask `Validator` to validate a letter rather than containing its own validation rules.

Likewise, it should use `WordManager` to obtain words and `Renderer` to display the game.

## `renderer.py`

### Purpose

`renderer.py` is responsible for the terminal interface of Advanced Hangman.

It converts game-state information supplied by the engine into readable and polished terminal output.

### Main Responsibilities

The renderer handles:

* Clearing the terminal.
* Titles and subtitles.
* Menus.
* Colored messages.
* Hangman frames.
* Hidden words.
* Categories.
* Difficulty information.
* Scores.
* Lives.
* Timers.
* Player information.
* Correct and incorrect letters.
* Gameplay screens.
* Pause screens.
* Help screens.
* Statistics screens.
* Leaderboards.
* Victory screens.
* Game-over screens.
* Dialog boxes.
* Credits.
* Goodbye screens.

### Separation From Gameplay

The renderer should not decide whether the player has won or lost.

Instead:

```text
Engine determines game state
        ↓
Engine sends state to Renderer
        ↓
Renderer displays the state
```

This keeps presentation logic separate from gameplay logic.

### Dependencies

The renderer uses resources from:

```text
assets.colors
assets.hangman_frames
utils.animations
utils.banner
utils.constants
utils.helper
```

## `player.py`

### Purpose

`player.py` represents the player participating in the game.

The `Player` class stores information that belongs specifically to an individual player.

### Typical Responsibilities

The player system tracks information such as:

* Player name.
* Score.
* Games played.
* Games won.
* Games lost.
* Current streak.
* Hints used.
* Other player-specific statistics supported by the project.

### Design Principle

`Player` represents **who is playing**, while `Engine` represents **what is currently happening in the game**.

For example:

```text
Player
  └── Name
  └── Score
  └── Wins
  └── Losses
  └── Streak

Engine
  └── Current word
  └── Current guesses
  └── Current lives
  └── Current game state
```

This separation prevents player information from becoming mixed with temporary puzzle state.

## `difficulty.py`

### Purpose

`difficulty.py` defines all difficulty levels available in Advanced Hangman.

The project currently supports:

```text
Easy
Medium
Hard
Impossible
```

### Main Components

The module contains:

* `Difficulty`
* `DifficultySettings`
* `DifficultyManager`

### `Difficulty`

The `Difficulty` enum provides standardized difficulty identifiers.

This prevents different parts of the project from using inconsistent strings.

### `DifficultySettings`

`DifficultySettings` stores the configuration associated with a difficulty.

Settings include:

* Difficulty name.
* Maximum lives.
* Score multiplier.
* Hint penalty.
* Number of hints allowed.
* Duplicate-hint behavior.
* Word-file path.
* Description.

### `DifficultyManager`

The manager provides centralized access to difficulty configurations.

Other modules should retrieve difficulty information from `DifficultyManager` instead of hardcoding values.

For example:

```text
Difficulty
    ↓
DifficultyManager
    ↓
DifficultySettings
    ↓
Engine / WordManager / ScoreBoard
```

### Design Principle

Game rules affected by difficulty should be centralized here.

This makes adding or modifying a difficulty much easier.

## `word_manager.py`

### Purpose

`word_manager.py` manages the game's word database and puzzle selection.

It provides the engine with words appropriate for the selected difficulty.

### Main Responsibilities

The word manager handles tasks such as:

* Loading word data.
* Selecting random words.
* Associating words with categories.
* Creating hidden-word displays.
* Managing word-related information.
* Supporting difficulty-specific word files.

### Word Selection Flow

```text
Engine
  ↓
WordManager
  ↓
Difficulty
  ↓
Correct word database
  ↓
Random word
  ↓
Engine
```

### Display Word

The word manager can also construct the visible representation of a word.

For example:

```text
Actual word:
PYTHON

No guesses:
_ _ _ _ _ _

Guessed P and T:
P _ T _ _ _
```

The engine stores the current guesses, while the word manager handles the transformation into a display representation.

## `scoreboard.py`

### Purpose

`scoreboard.py` manages score calculation and scoring-related rules.

It prevents score formulas from being scattered throughout the engine.

### Responsibilities

The scoreboard handles operations such as:

* Correct-guess scoring.
* Word-completion rewards.
* Final-score calculations.
* Difficulty multipliers.
* Score-related player updates.
* Scoreboard clearing when appropriate.

### Relationship With Difficulty

Difficulty settings can affect scoring.

For example:

```text
Difficulty
     ↓
Score Multiplier
     ↓
ScoreBoard
     ↓
Final Score
```

### Design Principle

The engine should request score calculations from `ScoreBoard` rather than manually calculating score values.

This makes scoring rules easier to change and test.

## `statistics.py`

### Purpose

`statistics.py` manages long-term game statistics.

Unlike the engine's temporary game state, statistics persist across completed games.

### Responsibilities

The statistics system handles information such as:

* Games played.
* Wins.
* Losses.
* Win rate.
* Scores.
* Streak information.
* Playing time.
* Letters guessed.
* Hints used.
* Difficulty-related statistics.
* Game-mode statistics.

### Main Operations

The statistics system supports operations such as:

```text
Record completed game
        ↓
Update statistics
        ↓
Save statistics
        ↓
Generate report
```

### Separation From Player

Player statistics and global game statistics can overlap, but they serve different purposes.

`Player` represents information about the current player profile.

`Statistics` represents persistent records of completed games and aggregate performance.

## `save_system.py`

### Purpose

`save_system.py` handles saving and loading active game progress.

It provides persistence so that a player can leave an unfinished game and potentially continue it later.

### Main Responsibilities

The save system handles:

* Save-file creation.
* Saving game state.
* Loading game state.
* Checking whether a save exists.
* Deleting saves.
* Clearing progress.
* Updating selected save fields.
* Converting save data to dictionaries.
* Restoring data from dictionaries.
* Determining whether a saved game is active.
* Determining whether a saved game is finished.
* Determining whether a saved game ended in victory or defeat.

### Save Flow

```text
Engine
  ↓
Build current game state
  ↓
SaveSystem
  ↓
FileManager
  ↓
JSON save file
```

The save system uses `utils.file_manager.FileManager` for direct file operations.

### Design Principle

`SaveSystem` manages the meaning and structure of save data, while `FileManager` handles the low-level file operations.

## `validator.py`

### Purpose

`validator.py` validates player input before it reaches the gameplay logic.

This keeps input rules centralized and prevents the engine from becoming responsible for every validation detail.

### Main Responsibilities

The validator checks inputs such as:

* Individual letter guesses.
* Alphabetic characters.
* Valid player names.
* Menu choices.
* Other game-specific input constraints.

### Guess Validation Flow

```text
Player input
     ↓
Renderer
     ↓
Engine
     ↓
Validator
     ↓
Valid / Invalid
```

If an input is invalid, the engine can reject it without modifying game state.

### Design Principle

Validation should be performed before gameplay state is changed.

## `game_mode.py`

### Purpose

`game_mode.py` defines the different ways Advanced Hangman can be played.

The current game modes are:

```text
Classic
Timed
Endless
Daily Challenge
```

### Main Components

The module contains:

* `GameMode`
* `GameModeSettings`
* `GameModeManager`

### `GameMode`

The enum provides standardized identifiers for each game mode.

### `GameModeSettings`

Each mode has configuration describing its behavior, including:

* Name.
* Description.
* Whether the mode is timed.
* Whether it is endless.
* Whether it is the daily challenge.
* Whether saving is allowed.
* Whether scoring is enabled.
* Time limit.

### `GameModeManager`

The manager provides centralized access to the active mode and its settings.

### Relationship With Difficulty

Difficulty and game mode are intentionally separate.

This allows combinations such as:

```text
Easy + Classic
Hard + Classic
Easy + Timed
Hard + Timed
Impossible + Daily Challenge
```

Difficulty determines how challenging the puzzle is, while game mode determines how the game operates.

## `timer.py`

### Purpose

`timer.py` provides timing functionality for gameplay.

The timer tracks how long the player has been playing.

### Main Responsibilities

The timer handles operations such as:

* Starting the timer.
* Stopping the timer.
* Resetting the timer.
* Measuring elapsed time.
* Supporting timed gameplay modes.

### Typical Flow

```text
Game starts
    ↓
Timer starts
    ↓
Player plays
    ↓
Elapsed time queried
    ↓
Game ends
    ↓
Timer stops
```

### Design Principle

The timer should manage time measurement rather than making gameplay decisions.

For example, `Timer` measures elapsed time, while `Engine` decides what should happen when a time limit is reached.

## Module Relationships

The main relationships between the modules can be represented as follows:

```text
                    ┌──────────────┐
                    │    Engine    │
                    └──────┬───────┘
                           │
       ┌───────────────────┼────────────────────┐
       │                   │                    │
       ▼                   ▼                    ▼
    Player            WordManager           Validator
       │                   │                    │
       │                   ▼                    │
       │              Word Data                │
       │                                        │
       └──────────────────┬─────────────────────┘
                          │
                          ▼
                     ScoreBoard
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
        Statistics                 SaveSystem
             │                         │
             │                         ▼
             │                    FileManager
             │
             ▼
          JSON Data

Engine
  │
  ├── DifficultyManager
  ├── GameModeManager
  ├── GameTimer
  └── Renderer
          │
          ├── Colors
          ├── HangmanFrames
          ├── Banner
          └── Animations
```

## Typical Gameplay Dependency Flow

When the player makes a guess, the systems interact approximately as follows:

```text
Player enters letter
        ↓
Renderer receives input
        ↓
Engine receives guess
        ↓
Validator checks guess
        ↓
Engine checks word
        ↓
WordManager provides word-related behavior
        ↓
ScoreBoard updates score if appropriate
        ↓
Engine updates game state
        ↓
Renderer displays new state
```

If the game ends:

```text
Victory / Defeat
       ↓
Engine finalizes game
       ↓
Player profile updated
       ↓
Statistics recorded
       ↓
Statistics saved
       ↓
Renderer displays result
```

## Separation of Responsibilities

The `game/` folder follows a modular architecture.

| Module            | Primary Responsibility                  |
| ----------------- | --------------------------------------- |
| `engine.py`       | Coordinates the entire gameplay process |
| `renderer.py`     | Displays the game's terminal interface  |
| `player.py`       | Stores player-specific information      |
| `difficulty.py`   | Defines difficulty settings             |
| `word_manager.py` | Handles words and word selection        |
| `scoreboard.py`   | Calculates and manages scores           |
| `statistics.py`   | Records long-term statistics            |
| `save_system.py`  | Saves and restores active game progress |
| `validator.py`    | Validates player input                  |
| `game_mode.py`    | Defines game-mode behavior              |
| `timer.py`        | Tracks gameplay time                    |

This modular structure makes individual components easier to test, maintain, and replace.

## Important Architectural Rule

The `Engine` is the coordinator, not the owner of every piece of functionality.

For example:

### Incorrect Approach

```python
# Engine manually calculates everything
score += 100
if len(guess) != 1:
    ...
if difficulty == "Hard":
    ...
```

### Preferred Approach

```python
score += self.scoreboard.correct_guess(...)
self.validator.validate_letter(...)
DifficultyManager.get(self.difficulty)
```

Each subsystem should remain responsible for its own domain.

## Interaction With Other Folders

The `game/` folder depends on several other project areas.

### `assets/`

Used primarily by `renderer.py` for:

* Colors.
* Hangman artwork.
* ASCII logo resources.

### `utils/`

Provides shared functionality such as:

* File operations.
* Constants.
* Terminal animations.
* Banner handling.
* Helper functions.

### `data/`

Provides persistent data such as:

* Difficulty-specific word lists.
* Statistics.
* Save files.

### `tests/`

Contains automated tests for the modules in `game/`.

### `docs/`

Contains documentation describing the architecture and behavior of these modules.

## Testing Strategy

Each major game subsystem should have its own test coverage where practical.

Examples include:

```text
tests/test_engine.py
tests/test_player.py
tests/test_validator.py
tests/test_word_manager.py
tests/test_scoreboard.py
tests/test_statistics.py
```

The goal is to verify individual modules independently rather than relying exclusively on manual gameplay.

The engine can then be tested as an integration point between those systems.

## Development Guidelines

When modifying the `game/` folder:

1. Keep each module focused on one primary responsibility.
2. Avoid duplicating functionality between modules.
3. Use managers for centralized configuration.
4. Avoid hardcoding difficulty values in the engine.
5. Avoid hardcoding game-mode behavior in unrelated modules.
6. Keep rendering logic inside `renderer.py`.
7. Keep validation logic inside `validator.py`.
8. Keep score calculations inside `scoreboard.py`.
9. Keep persistent save handling inside `save_system.py`.
10. Keep timing behavior inside `timer.py`.
11. Keep word-selection behavior inside `word_manager.py`.
12. Update the corresponding tests whenever behavior changes.

## Adding a New Game Feature

When adding a feature, first determine which module owns the responsibility.

For example:

| New Feature                 | Likely Module                 |
| --------------------------- | ----------------------------- |
| New difficulty              | `difficulty.py`               |
| New game mode               | `game_mode.py`                |
| New scoring rule            | `scoreboard.py`               |
| New validation rule         | `validator.py`                |
| New word-selection behavior | `word_manager.py`             |
| New save field              | `save_system.py`              |
| New player statistic        | `player.py` / `statistics.py` |
| New visual screen           | `renderer.py`                 |
| New timing behavior         | `timer.py`                    |
| Overall game-flow change    | `engine.py`                   |

This approach prevents unrelated modules from becoming unnecessarily large.

## Summary

The `game/` folder is the central gameplay layer of Advanced Hangman. It contains the engine and all major systems required to run a complete game.

The architecture is intentionally modular:

```text
Engine
 ├── Player
 ├── WordManager
 ├── Validator
 ├── ScoreBoard
 ├── Statistics
 ├── SaveSystem
 ├── Timer
 ├── Difficulty
 ├── GameMode
 └── Renderer
```

Each module has a clearly defined responsibility, while `Engine` coordinates them into a complete gameplay experience.

This separation makes Advanced Hangman easier to understand, test, debug, extend, and maintain as the project grows.

