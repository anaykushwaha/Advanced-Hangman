# Advanced Hangman — Architecture Documentation

## 1. Architecture Overview

Advanced Hangman is a modular Python terminal application designed around separation of responsibilities.

The project is divided into several layers:

```text
Advanced-Hangman/
│
├── Application Entry Point
│       ↓
├── Game Logic Layer
│       ↓
├── Utility Layer
│       ↓
├── Resource / Data Layer
│       ↓
└── Testing Layer
```

The primary goal of this architecture is to avoid placing all functionality inside one large file.

Instead, individual systems are separated into modules with clearly defined responsibilities.

The main gameplay controller is `game/engine.py`, while supporting systems such as validation, scoring, word management, saving, statistics, timing, difficulty, and game modes are implemented independently.

## 2. Complete Project Structure

The current project structure is:

```text
Advanced-Hangman/
│
├── README.md
├── requirements.txt
├── .gitignore
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
│   ├── animations.py
│   ├── constants.py
│   ├── banner.py
│   └── file_manager.py
│
├── tests/
│   ├── test_engine.py
│   ├── test_player.py
│   ├── test_validator.py
│   ├── test_word_manager.py
│   ├── test_scoreboard.py
│   └── test_statistics.py
│
└── docs/
    ├── architecture.md
    ├── game.md
    ├── utils.md
    ├── assets.md
    ├── data.md
    └── tests.md
```

## 3. High-Level Architecture

The application can be viewed as five major areas:

```text
                    ┌──────────────────────┐
                    │       main.py        │
                    │   Application Entry  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    game/engine.py    │
                    │   Gameplay Control   │
                    └──────────┬───────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │          │           │          │            │
        ▼          ▼           ▼          ▼            ▼
     Player    WordManager  Validator  ScoreBoard   Timer
        │          │           │          │            │
        └──────────┴───────────┴──────────┴────────────┘
                               │
                    ┌──────────┴───────────┐
                    │                      │
                    ▼                      ▼
               Statistics             SaveSystem
                    │                      │
                    │                      ▼
                    │                FileManager
                    │                      │
                    └──────────┬───────────┘
                               │
                               ▼
                             data/

Engine
  │
  ├── DifficultyManager
  ├── GameModeManager
  └── Renderer
          │
          ├── Colors
          ├── HangmanFrames
          ├── Banner
          └── Animations
```

## 4. Layered Architecture

The project uses a practical layered architecture rather than a strict enterprise framework.

### Layer 1 — Application

```text
main.py
```

Responsible for starting the application.

### Layer 2 — Game Logic

```text
game/
```

Contains the actual game systems and gameplay coordination.

### Layer 3 — Utilities

```text
utils/
```

Contains reusable functionality shared by different systems.

### Layer 4 — Resources and Persistent Data

```text
assets/
data/
```

Contains static resources and persistent information.

### Layer 5 — Testing

```text
tests/
```

Contains automated tests for the application's logic.

### Layer 6 — Documentation

```text
docs/
```

Contains technical documentation explaining the architecture and individual project components.

## 5. Application Entry Point

### `main.py`

`main.py` is the entry point of the application.

Its responsibility should be limited to starting the program rather than implementing gameplay rules.

Conceptually:

```text
Operating System
       ↓
    main.py
       ↓
     Engine
       ↓
   Game Starts
```

Keeping the entry point small makes the application easier to understand and prevents startup code from becoming mixed with gameplay logic.

## 6. Central Controller — Engine

The most important architectural component is:

```text
game/engine.py
```

The `Engine` coordinates the major gameplay systems.

It does not need to implement every operation itself.

Instead, it delegates responsibilities to specialized components.

For example:

