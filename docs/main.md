# main.py Documentation

## 1. Purpose

`main.py` is the **entry point and application-level controller** for Advanced Hangman. It is responsible for starting the program, displaying the main menu, collecting the player's configuration choices, creating or continuing games through the `Engine`, and handling application shutdown. It does not contain the core Hangman gameplay logic; instead, it delegates gameplay-related work to the appropriate modules inside the `game/` package.

## 2. Responsibilities

The main responsibilities of `main.py` are:

* Start the Advanced Hangman application.
* Create the `HangmanApplication` controller.
* Create and manage the central `Engine` instance.
* Display the main application menu.
* Handle main-menu selections.
* Collect the player's name.
* Allow the player to select a difficulty.
* Allow the player to select a game mode.
* Start a newly configured game.
* Continue a previously saved game.
* Provide access to statistics, leaderboard, help, and settings.
* Handle invalid menu selections.
* Handle `KeyboardInterrupt` and unexpected application errors.
* Exit the application cleanly.

## 3. Imports

### `from __future__ import annotations`

Enables postponed evaluation of type annotations. This allows annotations such as `Difficulty` and `GameMode` to be handled without requiring immediate evaluation when the module is loaded.

### `import sys`

Provides access to system-level functionality, primarily `sys.exit()` when the application terminates.

### `Engine`

```python
from game.engine import Engine
```

Imports the central gameplay engine. `main.py` uses the engine rather than implementing gameplay logic itself.

The engine handles:

* Game initialization
* Word selection
* Guess processing
* Scoring
* Timers
* Saving and loading
* Statistics
* Rendering
* Win/loss processing

### `Difficulty`

```python
from game.difficulty import Difficulty
```

Provides the available difficulty levels:

* Easy
* Medium
* Hard
* Impossible

### `GameMode`

```python
from game.game_mode import GameMode
```

Provides the available game modes.

### Banner functions

```python
from utils.banner import (
    print_banner,
    print_goodbye
)
```

Used to display the application's startup banner and goodbye message.

### `clear_screen`

```python
from utils.helper import clear_screen
```

Clears the terminal before displaying different application screens.

### `DEFAULT_PLAYER_NAME`

```python
from utils.constants import DEFAULT_PLAYER_NAME
```

Provides the default player name when the user does not enter a name.

## 4. `HangmanApplication`

`HangmanApplication` is the **top-level application controller**.

It sits above the `Engine` and manages the overall application flow.

### `__init__()`

```python
def __init__(self) -> None:
```

Initializes the application.

It creates:

* An `Engine` instance
* A `running` flag

The `running` flag controls whether the main application loop should continue.

### `start()`

```python
def start(self) -> None:
```

Starts the application.

The method:

1. Clears the terminal.
2. Displays the game banner.
3. Opens the main menu.

This acts as the first major method called after the application object is created.

### `quit()`

```python
def quit(self) -> None:
```

Terminates the application.

It:

1. Displays the goodbye message.
2. Sets `running` to `False`.
3. Calls `sys.exit()`.

This provides a centralized shutdown operation.

## 5. Main Menu

### `main_menu()`

```python
def main_menu(self) -> None:
```

Runs the application's primary menu loop.

The menu provides access to:

1. New Game
2. Continue Saved Game
3. Statistics
4. Leaderboard
5. Help
6. Settings
7. Quit

The method repeatedly displays the menu and passes the user's selection to `handle_main_menu()`.

### `handle_main_menu()`

```python
def handle_main_menu(self, choice: str) -> None:
```

Processes a main-menu selection.

The method uses Python's `match` statement to route each menu option to the appropriate operation.

| Choice | Action              |
| ------ | ------------------- |
| `1`    | Open new-game setup |
| `2`    | Continue saved game |
| `3`    | Show statistics     |
| `4`    | Show leaderboard    |
| `5`    | Show help           |
| `6`    | Show settings       |
| `7`    | Quit application    |

Invalid selections produce an error message and wait for the user before returning to the menu.

## 6. New Game Setup

### `new_game_menu()`

```python
def new_game_menu(self) -> None:
```

Collects all configuration required before starting a new game.

The method obtains:

* Player name
* Difficulty
* Game mode

It then passes these values to:

```python
self.engine.create_new_game(...)
```

This keeps actual gameplay logic outside `main.py`.

### `get_player_name()`

```python
def get_player_name(self) -> str:
```

Prompts the player for their name.

If the player enters an empty string, `DEFAULT_PLAYER_NAME` is returned.

Otherwise, the entered name is returned.

### `select_difficulty()`

