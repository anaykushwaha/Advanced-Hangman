# Utils Folder Documentation

## Overview

The `utils/` folder contains reusable utility modules used throughout the Advanced Hangman project.

These modules provide functionality that is not specific to one particular gameplay system. Examples include file operations, terminal animations, application-wide constants, banner rendering, and general helper functions.

The purpose of this folder is to prevent common functionality from being duplicated across the project.

The `utils/` folder should therefore remain focused on **general-purpose supporting functionality**, while game-specific behavior belongs in the `game/` folder.

## Folder Structure

```text
utils/
├── __init__.py
├── helper.py
├── animations.py
├── constants.py
├── banner.py
└── file_manager.py
```

## Architectural Role

The `utils/` folder acts as a shared support layer for the rest of the application.

A simplified relationship is:

```text
                game/
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
    FileManager Animations Constants
        │         │         │
        └─────────┼─────────┘
                  │
                utils/
```

Multiple parts of the application can import utilities without needing to know how the utility itself is implemented.

For example:

```text
SaveSystem
     ↓
FileManager
     ↓
JSON file
```

or:

```text
Renderer
     ↓
Animation
     ↓
Terminal
```

## `__init__.py`

### Purpose

The `__init__.py` file identifies `utils/` as a Python package.

It allows utility modules to be imported using package-qualified paths such as:

```python
from utils.constants import SCREEN_WIDTH
from utils.file_manager import FileManager
from utils.animations import Animation
```

### Responsibilities

* Defines the package boundary.
* Allows clean imports.
* Keeps utility modules organized under a single package.

### Design Guideline

The file should remain lightweight and should not contain major application logic.

## `helper.py`

### Purpose

`helper.py` contains small, reusable helper functions used throughout the application.

These functions are intended to simplify common operations that do not belong specifically to one game subsystem.

### Typical Responsibilities

Depending on the current implementation, helper functionality can include operations such as:

* Formatting text.
* Centering text.
* String manipulation.
* Small terminal-related calculations.
* General-purpose convenience functions.

One important helper used by the renderer is `center_text()`.

### Example

The renderer can use:

```python
from utils.helper import center_text
```

instead of implementing text-centering logic itself.

Conceptually:

```text
Renderer
   ↓
center_text()
   ↓
Formatted terminal output
```

### Design Principle

A helper function should generally be:

* Small.
* Reusable.
* Independent of game state.
* Easy to test.
* Focused on one operation.

A helper should not contain major gameplay logic.

### What Should Not Go Here

Avoid placing functionality such as:

* Score calculations.
* Guess validation.
* Word selection.
* Save management.
* Difficulty management.
* Game-mode management.

Those responsibilities belong in the appropriate `game/` modules.

## `animations.py`

### Purpose

`animations.py` provides reusable terminal animations for Advanced Hangman.

The module contains the `Animation` class, which provides static methods for displaying animated or timed terminal output.

### Main Responsibilities

The animation system can provide:

* Screen clearing.
* Delays.
* Typing effects.
* Line-by-line output.
* Loading spinners.
* Countdown sequences.
* Progress bars.
* Animated dots.
* Flashing messages.
* Blinking text.
* Fade-style effects.
* Moving or bouncing text.
* Victory animations.
* Game-over animations.
* Celebration sequences.
* Separators.
* Slowly rendered text boxes.

### Example Usage

The renderer can use:

```python
from utils.animations import Animation
```

and then call methods such as:

```python
Animation.pause()
Animation.type_text()
Animation.spinner()
Animation.countdown()
```

### Relationship With Renderer

The animation system provides the behavior, while the renderer determines **when** that behavior should be used.

For example:

```text
Engine
  ↓
Renderer
  ↓
Animation
  ↓
Terminal
```

This prevents animation code from being duplicated throughout the renderer.

### Design Principle

Animations should remain presentation utilities.

They should not determine:

* Whether a player won.
* Whether a player lost.
* How many lives remain.
* Which word was selected.
* How much the player scores.

They simply display visual effects requested by other modules.

## `constants.py`

### Purpose

`constants.py` stores application-wide constants used by multiple modules.

Centralizing these values prevents important configuration values from being duplicated throughout the project.

### Typical Constants

The module may contain values such as:

* Screen width.
* Application title.
* Save-file location.
* Data directories.
* Default player name.
* Timing defaults.
* Other project-wide configuration values.

For example:

```python
SCREEN_WIDTH
DEFAULT_PLAYER_NAME
SAVE_FILE
```