```text
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

This makes `Engine` the **orchestrator** of the game.

## 7. Game Logic Components

### Player

```text
game/player.py
```

Represents the current player and stores player-specific information.

Examples include:

* Name.
* Score.
* Games played.
* Wins.
* Losses.
* Streak.
* Hints used.

### Word Manager

```text
game/word_manager.py
```

Handles word-related functionality.

Responsibilities include:

* Loading word data.
* Selecting words.
* Associating categories.
* Generating hidden-word displays.

### Validator

```text
game/validator.py
```

Ensures player input satisfies the game's requirements.

For example, it can verify that a guess is a valid single alphabetic character.

### ScoreBoard

```text
game/scoreboard.py
```

Centralizes scoring rules.

This prevents score formulas from being scattered throughout the engine.

### Statistics

```text
game/statistics.py
```

Records and manages long-term performance data.

### SaveSystem

```text
game/save_system.py
```

Manages the meaning and structure of saved game state.

### Timer

```text
game/timer.py
```

Tracks elapsed gameplay time and supports timed modes.

### Difficulty

```text
game/difficulty.py
```

Centralizes difficulty-specific settings.

### Game Mode

```text
game/game_mode.py
```

Defines how the game operates under different modes.

### Renderer

```text
game/renderer.py
```

Handles terminal presentation.

It receives information from the engine and converts that state into user-facing output.

## 8. Difficulty and Game Mode Separation

Difficulty and game mode are intentionally independent concepts.

### Difficulty

Difficulty determines how challenging the game is.

For example:

```text
Easy
Medium
Hard
Impossible
```

It can affect:

* Lives.
* Score multiplier.
* Hint availability.
* Hint penalties.
* Word selection.

### Game Mode

Game mode determines how the game is played.

Current modes include:

```text
Classic
Timed
Endless
Daily Challenge
```

A player can therefore combine the two concepts:

```text
Hard + Classic
Easy + Timed
Impossible + Timed
Medium + Endless
```

This design makes the system extensible.

Adding a new difficulty does not require creating a new game mode, and vice versa.

## 9. Rendering Architecture

The project separates game logic from presentation.

The engine determines what is happening.

The renderer determines how it looks.

```text
Game State
    ↓
  Engine
    ↓
 Renderer
    ↓
Terminal Output
```

For example, the engine may determine:

```text
Score = 450
Lives = 7
Word = PYTHON
Correct Letters = P, T
```

The renderer transforms that information into:

```text
Player: Anay
Score: 450
Lives: 7

_ _ T _ _ _
```

The renderer should not determine whether the player has actually won.

## 10. Assets Architecture

The `assets/` directory contains static presentation resources.

```text
assets/
├── logo.txt
├── colors.py
└── hangman_frames.py
```

### Logo

```text
logo.txt
```

Contains ASCII-art branding.

### Colors

```text
colors.py
```

Provides terminal color/style constants.

### Hangman Frames

```text
hangman_frames.py
```

Contains the visual stages of the hangman.

The assets layer is primarily consumed by the renderer.

```text
Assets
   ↓
Renderer
   ↓
Terminal
```

## 11. Utility Architecture

The `utils/` directory contains reusable support functionality.

```text
utils/
├── helper.py
├── animations.py
├── constants.py
├── banner.py
└── file_manager.py
```

### Helper

Provides reusable small functions.

### Animations

Provides terminal animation behavior.

### Constants

Provides shared application-wide configuration.

### Banner

Handles presentation of the ASCII logo.

### FileManager

Provides low-level file-system and JSON operations.

The utilities should remain relatively independent from game-specific logic.

## 12. Data Architecture

Persistent resources are stored in:

```text
data/
```

The data layer currently contains:

```text
data/
├── easy_words.json
├── medium_words.json
├── hard_words.json
├── impossible_words.json
├── statistics.json
└── saves/
    └── savegame.json
```

### Word Databases

The four word files correspond to the four difficulty levels.

```text
DifficultyManager
       ↓
DifficultySettings.word_file
       ↓
WordManager
       ↓
JSON word database
```

### Statistics

```text
Statistics
     ↓
FileManager
     ↓
statistics.json
```

### Save Data

```text
SaveSystem
     ↓
FileManager
     ↓
savegame.json
```

## 13. Persistence Architecture

The application separates high-level persistence logic from low-level file operations.

### High-Level

```text
SaveSystem
Statistics
```

These systems understand what the stored data means.

### Low-Level

```text
FileManager
```

This system only understands how to interact with files.

The relationship is:

```text
Game Logic
    ↓
SaveSystem / Statistics
    ↓
FileManager
    ↓
JSON Files
```

This separation prevents every game module from directly manipulating files.

## 14. Save System Flow

A typical save operation follows:

```text
Player Game
    ↓
Engine
    ↓