```python
def select_difficulty(self) -> Difficulty:
```

Displays the difficulty-selection menu and repeatedly asks for a valid choice.

The choices are mapped to:

```python
1 → Difficulty.EASY
2 → Difficulty.MEDIUM
3 → Difficulty.HARD
4 → Difficulty.IMPOSSIBLE
```

Invalid choices cause the method to display an error and ask the player to try again.

The method does not directly modify difficulty settings. It simply returns the selected `Difficulty` enum to the caller.

### `select_game_mode()`

```python
def select_game_mode(self) -> GameMode:
```

Displays the game-mode selection menu and returns the selected `GameMode`.

The method follows the same validation pattern as `select_difficulty()`.

## 7. Application Entry Point

### `main()`

```python
def main() -> None:
```

Creates the `HangmanApplication` and starts it.

It also provides top-level exception handling.

### `KeyboardInterrupt`

If the user presses `Ctrl+C`, the application prints an exit message and attempts to shut down through `application.quit()`.

### General Exception Handling

Unexpected errors are caught using:

```python
except Exception as error:
```

The application then displays:

* A general error message
* The actual exception
* A prompt before exiting

This prevents the program from immediately terminating with an unformatted traceback during normal use.

## 8. Module Execution Guard

```python
if __name__ == "__main__":
    main()
```

This ensures `main()` runs only when `main.py` is executed directly.

For example:

```text
python main.py
```

will start the application.

Importing `main.py` from another module will not automatically start the game.

## 9. Application Flow

The overall flow of `main.py` is:

```text
Program starts
      ↓
main()
      ↓
HangmanApplication()
      ↓
start()
      ↓
Display banner
      ↓
main_menu()
      ↓
User selects option
      ↓
handle_main_menu()
      ↓
┌──────────────────────────────┐
│ New Game                     │
│ Continue Game                │
│ Statistics                   │
│ Leaderboard                  │
│ Help                         │
│ Settings                     │
│ Quit                         │
└──────────────────────────────┘
      ↓
Engine handles game-specific work
      ↓
Application returns to menu
      ↓
Quit
```

## 10. Architectural Role

`main.py` belongs to the **application layer** of Advanced Hangman.

Its primary purpose is coordination rather than gameplay.

The architecture can be summarized as:

```text
main.py
   │
   ▼
HangmanApplication
   │
   ▼
Engine
   │
   ├── Player
   ├── WordManager
   ├── Validator
   ├── ScoreBoard
   ├── Statistics
   ├── SaveSystem
   ├── GameTimer
   ├── DifficultyManager
   ├── GameModeManager
   └── Renderer
```

This separation keeps `main.py` relatively lightweight and prevents the application's entry point from becoming responsible for the internal mechanics of Hangman.

## 11. Design Principles

`main.py` follows several important project-design principles:

### Separation of Concerns

The application controller handles menus and high-level navigation while the `Engine` handles gameplay.

### Delegation

Rather than directly manipulating game state, `main.py` delegates operations to `Engine`.

### Enum-Based Configuration

Difficulty and game mode selections use `Difficulty` and `GameMode` enums rather than arbitrary strings.

### Centralized Application Shutdown

The `quit()` method provides a single location for terminating the application.

### Input Validation

Menu selections are checked before being accepted.

### Exception Handling

The top-level `main()` function provides protection against unexpected runtime errors.

## 12. Dependencies

`main.py` depends on:

* `game.engine`
* `game.difficulty`
* `game.game_mode`
* `utils.banner`
* `utils.helper`
* `utils.constants`

It does not directly interact with:

* JSON files
* Save files
* Word databases
* Statistics files
* Terminal rendering internals
* Scoring calculations
* Hangman logic

Those responsibilities belong to specialized modules elsewhere in the project.

## 13. Important Implementation Note

The current `main.py` should remain synchronized with the project's current `GameMode` definitions and `Engine` API.

For example, if `GameMode` contains:

```python
CLASSIC
TIMED
ENDLESS
DAILY
```

then `select_game_mode()` should use those values rather than referencing a nonexistent `GameMode.SURVIVAL`.

Likewise, every method called on `self.engine` must exist in the current `Engine` implementation.

This is particularly important because `main.py` acts as the connection point between the user interface and the rest of the application.

## 14. Summary

`main.py` is the starting point of Advanced Hangman and the controller for the application's high-level navigation. It creates the main `Engine`, presents menus, collects player configuration, and delegates actual gameplay and subsystem operations to specialized classes. Keeping this file focused on application flow helps maintain the project's modular architecture and makes the codebase easier to test, maintain, and extend.

