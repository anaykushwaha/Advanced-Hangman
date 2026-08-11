# Data Directory Documentation

## Overview

The `data/` directory contains the external data used by Advanced Hangman during gameplay. These files separate game content and persistent information from the Python source code, allowing the application to modify or expand its data without changing the core logic.

The directory primarily contains word databases, persistent statistics, and saved game information. The Python modules in the `game/` and `utils/` directories access these files through dedicated systems such as `WordManager`, `Statistics`, `SaveSystem`, and `FileManager`.

Keeping data separate from application logic makes the project easier to maintain, extend, test, and customize.

## Directory Structure

```text
data/
│
├── easy_words.json
├── medium_words.json
├── hard_words.json
├── impossible_words.json
├── statistics.json
│
└── saves/
    └── savegame.json
```

The directory can be divided into two main categories:

* **Game content** — word databases used to generate puzzles.
* **Persistent player data** — statistics and saved game progress.

## Word Databases

The four word files contain the words and categories used by the game.

```text
easy_words.json
medium_words.json
hard_words.json
impossible_words.json
```

Each difficulty has its own database so that the `WordManager` can select appropriate words based on the player's selected difficulty.

This keeps difficulty-specific content outside the Python code.

### `easy_words.json`

Contains words intended for the Easy difficulty.

The words should generally be simpler and more accessible to new players.

The file is accessed by the `WordManager` when:

```text
Difficulty.EASY
```

is selected.

The Easy difficulty configuration in `DifficultyManager` points to:

```text
data/easy_words.json
```

### `medium_words.json`

Contains words intended for the Medium difficulty.

These words provide a more balanced challenge and are used when:

```text
Difficulty.MEDIUM
```

is active.

The corresponding difficulty configuration points to:

```text
data/medium_words.json
```

### `hard_words.json`

Contains words intended for the Hard difficulty.

The words are generally more difficult, longer, or less common than those in the Easy and Medium databases.

The Hard difficulty configuration points to:

```text
data/hard_words.json
```

### `impossible_words.json`

Contains the most difficult vocabulary in the game.

This database is used by:

```text
Difficulty.IMPOSSIBLE
```

and is intended to provide the highest level of challenge.

The corresponding difficulty configuration points to:

```text
data/impossible_words.json
```

## Word Data Structure

The word databases are JSON files so that word content can be edited without modifying Python source code.

A typical entry can contain information such as:

```json
{
    "word": "PYTHON",
    "category": "Programming"
}
```

The exact structure of the JSON data must remain compatible with the expectations of `WordManager`.

The `WordManager` is responsible for:

* Loading the appropriate word file.
* Reading the available entries.
* Selecting a word.
* Retrieving its category.
* Providing the selected word to the game engine.
* Creating the hidden/display version of the word.

The game engine does not need to know how the JSON files are structured internally. It requests a word from `WordManager` instead.

## Difficulty and Word Database Relationship

The difficulty system determines which word database should be used.

The relationship is:

```text
Difficulty
    │
    ├── Easy ────────> easy_words.json
    │
    ├── Medium ──────> medium_words.json
    │
    ├── Hard ────────> hard_words.json
    │
    └── Impossible ──> impossible_words.json
```

This design prevents the engine from hardcoding individual word-file paths.

Instead, `DifficultyManager` stores the appropriate `word_file` configuration, and `WordManager` uses that information to retrieve the correct database.

## `statistics.json`

The `statistics.json` file stores persistent statistics collected during gameplay.

Unlike the word databases, this file changes as the player completes games.

The statistics system can record information such as:

* Games played
* Games won
* Games lost
* Win rate
* Highest score
* Total score
* Current or best streak
* Total play time
* Letters guessed
* Hints used
* Difficulty-related statistics
* Game-mode statistics

The `Statistics` class is responsible for managing this information.

The application should not manipulate `statistics.json` directly from the gameplay engine. Instead, the statistics subsystem provides the appropriate interface for recording, loading, saving, generating reports, and resetting statistics.

## Statistics Data Flow

The general flow is:

```text
Player completes game
        │
        ▼
     Engine
        │
        ▼
   Statistics
        │
        ▼
statistics.json
```

When the game finishes, `Engine` records the results through the `Statistics` class.

The `Statistics` class then persists the updated information in `statistics.json`.

When statistics are requested later, the system loads the stored information and generates a report for the renderer.

## `saves/`

The `saves/` directory contains persistent saved-game data.

```text
data/
└── saves/
    └── savegame.json
```

The directory is separated from the other data files because save data represents an active or previously stored game state rather than permanent game content.

The `SaveSystem` manages this directory.

## `savegame.json`

The `savegame.json` file stores the state of a game that can be resumed later.

Saved information can include:

* Player name
* Difficulty
* Game mode
* Current word
* Category
* Guessed letters
* Correct letters
* Wrong letters
* Remaining lives
* Score
* Current streak
* Elapsed time
* Hint usage
* Game-over status
* Victory status

The `SaveSystem` provides methods for:

* Creating a default save.
* Saving game progress.
* Loading game progress.
* Updating selected save fields.
* Clearing progress.
* Deleting the save.
* Checking whether a save exists.
* Determining whether a saved game is active.
* Determining whether a saved game ended in victory or defeat.

## Save Data Flow

The general save process is:

```text
Engine
   │
   │ current game state
   ▼
SaveSystem
   │
   ▼
FileManager
   │
   ▼
data/saves/savegame.json
```