build_save_data()
    ↓
SaveSystem
    ↓
FileManager
    ↓
data/saves/savegame.json
```

Loading reverses the process:

```text
savegame.json
      ↓
FileManager
      ↓
SaveSystem
      ↓
Engine
      ↓
Game State Restored
```

The `SaveSystem` is responsible for interpreting the save structure.

## 15. Statistics Flow

Statistics are handled separately from active game saves.

```text
Game Ends
    ↓
Engine
    ↓
Statistics.record_completed_game()
    ↓
Statistics.save()
    ↓
FileManager
    ↓
statistics.json
```

This means an unfinished game and long-term player statistics are treated as different types of persistent information.

## 16. Gameplay Flow

A complete gameplay session can be represented as:

```text
Application Starts
       ↓
      main.py
       ↓
     Engine
       ↓
Player Configuration
       ↓
Difficulty Selection
       ↓
Game Mode Selection
       ↓
Word Selection
       ↓
Timer Starts
       ↓
Gameplay Loop
       ↓
Render Screen
       ↓
Receive Guess
       ↓
Validate Guess
       ↓
Check Word
       ↓
Update Score / Lives / Letters
       ↓
Render Updated State
       ↓
Check Win / Loss
       ↓
     ┌───────────────┐
     │               │
   Continue        Game Ends
     │               │
     └───→ Loop      ▼
                 Finalize
                    ↓
             Update Player
                    ↓
             Record Statistics
                    ↓
              Save Statistics
                    ↓
              Result Screen
```

## 17. Guess Processing Flow

A player's guess follows a specific pipeline:

```text
Player
  ↓
Renderer.prompt_guess()
  ↓
Engine.get_player_guess()
  ↓
Validator
  ↓
Valid Guess
  ↓
Engine.process_guess()
  ↓
Correct? ──────────────┐
  │                    │
 Yes                   No
  ↓                    ↓
Correct Letters     Wrong Letters
  ↓                    ↓
Update Display      Lose Life
  ↓                    ↓
Update Score        Advance Hangman
  └──────────┬─────────┘
             ↓
       Update Game State
             ↓
      Check Win / Defeat
```

This keeps validation, gameplay processing, scoring, and presentation conceptually separate.

## 18. Victory Flow

When the player completes the word:

```text
Word Complete
     ↓
is_game_won()
     ↓
finish_victory()
     ↓
Calculate Completion Score
     ↓
Calculate Final Score
     ↓
Stop Game
     ↓
Update Player Profile
     ↓
Record Statistics
     ↓
Save Statistics
     ↓
Victory Screen
```

The engine coordinates the process while individual systems perform their specialized responsibilities.

## 19. Defeat Flow

When the player runs out of lives:

```text
Lives Exhausted
      ↓
is_game_over()
      ↓
finish_defeat()
      ↓
Reveal Word
      ↓
Stop Game
      ↓
Update Player Profile
      ↓
Record Statistics
      ↓
Save Statistics
      ↓
Game Over Screen
```

## 20. Dependency Direction

The preferred dependency direction is:

```text
main.py
   ↓
game/
   ↓
utils/
   ↓
Python Standard Library
```

The data and assets directories provide resources consumed by the appropriate systems.

A simplified model is:

```text
          main.py
             ↓
           game/
             ↓
           utils/
             ↓
     Standard Library
```

The project should avoid unnecessary reverse dependencies.

For example, `utils/file_manager.py` should not depend on `game/engine.py`.

## 21. Dependency Responsibilities

A useful dependency map is:

```text
Engine
 ├── Player
 ├── WordManager
 ├── Validator
 ├── ScoreBoard
 ├── Statistics
 ├── SaveSystem
 ├── GameTimer
 ├── Difficulty
 ├── GameMode
 └── Renderer

Renderer
 ├── Colors
 ├── HangmanFrames
 ├── Animation
 ├── Banner
 ├── Constants
 └── Helper

SaveSystem
 └── FileManager

Statistics
 └── FileManager

WordManager
 └── FileManager