### Why Centralization Is Important

Without centralized constants, different modules might contain inconsistent values.

For example:

```python
# Renderer
width = 60

# Another module
width = 70
```

A centralized constant prevents this inconsistency:

```python
from utils.constants import SCREEN_WIDTH
```

### Design Principle

Constants should represent values that are:

* Shared across modules.
* Stable.
* Configuration-like.
* Not dependent on current game state.

Dynamic values should not be stored as global constants.

For example, the current player's score does **not** belong in `constants.py`.

## `banner.py`

### Purpose

`banner.py` manages the display of the game's ASCII-art banner or logo.

It provides a reusable interface for displaying the game's visual identity.

### Main Responsibility

The `Banner` class handles presentation of the game's logo, which is stored separately in:

```text
assets/logo.txt
```

### Typical Flow

```text
assets/logo.txt
       ↓
     Banner
       ↓
    Renderer
       ↓
    Terminal
```

### Separation From Logo Data

The actual ASCII artwork belongs in the `assets/` folder.

The `Banner` utility provides the Python functionality needed to load and display that resource.

This separates:

* **What the logo looks like** → `assets/logo.txt`
* **How the logo is displayed** → `utils/banner.py`

### Design Principle

`Banner` should remain a presentation utility.

It should not contain gameplay logic or determine when a game ends.

## `file_manager.py`

### Purpose

`file_manager.py` provides centralized file-system operations for the application.

It is the project's low-level interface for reading, writing, checking, deleting, and managing files.

### Main Responsibility

The `FileManager` class provides reusable operations for:

* Loading text files.
* Saving text files.
* Loading JSON files.
* Saving JSON files.
* Checking whether files exist.
* Deleting files.
* Creating folders.
* Checking file size.
* Clearing files.

### Text File Operations

The file manager can read an entire text file:

```python
FileManager.load_text(path)
```

and save text:

```python
FileManager.save_text(path, text)
```

### JSON Operations

The application primarily uses JSON for structured persistent data.

The file manager provides:

```python
FileManager.load_json(path)
FileManager.save_json(path, data)
```

This allows higher-level systems to work with dictionaries and lists without implementing JSON file handling themselves.

### Utility Operations

The file manager also provides operations such as:

```python
FileManager.exists(path)
FileManager.delete(path)
FileManager.create_folder(path)
FileManager.file_size(path)
FileManager.clear_file(path)
```

### Relationship With Other Modules

The `FileManager` is intentionally lower-level than systems such as `SaveSystem` and `Statistics`.

For example:

```text
SaveSystem
    ↓
FileManager
    ↓
JSON save file
```

and:

```text
Statistics
    ↓
FileManager
    ↓
statistics.json
```

### Separation of Responsibilities

`FileManager` is responsible for **how** a file is accessed.

`SaveSystem` is responsible for **what save data means**.

For example:

```text
SaveSystem
"player_name"
"score"
"remaining_lives"
"game_over"
       ↓
FileManager
       ↓
JSON file
```

This distinction is important for maintaining clean architecture.

## Relationship Between Utility Modules

The utilities are independent but can work together.

A simplified relationship is:

```text
utils/
│
├── helper.py
│      ↓
│   Formatting / convenience
│
├── animations.py
│      ↓
│   Terminal animation
│
├── constants.py
│      ↓
│   Shared configuration
│
├── banner.py
│      ↓
│   Logo presentation
│
└── file_manager.py
       ↓
    File operations
```

They provide services to higher-level modules rather than controlling gameplay themselves.

## Relationship With the Game Folder

The `game/` folder is one of the main consumers of `utils/`.

For example:

```text
game/renderer.py
       │
       ├── utils.animations
       ├── utils.banner
       ├── utils.constants
       └── utils.helper
```

And:

```text
game/save_system.py
       │
       └── utils.file_manager
```

This creates a clean separation:

```text
Game-specific behavior
        ↓
      game/
        ↓
Reusable support functionality
        ↓
      utils/
```

## Relationship With the Assets Folder

The utilities can also interact with static assets.

The most important example is the banner system:

```text
assets/logo.txt
       ↓
utils/banner.py
       ↓
game/renderer.py
       ↓
Terminal
```

Similarly, terminal styling comes from:

```text
assets/colors.py
       ↓
game/renderer.py
```

The utilities and assets therefore complement one another:

* `assets/` stores static resources.
* `utils/` provides reusable functionality for working with those resources.

## Relationship With the Data Folder

