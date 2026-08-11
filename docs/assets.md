# Assets Folder Documentation

## Overview

The `assets/` folder contains the static resources used by **Advanced Hangman** to improve the game's visual presentation and provide reusable terminal styling components. These resources are separated from the game's gameplay logic so that visual elements can be modified without changing the core engine.

The folder primarily contains the game's ASCII logo, terminal color definitions, and Hangman drawing frames. These resources are imported by other modules such as the renderer, banner utility, and gameplay interface.

The `assets/` folder does **not** contain gameplay logic, player data, saved games, statistics, or game-processing functionality.

## Folder Structure

```text
assets/
├── __init__.py
├── logo.txt
├── colors.py
└── hangman_frames.py
```

## `__init__.py`

### Purpose

The `__init__.py` file identifies `assets` as a Python package and allows its modules to be imported cleanly throughout the project.

### Responsibilities

* Marks the `assets/` directory as a Python package.
* Allows modules to be imported using paths such as:

  * `from assets.colors import Colors`
  * `from assets.hangman_frames import HangmanFrames`
* Provides a clean package boundary between static assets and the rest of the application.

### What It Should Not Contain

The file should remain lightweight. It should not contain:

* Gameplay logic.
* Game state.
* File-processing logic.
* Player information.
* Configuration for individual games.
* Large amounts of executable code.

## `logo.txt`

### Purpose

`logo.txt` contains the ASCII-art logo displayed by Advanced Hangman.

The logo provides the application with a recognizable visual identity when the program starts and when menus or major screens are displayed.

### Responsibilities

* Stores the game's ASCII logo.
* Provides a static visual resource that can be loaded by the banner system.
* Keeps large blocks of ASCII art outside Python source files.

### Usage

The logo is accessed indirectly through the banner utility rather than being part of the gameplay engine itself.

The typical flow is:

```text
logo.txt
   ↓
Banner
   ↓
Renderer
   ↓
Terminal
```

### Design Principle

The logo should contain presentation data only. If the game's visual identity needs to change, this file can be edited without modifying gameplay code.

## `colors.py`

### Purpose

`colors.py` contains reusable terminal color and text-formatting constants used throughout the application.

Instead of hardcoding ANSI escape sequences in multiple files, the project centralizes them in the `Colors` class.

### Main Responsibility

The `Colors` class provides reusable formatting values such as:

* Reset formatting.
* Standard terminal colors.
* Bright colors.
* Bold text.
* Other terminal formatting used by the renderer.

### Example Usage

Other modules can import the class:

```python
from assets.colors import Colors
```

and then use constants such as:

```python
Colors.GREEN
Colors.RED
Colors.YELLOW
Colors.CYAN
Colors.BOLD
Colors.RESET
```

### Why This Design Is Used

Centralizing terminal colors provides several advantages:

1. **Consistency**
   The same colors can be reused throughout the application.

2. **Maintainability**
   A color can be changed in one location instead of searching through every source file.

3. **Readability**
   Code such as:

```python
print(Colors.GREEN + "Correct!" + Colors.RESET)
```

is easier to understand than embedding raw ANSI escape sequences.

4. **Separation of Concerns**
   Color definitions remain separate from gameplay and rendering logic.

### Modules That Use It

The renderer is one of the primary consumers of `Colors`.

For example:

```text
Colors
  ↓
Renderer
  ↓
Menus / Gameplay Screens / Messages
```

## `hangman_frames.py`

### Purpose

`hangman_frames.py` stores the ASCII-art stages of the Hangman drawing.

Each incorrect guess advances the Hangman through another visual stage until the final stage represents defeat.

### Main Responsibility

The module provides the `HangmanFrames` class, which allows the renderer to retrieve the appropriate Hangman drawing for a particular stage.

The renderer uses the stage number provided by the game engine.

### Typical Flow

```text
Player makes incorrect guess
        ↓
Engine increases hangman_stage
        ↓
Renderer receives hangman_stage
        ↓
HangmanFrames retrieves matching frame
        ↓
Frame is displayed in terminal
```

### Separation From Gameplay Logic

`hangman_frames.py` should only contain the visual representation of the Hangman.

It should not determine:

* Whether a guess is correct.
* How many lives remain.
* Whether the player has won.
* Whether the game is over.
* How much the player scores.

Those decisions belong to the gameplay engine and related systems.

### Why Separate Frames Are Useful

Keeping the frames in their own module makes the project easier to maintain and customize.

For example, the Hangman artwork can be redesigned without changing:

* `engine.py`
* `renderer.py`
* `validator.py`
* `player.py`
* `scoreboard.py`

The engine only needs to provide a stage number, while the asset module determines what that stage looks like.

## Relationship With Other Project Folders

The `assets/` folder is primarily consumed by the presentation layer.

A simplified dependency relationship is:

```text
assets/
   │
   ├── logo.txt
   │      ↓
   │   Banner
   │      ↓
   │   Renderer
   │
   ├── colors.py
   │      ↓
   │   Renderer
   │
   └── hangman_frames.py
          ↓
       Renderer
          ↓
       Terminal
```

The `game/` folder provides the information that needs to be displayed, while the `assets/` folder provides reusable visual resources.

For example:

```text
game.engine
     ↓
hangman_stage = 3
     ↓
game.renderer
     ↓
assets.hangman_frames
     ↓
ASCII Hangman frame
     ↓
Terminal
```

## Separation of Responsibilities

The project follows a separation-of-concerns approach.

| Folder    | Responsibility                               |
| --------- | -------------------------------------------- |
| `assets/` | Static visual resources and terminal styling |
| `game/`   | Gameplay systems and game state              |
| `utils/`  | General-purpose utilities                    |
| `data/`   | Words, statistics, and saved game data       |
| `tests/`  | Automated tests                              |
| `docs/`   | Project documentation                        |

This prevents static presentation resources from becoming mixed with application logic.

## Development Guidelines

When adding a new asset, determine whether it belongs in this folder based on whether it is primarily a **static presentation resource**.

Good candidates include:

* ASCII art.
* Terminal color definitions.
* Static visual frames.
* Other reusable presentation resources.

Assets should generally **not** contain:

* Player profiles.
* Saved games.
* Word lists.
* Statistics.
* Gameplay rules.
* Score calculations.
* Input validation.
* Game-state management.

Those belong in their appropriate project folders.

## Modification Guidelines

When modifying an asset:

1. Preserve the existing filename unless there is a strong reason to rename it.
2. Keep static resources independent from gameplay logic.
3. Avoid duplicating the same visual constants in other modules.
4. Keep reusable terminal styling centralized in `colors.py`.
5. Keep Hangman artwork centralized in `hangman_frames.py`.
6. Keep large ASCII-art resources outside Python files when practical.
7. Test the application after changing assets to ensure terminal formatting and alignment remain correct.

## Summary

The `assets/` folder provides the static visual foundation of Advanced Hangman. It contains the game's ASCII logo, terminal color definitions, and Hangman drawing frames while keeping these resources separate from gameplay logic.

Its main purpose is to allow the game's visual presentation to be changed or expanded without requiring major changes to the underlying game engine.

The folder therefore supports the project's overall architecture by keeping **presentation resources reusable, centralized, and independent from gameplay processing**.