```

The exact implementation dependencies may evolve, but the architectural principle should remain the same.

## 22. Separation of Responsibilities

One of the most important principles in the project is **single responsibility**.

Each module should have one primary reason to change.

| Component           | Primary Responsibility            |
| ------------------- | --------------------------------- |
| `main.py`           | Start application                 |
| `Engine`            | Coordinate gameplay               |
| `Player`            | Store player information          |
| `WordManager`       | Manage words                      |
| `Validator`         | Validate input                    |
| `ScoreBoard`        | Calculate scores                  |
| `Statistics`        | Track long-term statistics        |
| `SaveSystem`        | Manage game saves                 |
| `Timer`             | Track time                        |
| `DifficultyManager` | Manage difficulty                 |
| `GameModeManager`   | Manage game modes                 |
| `Renderer`          | Display interface                 |
| `FileManager`       | Perform file operations           |
| `Animation`         | Perform terminal animations       |
| `Banner`            | Display banner                    |
| `Helper`            | Provide reusable helper functions |

## 23. Why the Architecture Is Modular

A monolithic implementation could place everything into a single file:

```text
Game
 ├── input
 ├── validation
 ├── scoring
 ├── saving
 ├── statistics
 ├── rendering
 ├── words
 └── timing
```

However, this would become difficult to maintain as the project grows.

The modular design instead creates:

```text
Engine
 ├── Validator
 ├── ScoreBoard
 ├── WordManager
 ├── SaveSystem
 ├── Statistics
 ├── Timer
 └── Renderer
```

Advantages include:

* Easier testing.
* Easier debugging.
* Better readability.
* Lower coupling.
* Easier feature additions.
* Clearer responsibilities.
* Reduced code duplication.
* Easier future refactoring.

## 24. Testing Architecture

Automated tests are stored in:

```text
tests/
```

Tests are separated from production code.

Current test modules include:

```text
tests/
├── test_engine.py
├── test_player.py
├── test_validator.py
├── test_word_manager.py
├── test_scoreboard.py
└── test_statistics.py
```

The tests focus primarily on game logic rather than requiring the entire application to run interactively.

### Testing Philosophy

Individual modules should be tested independently where possible.

For example:

```text
Validator
    ↓
test_validator.py
```

```text
ScoreBoard
    ↓
test_scoreboard.py
```

```text
WordManager
    ↓
test_word_manager.py
```

The engine can then be tested as the coordinator of these systems.

## 25. Mocking and Isolation

Some game systems interact with external resources or interactive functionality.

Examples include:

* Terminal input.
* Terminal output.
* File operations.
* Timers.
* Random word selection.

Tests can isolate these dependencies using mocking where appropriate.

The goal is to test the behavior of the component itself rather than accidentally testing unrelated systems.

For example, an engine test should be able to verify:

```text
"Correct guess increases score"
```

without requiring a real terminal animation to run.

## 26. Documentation Architecture

Technical documentation is stored in:

```text
docs/
```

The documentation layer mirrors the project's major components.

```text
docs/
├── architecture.md
├── game.md
├── utils.md
├── assets.md
├── data.md
└── tests.md
```

### Purpose of Each Document

| Document          | Purpose                      |
| ----------------- | ---------------------------- |
| `architecture.md` | Overall project architecture |
| `game.md`         | Game-layer documentation     |
| `utils.md`        | Utility-layer documentation  |
| `assets.md`       | Static asset documentation   |
| `data.md`         | Data-file documentation      |
| `tests.md`        | Testing documentation        |

This allows developers to understand either the entire project or a specific area without reading every source file.

## 27. Error Handling Architecture

Errors should be handled at the appropriate level.

Low-level modules should report or raise errors relevant to their own responsibilities.

For example:

```text
FileManager
    ↓
File-related error
```

while:

```text
Validator
    ↓