`utils/file_manager.py` provides the low-level file operations used by systems that interact with the `data/` directory.

For example:

```text
game/word_manager.py
        ↓
FileManager
        ↓
data/easy_words.json
```

and:

```text
game/statistics.py
        ↓
FileManager
        ↓
data/statistics.json
```

and:

```text
game/save_system.py
        ↓
FileManager
        ↓
data/saves/savegame.json
```

The utility layer therefore provides a common interface for persistent data access.

## Separation of Responsibilities

The project follows a clear separation between reusable utilities and application-specific functionality.

| Utility           | Responsibility                         |
| ----------------- | -------------------------------------- |
| `helper.py`       | Small reusable helper functions        |
| `animations.py`   | Terminal animations and timing effects |
| `constants.py`    | Shared application-wide constants      |
| `banner.py`       | Loading and displaying the game banner |
| `file_manager.py` | Low-level file and JSON operations     |

## What Belongs in `utils/`

Good candidates for the `utils/` folder include:

* Reusable helper functions.
* Generic file operations.
* Terminal formatting utilities.
* Terminal animation utilities.
* Shared constants.
* Generic presentation helpers.

The key requirement is that the functionality should be useful to multiple parts of the project and should not represent one specific gameplay system.

## What Does Not Belong in `utils/`

The following should generally remain outside `utils/`:

### Gameplay Rules

For example:

* Guess processing.
* Win conditions.
* Loss conditions.
* Lives.
* Score calculations.

These belong in `game/`.

### Player Data

Player-specific information belongs in:

```text
game/player.py
```

### Difficulty Rules

Difficulty settings belong in:

```text
game/difficulty.py
```

### Game Modes

Game-mode definitions belong in:

```text
game/game_mode.py
```

### Word Management

Word-selection behavior belongs in:

```text
game/word_manager.py
```

### Persistent Game Meaning

Save-data behavior belongs in:

```text
game/save_system.py
```

The low-level file operations themselves belong in:

```text
utils/file_manager.py
```

## Development Guidelines

When modifying the `utils/` folder:

1. Keep utility functions generic whenever possible.
2. Avoid storing game state in utility modules.
3. Avoid importing high-level gameplay modules into utilities.
4. Keep file-system operations centralized in `FileManager`.
5. Keep shared constants centralized in `constants.py`.
6. Keep terminal animation behavior centralized in `animations.py`.
7. Keep banner presentation centralized in `banner.py`.
8. Avoid duplicating helper functions across game modules.
9. Update relevant tests whenever utility behavior changes.
10. Keep dependencies flowing from higher-level systems toward lower-level utilities.

## Dependency Direction

The preferred architectural direction is:

```text
Application / Game Logic
          ↓
       Utilities
          ↓
   Python Standard Library
```

For example:

```text
Engine
  ↓
SaveSystem
  ↓
FileManager
  ↓
pathlib / json
```

The utility layer should generally not depend on the `Engine`.

This prevents circular dependencies and keeps the utilities reusable.

## Testing Considerations

Utilities should be tested independently because many other modules depend on them.

For example, `FileManager` should be tested for:

* Correct text loading.
* Correct text saving.
* Correct JSON loading.
* Correct JSON saving.
* File existence detection.
* File deletion.
* Folder creation.
* File-size calculation.
* File clearing.

Animation utilities can be tested where practical, although terminal output and timing-based behavior may require more careful testing than pure helper functions.

Helper functions should be tested using normal input/output assertions.

## Extending the Utilities

When adding a new utility, ask:

1. Is this functionality reusable?
2. Is it independent of game state?
3. Could multiple modules benefit from it?
4. Does it belong to an existing utility module?
5. Would adding it reduce duplicated code elsewhere?

For example, if multiple modules need a common text-formatting operation, it may belong in `helper.py`.

If multiple modules need the same file operation, it should likely belong in `file_manager.py`.

If several screens need the same animation, it may belong in `animations.py`.

## Summary

The `utils/` folder provides the reusable foundation that supports the rest of Advanced Hangman.

Its modules are intentionally generic:

```text
utils/
├── helper.py
│     → General reusable helpers
│
├── animations.py
│     → Terminal animations
│
├── constants.py
│     → Shared configuration
│
├── banner.py
│     → ASCII banner presentation
│
└── file_manager.py
      → File and JSON operations
```

The folder follows an important architectural principle: **common functionality should be implemented once and reused throughout the project**.

By keeping these utilities separate from gameplay systems, Advanced Hangman remains easier to maintain, test, debug, and expand.