Loading works in the opposite direction:

```text
data/saves/savegame.json
        │
        ▼
   FileManager
        │
        ▼
    SaveSystem
        │
        ▼
      Engine
```

This layered structure ensures that file-system operations remain separated from gameplay logic.

## Relationship With `FileManager`

The files inside `data/` are not normally accessed directly by the gameplay engine.

The `FileManager` in `utils/file_manager.py` provides the low-level file operations required by the project.

It handles:

* Reading JSON files.
* Writing JSON files.
* Checking whether files exist.
* Creating directories.
* Deleting files.
* Reading and writing text.
* Checking file sizes.
* Clearing files.

The relationship is:

```text
Game Systems
     │
     ├── WordManager
     ├── Statistics
     └── SaveSystem
            │
            ▼
       FileManager
            │
            ▼
          data/
```

This keeps file-system responsibilities centralized.

## Data Persistence

Not all files in the `data/` directory behave in the same way.

### Static Data

These files primarily contain predefined game content:

```text
easy_words.json
medium_words.json
hard_words.json
impossible_words.json
```

They are normally created or edited by the developer.

### Persistent Runtime Data

These files are modified by the application:

```text
statistics.json
saves/savegame.json
```

`statistics.json` stores long-term player statistics, while `savegame.json` stores resumable game progress.

## Data Validation

The application should treat external JSON data as potentially invalid.

For example, a JSON file could be:

* Empty
* Malformed
* Missing expected fields
* Containing incorrect data types
* Missing entirely
* Manually modified by the user

Higher-level systems should therefore validate loaded data before using it.

For example, `SaveSystem.load()` provides default values when loaded data is invalid or incomplete.

This prevents corrupted external data from immediately crashing the game.

## Adding New Words

New words can be added to the appropriate difficulty database without modifying the game engine.

For example, adding another Easy word should involve modifying:

```text
data/easy_words.json
```

rather than changing:

```text
game/engine.py
```

This is one of the main advantages of separating data from application logic.

## Adding New Categories

Categories can similarly be expanded by modifying the word databases.

Examples of possible categories include:

* Animals
* Countries
* Food
* Sports
* Technology
* Programming
* Movies
* Science
* Geography
* General Knowledge

The exact categories supported depend on the contents of the word databases.

## File Format

The project uses JSON for structured data because JSON is:

* Human-readable
* Lightweight
* Easy to edit
* Supported natively by Python
* Suitable for dictionaries and lists
* Easy to serialize and deserialize
* Appropriate for small local datasets

Python's `json` module is used indirectly through `FileManager`.

## Why Data Is Separate From Code

Separating data from source code provides several advantages.

### Maintainability

Words can be changed without modifying Python classes.

### Extensibility

New word databases can be added later.

### Customization

Players or developers can potentially create custom word packs.

### Cleaner Architecture

Gameplay classes focus on gameplay rather than storing large amounts of static content.

### Easier Testing

Test data can be changed independently of the application logic.

### Reduced Hardcoding

Difficulty-specific content does not need to be embedded directly inside `Engine` or `WordManager`.

## Data Directory Responsibilities

The `data/` directory is responsible for storing:

1. Difficulty-specific word databases.
2. Persistent game statistics.
3. Saved game progress.
4. External structured information required by the application.

It is **not** responsible for:

* Gameplay logic
* Rendering
* Input validation
* Scoring calculations
* Difficulty management
* Game-mode management
* File-system abstraction

Those responsibilities belong to the appropriate Python modules.

## Relationship With the Overall Architecture

The `data/` directory occupies the persistence/content layer of the project.

```text
                    Advanced Hangman
                          │
                          ▼
                       Engine
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
    WordManager       Statistics       SaveSystem
          │               │                │
          └───────────────┼────────────────┘
                          ▼
                     FileManager
                          │
                          ▼
                        data/
             ┌────────────┼─────────────┐
             │            │             │
             ▼            ▼             ▼
        Word JSON    statistics.json   saves/
                                         │
                                         ▼
                                   savegame.json
```

This architecture keeps the responsibilities of the application separated into logical layers.

## Important Considerations

The following rules should be followed when working with the `data/` directory:

* Do not place Python source code inside `data/`.
* Keep word data valid JSON.
* Preserve the expected JSON structure.
* Do not manually modify `statistics.json` while the game is running.
* Do not manually modify `savegame.json` unless intentionally testing corrupted or custom save data.
* Use `FileManager` for file operations rather than duplicating file-system logic.
* Keep difficulty-specific words in the appropriate difficulty file.
* Avoid hardcoding word data inside gameplay classes.
* Ensure required data files exist before running the game.

## Future Expansion

The data architecture can be expanded without significantly changing the core game.

Potential future additions include:

```text
data/
├── achievements.json
├── custom_words/
│   ├── movies.json
│   ├── animals.json
│   └── programming.json
├── daily/
│   └── challenges.json
├── settings.json
└── profiles/
    └── players.json
```

These additions could support features such as achievements, custom word packs, daily challenges, persistent settings, and multiple player profiles.

## Conclusion

The `data/` directory provides the external data layer for Advanced Hangman. It stores the word databases that drive gameplay as well as persistent statistics and saved game information.

By keeping this information outside the Python source code, the project maintains a cleaner separation between **application logic, game content, and persistent data**. This makes Advanced Hangman easier to maintain, test, customize, and expand as additional features are introduced.