Invalid input
```

The engine can then decide how the application should respond.

This prevents low-level utilities from making high-level gameplay decisions.

## 28. Configuration Architecture

Configuration is distributed according to responsibility.

### Application-Wide Configuration

Stored in:

```text
utils/constants.py
```

### Difficulty Configuration

Stored in:

```text
game/difficulty.py
```

### Game Mode Configuration

Stored in:

```text
game/game_mode.py
```

This prevents one large configuration file from becoming responsible for unrelated settings.

## 29. Extensibility

The architecture is designed so new features can be added without rewriting the entire project.

### Adding a New Difficulty

Modify:

```text
game/difficulty.py
```

and provide:

* New enum value.
* New settings.
* New word database.

### Adding a New Game Mode

Modify:

```text
game/game_mode.py
```

and implement the required behavior through the engine.

### Adding New Words

Add or modify the appropriate JSON data file.

### Adding a New Visual Effect

Modify:

```text
utils/animations.py
```

and use it from the renderer.

### Adding a New Screen

Add the appropriate rendering method to:

```text
game/renderer.py
```

### Adding a New Persistent Field

Update the save structure in:

```text
game/save_system.py
```

and update the associated tests.

## 30. Architectural Rules

The following rules should be maintained as the project evolves.

### Rule 1 — Keep Gameplay in `game/`

Game-specific behavior belongs in the `game/` package.

### Rule 2 — Keep Generic Functionality in `utils/`

Reusable functionality belongs in `utils/`.

### Rule 3 — Keep Static Resources in `assets/`

ASCII artwork and visual constants belong in `assets/`.

### Rule 4 — Keep Persistent Data in `data/`

Word lists, statistics, and save data belong in `data/`.

### Rule 5 — Keep Tests in `tests/`

Automated tests should not be mixed with production modules.

### Rule 6 — Keep Documentation in `docs/`

Technical documentation should remain separate from executable code.

### Rule 7 — Avoid Circular Dependencies

Modules should depend on lower-level or peer systems only when necessary.

### Rule 8 — Avoid Duplicated Business Logic

If a rule already belongs to a dedicated system, other modules should call that system instead of reimplementing the rule.

### Rule 9 — Keep the Engine as an Orchestrator

The engine coordinates systems rather than becoming a giant collection of unrelated utility functions.

### Rule 10 — Update Tests With Behavior Changes

Whenever a module's behavior changes, its corresponding tests should be reviewed and updated.

## 31. Overall Architecture Diagram

The entire application can be summarized as:

```text
                         Advanced Hangman
                                │
                                ▼
                             main.py
                                │
                                ▼
                         ┌──────────────┐
                         │    Engine    │
                         └──────┬───────┘
                                │
       ┌────────────────────────┼─────────────────────────┐
       │            │           │           │             │
       ▼            ▼           ▼           ▼             ▼
    Player      WordManager  Validator  ScoreBoard     Timer
       │            │           │           │             │
       └────────────┴───────────┴───────────┴─────────────┘
                                │
                 ┌──────────────┼──────────────┐
                 │                             │
                 ▼                             ▼
             Statistics                   SaveSystem
                 │                             │
                 │                             ▼
                 │                       FileManager
                 │                             │
                 └──────────────┬──────────────┘
                                ▼
                              data/
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        ▼                       ▼                       ▼
   Word JSONs             statistics.json        savegame.json


                         Engine
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
       Difficulty                  GameMode
       Manager                     Manager
             │                           │
             └─────────────┬─────────────┘
                           ▼
                        Renderer
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          Assets        Animations      Helpers
             │
             ▼
          Terminal


                         Tests
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          Engine       Validator      Player
             │
             ├── WordManager
             ├── ScoreBoard
             └── Statistics
```

## 32. Final Architectural Summary

Advanced Hangman uses a modular architecture centered around a coordinating game engine.

The architecture can be summarized as:

```text
main.py
   ↓
Engine
   ↓
Specialized Game Systems
   ↓
Utilities / Resources
   ↓
Persistent Data
```

The major design principle is **separation of concerns**.

The engine controls the flow of the game, but specialized classes handle individual responsibilities:

```text
Player       → Player information
WordManager  → Words
Validator    → Input validation
ScoreBoard   → Scoring
Statistics   → Long-term statistics
SaveSystem   → Game persistence
Timer        → Time tracking
Difficulty   → Difficulty configuration
GameMode     → Game-mode configuration
Renderer     → Terminal presentation
```

The supporting layers provide:

```text
assets/      → Static visual resources
utils/       → Reusable utilities
data/        → Persistent data
tests/       → Automated verification
docs/        → Technical documentation
```

This architecture provides a strong foundation for expanding Advanced Hangman while keeping the codebase understandable and maintainable.

The project can therefore grow by adding or modifying individual systems instead of repeatedly rewriting the entire application.

