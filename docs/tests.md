# Tests Documentation

## Overview

The `tests/` directory contains the automated unit tests for the Advanced Hangman project. Its purpose is to verify that individual classes, methods, and subsystems behave correctly and consistently without requiring the entire game to run.

The test suite is primarily built using Python's built-in `unittest` framework. Each major module in the `game/` and `utils/` directories has a corresponding test file where appropriate. The tests cover normal behavior, invalid input, edge cases, state changes, return values, and interactions between components.

The test suite helps prevent regressions as the project is modified and provides confidence that changes to one subsystem do not unintentionally break another.

## Directory Structure

```text
tests/
│
├── test_engine.py
├── test_player.py
├── test_validator.py
├── test_word_manager.py
├── test_scoreboard.py
├── test_statistics.py
├── test_renderer.py
├── test_difficulty.py
├── test_save_system.py
├── test_game_mode.py
└── test_file_manager.py
```

Each test file is responsible for testing one primary component of the application.

## Testing Philosophy

The project follows a modular testing approach. Instead of testing the entire application as one large system, individual components are tested independently whenever possible.

The tests generally verify:

* Correct return values
* Correct object state
* Valid and invalid inputs
* Boundary conditions
* Error handling
* File operations
* Game-state transitions
* Score calculations
* Difficulty and game-mode configuration
* Save and load behavior
* Renderer interactions
* Statistics updates

Where a class depends on another subsystem, that dependency can be replaced with a mock during testing. This allows the test to focus on the behavior of the component being tested.

## Test Files

### `test_engine.py`

Tests the central `Engine` class and its coordination of the game's subsystems.

The engine tests cover:

* Engine initialization
* Game resetting
* Player configuration
* Difficulty selection
* Game-mode selection
* Word loading
* Game starting
* Guess processing
* Correct guesses
* Incorrect guesses
* Duplicate guesses
* Word completion
* Victory conditions
* Defeat conditions
* Game-over conditions
* Score updates
* Guess counting
* Accuracy calculation
* Rendering
* Gameplay turns
* Game-state updates
* Victory and defeat processing
* Statistics recording
* Player profile updates
* Save and load functionality
* Autosaving
* Continuing saved games
* Difficulty and game-mode selection
* Help and settings screens
* Resetting progress
* Resetting the entire application state
* Engine state snapshots
* Utility methods
* String representations

Because `Engine` coordinates many other classes, this is one of the largest test files in the project.

### `test_player.py`

Tests the `Player` class and its player-profile functionality.

The tests verify:

* Player initialization
* Player name handling
* Score management
* Games played
* Games won
* Games lost
* Current streak
* Best streak
* Hints used
* Player statistics
* Score updates
* Win/loss updates
* Streak behavior
* Player reset behavior
* String representation
* Object representation

### `test_validator.py`

Tests the input validation system.

The validator tests verify that the game correctly distinguishes valid input from invalid input.

Testing includes:

* Single alphabetic letters
* Uppercase and lowercase input
* Empty strings
* Multiple characters
* Numbers
* Symbols
* Whitespace
* Invalid guesses
* Letter normalization
* Validation errors

This prevents invalid user input from reaching the gameplay engine.

### `test_word_manager.py`

Tests the word-management system responsible for loading and selecting words.

The tests cover:

* Word-file loading
* Word selection
* Category handling
* Difficulty-based word retrieval
* Random word selection
* Display-word generation
* Hidden letters
* Correctly revealed letters
* Repeated letters
* Spaces and phrases
* Empty or invalid word data

The purpose is to ensure that the engine always receives valid puzzle information.

### `test_scoreboard.py`

Tests the scoring system.

The tests verify:

* Correct-guess scoring
* Incorrect-guess handling
* Word-completion bonuses
* Difficulty multipliers
* Final score calculations
* Player score updates
* Score resets
* Scoreboard state
* String representations where applicable

These tests help ensure that scoring remains consistent across different difficulty levels and game situations.

### `test_statistics.py`

Tests the statistics subsystem.

The tests cover:

* Statistics initialization
* Games played
* Wins
* Losses
* Win rate
* Scores
* Highest score
* Streak information
* Play time
* Letters guessed
* Hints used
* Difficulty statistics
* Game-mode statistics
* Recording completed games
* Generating reports
* Saving statistics
* Loading statistics
* Resetting statistics

The goal is to ensure that player performance data is recorded accurately and persists correctly.

### `test_renderer.py`

Tests the terminal rendering system.

Because `Renderer` is responsible for displaying information rather than calculating game logic, these tests focus primarily on whether the appropriate rendering methods are called with the correct information.

Testing includes:

* Renderer initialization
* Screen clearing
* Separators
* Titles and subtitles
* Centered text
* Menus
* Loading screens
* Messages
* Hangman rendering
* Hidden-word rendering
* Difficulty information
* Player information
* Score information
* Timer display
* Remaining lives
* Correct and incorrect letters
* Game screens
* Pause screen
* Help screen
* Statistics screens
* Victory screen
* Game-over screen
* Leaderboard
* Dialog boxes
* Footer rendering
* Goodbye screen
* Credits
* Splash screen
* String representations

Mock objects are particularly useful here because the renderer interacts heavily with terminal output and animation functionality.

### `test_difficulty.py`

Tests the difficulty configuration system.

The tests verify:

* All difficulty levels exist
* Difficulty settings are correctly defined
* Easy settings
* Medium settings
* Hard settings
* Impossible settings
* Maximum lives
* Score multipliers
* Hint penalties
* Hint limits
* Word-file paths
* Difficulty descriptions
* Current difficulty management
* Difficulty conversion from strings
* Invalid difficulty handling
* Retrieving all difficulties
* Retrieving difficulty names
* Resetting to the default difficulty

This ensures that gameplay components do not need to hardcode difficulty-specific values.

### `test_save_system.py`

Tests the game's save and persistence system.

The tests cover:

* Save-system initialization
* Save-file existence
* Save-file creation
* Default save data
* Saving game state
* Loading game state
* Handling missing save files
* Handling invalid save data
* Updating existing saves
* Clearing progress
* Deleting saves
* Checking active games
* Detecting finished games
* Detecting victories
* Detecting defeats
* Converting saves to dictionaries
* Restoring saves from dictionaries
* Reloading save data
* Quick save/load helpers
* String representation

These tests are particularly important because save data must remain consistent even when the game is restarted.

### `test_game_mode.py`

Tests the game-mode configuration system.

The tests verify:

* Classic mode
* Timed mode
* Endless mode
* Daily Challenge mode
* Mode descriptions
* Timer configuration
* Endless-mode configuration
* Daily-mode configuration
* Save availability
* Score availability
* Time limits
* Current mode management
* String-to-enum conversion
* Invalid mode handling
* Retrieving all modes
* Retrieving mode names
* Resetting to Classic mode
* Convenience methods such as `is_timed()`, `is_endless()`, and `is_daily()`

This ensures that game modes remain independent from difficulty settings while still interacting correctly with the engine.

### `test_file_manager.py`

Tests the low-level file-management utilities.

The tests cover:

* Loading text files
* Saving text files
* Loading JSON
* Saving JSON
* Checking file existence
* Deleting files
* Creating directories
* Measuring file size
* Clearing files
* Handling file paths
* Creating missing parent directories

These tests help ensure that higher-level systems such as `SaveSystem`, `Statistics`, and `WordManager` can safely depend on the file-management layer.

## Mocking and Isolation

Some tests use mocking to isolate the component being tested from unrelated systems.

For example, when testing the `Engine`, it is often unnecessary to actually display terminal animations or write real save files. Instead, dependent methods can be replaced with mock objects.

Python's `unittest.mock` functionality provides tools such as:

```python
from unittest.mock import MagicMock
```

A mocked method can then be configured and inspected:

```python
self.engine.renderer.success = MagicMock()

self.engine.renderer.success("Game saved successfully")

self.engine.renderer.success.assert_called_once_with(
    "Game saved successfully"
)
```

This allows the test to verify that the engine requested the correct behavior without depending on the implementation of the renderer.

## Running the Tests

The complete test suite can be executed from the project root with:

```bash
python -m unittest discover tests
```

If `pytest` is installed, the suite can also be run with:

```bash
pytest
```

Individual test files can be executed directly. For example:

```bash
python -m unittest tests.test_engine
```

or:

```bash
python -m unittest tests.test_validator
```

## What a Successful Test Run Means

A successful test run indicates that the tested components are behaving according to their expected contracts.

However, unit tests do not completely replace manual or integration testing. The game should also be played manually to verify that the complete system works correctly when all components operate together.

Important integration scenarios include:

* Starting a new game
* Selecting different difficulties
* Selecting different game modes
* Guessing correct letters
* Guessing incorrect letters
* Guessing repeated letters
* Solving words containing repeated letters
* Losing a game
* Saving a game
* Loading a saved game
* Continuing a saved game
* Updating statistics
* Using the timer
* Returning to menus
* Resetting progress

## Relationship With the Rest of the Project

The `tests/` directory sits outside the application's runtime code.

```text
Advanced-Hangman/
│
├── game/
│   ├── engine.py
│   ├── player.py
│   ├── validator.py
│   ├── word_manager.py
│   ├── scoreboard.py
│   ├── statistics.py
│   ├── save_system.py
│   ├── difficulty.py
│   ├── game_mode.py
│   ├── timer.py
│   └── renderer.py
│
├── utils/
│   ├── file_manager.py
│   ├── helper.py
│   ├── animations.py
│   ├── constants.py
│   └── banner.py
│
└── tests/
    ├── test_engine.py
    ├── test_player.py
    ├── test_validator.py
    ├── test_word_manager.py
    ├── test_scoreboard.py
    ├── test_statistics.py
    ├── test_renderer.py
    ├── test_difficulty.py
    ├── test_save_system.py
    ├── test_game_mode.py
    └── test_file_manager.py
```

The application files provide the functionality, while the test files verify that functionality.

## Testing Goals

The overall goals of the test suite are to:

1. Detect bugs before they reach the final application.
2. Prevent regressions when existing code is modified.
3. Verify that individual modules behave independently.
4. Confirm that invalid input is handled safely.
5. Verify that game-state transitions are correct.
6. Ensure persistent data is stored and retrieved correctly.
7. Verify scoring and statistics calculations.
8. Confirm that configuration systems behave consistently.
9. Make future refactoring safer.
10. Improve the reliability and maintainability of the project.

## Conclusion

The `tests/` directory provides the automated quality-control layer of Advanced Hangman. By testing the project's major gameplay, configuration, persistence, rendering, and utility components independently, the test suite helps ensure that the application remains reliable as new features are added or existing systems are modified.

The combination of unit testing, mocking, and manual integration testing provides a strong foundation for maintaining the project and makes the codebase more suitable as a portfolio project.


