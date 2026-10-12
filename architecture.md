
# Advanced Hangman — Architecture Documentation

## 1. Architecture Overview

Advanced Hangman is a modular Python terminal application designed around separation of concerns, maintainability, and testability.

The project divides responsibilities across dedicated modules instead of placing the entire application in one large file.

The main architectural components are:

- **Application Layer:** Starts the application and manages the main menu.
- **Game Logic Layer:** Coordinates gameplay and manages individual game systems.
- **Utility Layer:** Provides reusable functions and file operations.
- **Assets Layer:** Contains static visual resources and terminal styling.
- **Data Layer:** Stores word databases, statistics, and saved game information.
- **Testing Layer:** Contains automated tests for application components.
- **Documentation Layer:** Explains the architecture and individual modules.

The central gameplay controller is `game/engine.py`. It coordinates components such as the player, word manager, validator, scoreboard, statistics manager, save system, timer, difficulty settings, game modes, and renderer.

The main architectural objective is to make each component responsible for a clearly defined part of the application.

## 2. Architecture Goals

The architecture follows several practical software engineering principles.

### 2.1 Separation of Concerns

Each module should have one primary responsibility.

For example:

- `game/validator.py` validates player input.
- `game/word_manager.py` manages word selection and word-related operations.
- `game/scoreboard.py` handles scoring calculations.
- `game/save_system.py` manages saved game state.
- `utils/file_manager.py` provides reusable file operations.

This prevents unrelated functionality from becoming tightly coupled.

### 2.2 Modularity

Individual systems are implemented in separate Python modules.

A module can be updated or extended without unnecessarily changing unrelated parts of the application.

### 2.3 Testability

Components should be testable independently wherever practical.

Input, output, file access, timing, and random selection should be isolated or mocked when necessary.

### 2.4 Maintainability

A consistent directory structure and clear module responsibilities make the project easier to understand, debug, and extend.

### 2.5 Extensibility

The architecture supports future additions such as new difficulty levels, game modes, scoring rules, word categories, and terminal effects.

## 3. Complete Project Structure

The project is organized into the following directories and files:

```text
Advanced-Hangman/
│
├── README.md
├── LICENSE
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
│       ├── .gitkeep
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
    ├── main.md
    ├── game.md
    ├── utils.md
    ├── assets.md
    ├── data.md
    └── tests.md
```

The exact files present in the working directory should be kept synchronized with this documentation.

The `data/saves/.gitkeep` file is an optional placeholder for preserving the save directory in Git. A personal `savegame.json` may be generated at runtime and does not need to be committed.

## 4. High-Level Architecture

The application follows a layered design in which the entry point starts the program, the engine coordinates gameplay, specialized components perform individual tasks, and supporting modules provide resources and persistence.

```text
                    Advanced Hangman
                           |
                           v
                       main.py
                    Application Layer
                           |
                           v
                     game/engine.py
                    Gameplay Controller
                           |
           +---------------+----------------+
           |               |                |
           v               v                v
        Player         WordManager       Validator
           |               |                |
           +---------------+----------------+
                           |
           +---------------+----------------+
           |               |                |
           v               v                v
       ScoreBoard       GameTimer         Renderer
           |                                |
           v                                v
       Statistics                       Terminal UI
           |
           v
       SaveSystem
           |
           v
       FileManager
           |
           v
          data/

Supporting Resources:
    assets/
    utils/

Verification:
    tests/

Technical Documentation:
    docs/
```

This diagram describes the intended logical organization. The actual runtime dependencies should be verified against the Python imports and method calls in the implementation.

## 5. Layered Architecture

### 5.1 Application Layer

Location:

```text
main.py
```

The application layer provides the program's entry point and coordinates application-level interactions.

Its responsibilities include:

- Initializing the application.
- Starting the main menu.
- Handling menu selections.
- Starting a new game.
- Offering access to saved games.
- Displaying statistics and leaderboard options.
- Providing help and settings menus.
- Handling application exit.

The entry point should delegate gameplay behavior to the engine instead of duplicating game rules.

### 5.2 Game Logic Layer

Location:

```text
game/
```

The game package contains the main gameplay controller and supporting game systems.

Its responsibilities include:

- Managing game state.
- Processing guesses.
- Checking victory and defeat conditions.
- Coordinating scoring and player updates.
- Managing difficulty and game modes.
- Controlling timers.
- Coordinating saves and statistics.
- Requesting terminal output from the renderer.

### 5.3 Utility Layer

Location:

```text
utils/
```

The utility package provides reusable functionality that is not specific to a single gameplay rule.

Its responsibilities include:

- File operations.
- Shared constants.
- General helper functions.
- Terminal animations.
- Application banners.

Generic utility modules should not depend on the game engine.

### 5.4 Assets Layer

Location:

```text
assets/
```

The assets package contains static visual resources and presentation-related constants.

Examples include ASCII artwork, terminal color definitions, and hangman illustrations.

### 5.5 Data Layer

Location:

```text
data/
```

The data directory stores persistent information used by the application.

Examples include:

- Difficulty-specific word databases.
- Player statistics.
- Saved game state.

JSON files provide a straightforward storage format for this terminal application.

### 5.6 Testing Layer

Location:

```text
tests/
```

The testing layer contains automated tests for individual modules and their interactions.

Tests should verify expected behavior without requiring unnecessary interactive terminal input.

### 5.7 Documentation Layer

Location:

```text
docs/
```

The documentation layer contains Markdown files explaining the architecture, application entry point, game modules, utilities, assets, data files, and tests.

## 6. Application Entry Point

### 6.1 `main.py`

`main.py` is the starting point of the application.

The intended startup sequence is:

```text
Operating System
       |
       v
    main.py
       |
       v
Initialize Application
       |
       v
Initialize Engine
       |
       v
Display Main Menu
       |
       v
Handle User Selection
```

The entry point should remain focused on application orchestration.

It should not contain duplicate implementations of input validation, scoring, word selection, or other gameplay rules already assigned to the game package.

### 6.2 Application Responsibilities

The application controller may provide:

- `start()` — begin the application.
- `quit()` — terminate the application gracefully.
- Main menu handling.
- New-game setup.
- Saved-game selection.
- Help and settings menus.
- Navigation to statistics and leaderboard functionality.

These names describe the application interface and should be checked against the actual methods defined in `main.py`.

### 6.3 Application and Engine Relationship

The application and engine serve different purposes.

```text
Application
    |
    | Handles application navigation
    v
Engine
    |
    | Coordinates gameplay
    v
Specialized Game Systems
```

The application decides which major operation to initiate. The engine manages the gameplay behavior associated with that operation.

## 7. Central Gameplay Controller

### 7.1 `game/engine.py`

The `Engine` is the central coordinator of gameplay.

It connects the different game components and maintains the flow of a game session.

Its responsibilities may include:

- Initializing game systems.
- Resetting game state.
- Configuring difficulty and game mode.
- Starting a new game.
- Loading an existing game.
- Selecting the secret word.
- Processing guesses.
- Updating the visible word.
- Updating score and remaining lives.
- Checking win and loss conditions.
- Coordinating the renderer.
- Recording completed games.
- Saving and restoring progress.

### 7.2 Engine as an Orchestrator

The engine should coordinate specialized components rather than duplicate their responsibilities.

```text
Engine
  |
  +-- Player
  +-- WordManager
  +-- Validator
  +-- ScoreBoard
  +-- Statistics
  +-- SaveSystem
  +-- GameTimer
  +-- Difficulty Configuration
  +-- Game Mode Configuration
  +-- Renderer
```

For example, when a player submits a guess, the engine coordinates validation, guess processing, state updates, and rendering.

The validator determines whether the input is valid. The engine determines how a valid guess affects the active game. The renderer presents the resulting state.

### 7.3 Engine Design Principles

The engine should:

- Coordinate rather than duplicate specialized logic.
- Maintain a consistent game state.
- Use clear and predictable state transitions.
- Avoid direct low-level file operations when a dedicated persistence component exists.
- Avoid mixing presentation formatting with gameplay rules.
- Provide methods that can be tested independently.

## 8. Game Logic Components

### 8.1 Player

File:

```text
game/player.py
```

The player component represents the current player and stores player-specific information.

Depending on the implementation, this may include:

- Player name.
- Score.
- Games played.
- Wins and losses.
- Current or best streak.
- Hints used.

The player component should manage player-related state rather than deciding how the entire game proceeds.

### 8.2 Word Manager

File:

```text
game/word_manager.py
```

The word manager handles word-related operations.

Responsibilities may include:

- Loading word databases.
- Selecting a secret word.
- Associating words with categories.
- Supporting difficulty-specific word selection.
- Preparing hidden-word displays.
- Managing word-related validation or lookup operations.

The word manager should use the configured data files rather than duplicating word databases in Python source code.

### 8.3 Validator

File:

```text
game/validator.py
```

The validator checks player input before it is processed by the game engine.

Validation may include:

- Rejecting empty input.
- Checking whether a guess is a valid letter.
- Rejecting malformed guesses.
- Detecting repeated guesses if that behavior is implemented.
- Returning a clear validation result.

Validation rules should be centralized to avoid inconsistent behavior across different menus or game modes.

### 8.4 ScoreBoard

File:

```text
game/scoreboard.py
```

The scoreboard centralizes scoring calculations.

Depending on the scoring system, it may calculate:

- Points for correct guesses.
- Penalties for incorrect guesses.
- Difficulty bonuses.
- Completion bonuses.
- Hint penalties.
- Final game scores.

The engine should request score updates from the scoring component instead of scattering scoring formulas throughout the application.

### 8.5 Statistics

File:

```text
game/statistics.py
```

The statistics component manages longer-term performance records.

Possible statistics include:

- Total games played.
- Total victories and defeats.
- Win rate.
- Highest score.
- Longest winning streak.
- Performance by difficulty.
- Performance by game mode.

The exact statistics depend on the fields implemented by the project.

Statistics should be kept separate from an active game's temporary state.

### 8.6 SaveSystem

File:

```text
game/save_system.py
```

The save system manages the structure and interpretation of saved game data.

Its responsibilities include:

- Checking whether a save exists.
- Creating a default save structure.
- Saving current game state.
- Loading saved state.
- Updating save fields.
- Deleting saves.
- Clearing saved progress.
- Checking saved-game status.

The save system should use the file manager for low-level file operations.

### 8.7 GameTimer

File:

```text
game/timer.py
```

The timer manages elapsed gameplay time and time-related behavior.

Depending on the implementation, it may support:

- Starting a timer.
- Stopping a timer.
- Measuring elapsed time.
- Resetting timer state.
- Checking time limits.
- Supporting timed game modes.

Time-based rules should be coordinated with the engine so that expiration leads to a consistent game-state transition.

### 8.8 Difficulty Configuration

File:

```text
game/difficulty.py
```

The difficulty module defines the available difficulty levels and their associated settings.

The documented levels are:

```text
Easy
Medium
Hard
Impossible
```

Difficulty settings may control:

- Maximum incorrect guesses or lives.
- Scoring multipliers.
- Hint availability.
- Hint penalties.
- Word database selection.

A centralized difficulty configuration prevents different modules from maintaining inconsistent difficulty rules.

### 8.9 Game Mode Configuration

File:

```text
game/game_mode.py
```

The game mode module defines the rules or configuration associated with different styles of play.

The documented modes are:

```text
Classic
Timed
Endless
Daily Challenge
```

The exact behavior of each mode must be implemented and verified in the game systems.

A mode may influence time limits, game progression, completion conditions, or whether saving is permitted.

### 8.10 Renderer

File:

```text
game/renderer.py
```

The renderer is responsible for terminal presentation.

It may display:

- The current word.
- Remaining lives.
- Hangman artwork.
- Player score.
- Incorrect guesses.
- Game instructions.
- Victory and defeat screens.
- Menus and status messages.

The renderer should present the game state supplied by the engine. It should not independently decide whether the player has won or lost.

## 9. Difficulty and Game Mode Separation

Difficulty and game mode represent separate concepts.

### 9.1 Difficulty

Difficulty controls how challenging a game is.

For example:

```text
Easy + Classic
Medium + Timed
Hard + Classic
Impossible + Timed
```

Difficulty may change the number of permitted mistakes, scoring rules, hints, or word selection.

### 9.2 Game Mode

Game mode controls the style or rules of the game.

For example:

- Classic may use standard hangman rules.
- Timed may impose a time limit.
- Endless may support continued play across multiple words.
- Daily Challenge may provide a date-based challenge.

These descriptions represent intended behavior. Each mode must be implemented before it can be considered functional.

### 9.3 Independent Configuration

The intended relationship is:

```text
Difficulty Configuration
          |
          v
   Difficulty Settings
          |
          +------+
                 |
                 v
              Engine
                 ^
                 |
          +------+
          |
     Game Mode Settings
          ^
          |
   Game Mode Configuration
```

Separating difficulty from game mode makes it possible to add a new difficulty without creating a new mode, and vice versa.

## 10. Rendering Architecture

The application separates gameplay state from terminal presentation.

```text
Game State
    |
    v
  Engine
    |
    v
 Renderer
    |
    v
Terminal Output
```

The engine determines the state of the game. The renderer converts that state into readable terminal output.

For example, the engine may maintain:

```text
Score: 450
Remaining Lives: 7
Secret Word: PYTHON
Correct Guesses: P, T
```

The renderer may display the corresponding hidden word as:

```text
Player: Example
Score: 450
Remaining Lives: 7

P _ T _ _ _
```

The displayed values must be derived from the actual game state.

### 10.1 Presentation Responsibilities

The renderer should:

- Format information consistently.
- Display appropriate hangman frames.
- Use terminal colors where supported.
- Present clear prompts and messages.
- Separate visual formatting from game rules.

### 10.2 Terminal Compatibility

Terminal colors and animations should not prevent the game from operating in environments with limited terminal capabilities.

Presentation effects should be optional where necessary and should not alter gameplay logic.

## 11. Assets Architecture

The `assets/` directory contains static presentation resources.

```text
assets/
├── __init__.py
├── logo.txt
├── colors.py
└── hangman_frames.py
```

### 11.1 Logo

File:

```text
assets/logo.txt
```

Contains the application's ASCII-art branding.

The banner or renderer can read and display this resource.

### 11.2 Colors

File:

```text
assets/colors.py
```

Provides terminal color and style constants.

Centralizing these definitions avoids repeated escape sequences throughout the codebase.

### 11.3 Hangman Frames

File:

```text
assets/hangman_frames.py
```

Contains the visual stages of the hangman illustration.

The renderer selects the appropriate frame based on the current gameplay state.

### 11.4 Asset Usage

The intended presentation flow is:

```text
Assets
   |
   v
Renderer / Banner
   |
   v
Terminal
```

Assets should primarily provide presentation resources rather than implement gameplay rules.

## 12. Utility Architecture

The `utils/` directory contains reusable supporting functionality.

```text
utils/
├── __init__.py
├── helper.py
├── animations.py
├── constants.py
├── banner.py
└── file_manager.py
```

### 12.1 Helper

File:

```text
utils/helper.py
```

Provides small, reusable helper functions.

Helpers should remain general-purpose and should not become a second implementation of the game engine.

### 12.2 Animations

File:

```text
utils/animations.py
```

Provides terminal animation effects.

Animations should be presentation-focused and should not control scoring or victory conditions.

### 12.3 Constants

File:

```text
utils/constants.py
```

Stores shared application constants, such as default values, common paths, or other configuration values that are genuinely shared.

Game-specific difficulty and mode settings should remain in their corresponding game modules.

### 12.4 Banner

File:

```text
utils/banner.py
```

Provides functionality for displaying the application's banner or branding.

It may use the logo resource in `assets/logo.txt`.

### 12.5 FileManager

File:

```text
utils/file_manager.py
```

Provides low-level file and JSON operations.

Its documented operations include:

- Loading text.
- Saving text.
- Loading JSON.
- Saving JSON.
- Checking file existence.
- Deleting files.
- Creating directories.
- Checking file size.
- Clearing file contents.

The file manager should handle file operations without deciding what a saved game or statistic means.

## 13. Data Architecture

Persistent resources are stored in the `data/` directory.

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

### 13.1 Word Databases

The four word files correspond to the documented difficulty levels.

```text
Difficulty Configuration
          |
          v
Selected Difficulty
          |
          v
Configured Word File
          |
          v
WordManager
          |
          v
Selected Secret Word
```

Each JSON word database should follow the structure expected by `game/word_manager.py`.

The actual JSON schema must be confirmed against the word manager implementation and data files.

### 13.2 Statistics Data

File:

```text
data/statistics.json
```

Stores persistent statistics when the application is configured to save them.

The statistics component interprets the stored values, while the file manager performs the underlying file operations.

### 13.3 Saved Game Data

File:

```text
data/saves/savegame.json
```

Stores an active game's saved state when saving is supported and enabled.

The save format should include every field required to reconstruct a valid game state.

The schema should be consistent between saving, loading, and default-save creation.

### 13.4 Data Validation

Persistent JSON data may be missing, malformed, or incompatible with a newer version of the application.

The responsible component should handle these conditions appropriately rather than allowing invalid data to silently corrupt gameplay.

## 14. Persistence Architecture

The persistence design separates high-level data management from low-level file access.

### 14.1 High-Level Persistence

The following components understand the meaning of stored information:

```text
SaveSystem
Statistics
WordManager
```

They determine what information is loaded or saved and how that information is used.

### 14.2 Low-Level Persistence

The file manager provides reusable file access:

```text
FileManager
```

It should not contain game-specific decisions about scores, victories, or saved gameplay state.

### 14.3 Persistence Flow

```text
Game Components
       |
       v
SaveSystem / Statistics / WordManager
       |
       v
FileManager
       |
       v
JSON Files
```

This separation reduces duplicated file-handling code and makes persistence behavior easier to test.

## 15. Save System Flow

### 15.1 Saving a Game

A typical save operation follows this sequence:

```text
Active Game
     |
     v
   Engine
     |
     v
Build Save Data
     |
     v
 SaveSystem
     |
     v
 FileManager
     |
     v
savegame.json
```

The engine gathers the current gameplay state. The save system manages the save structure, and the file manager writes the data.

### 15.2 Loading a Game

Loading follows the reverse direction:

```text
savegame.json
     |
     v
 FileManager
     |
     v
 SaveSystem
     |
     v
   Engine
     |
     v
Restore Game State
     |
     v
Resume Gameplay
```

### 15.3 Save Consistency

The save schema must agree across:

- Default-save creation.
- Save serialization.
- Save loading.
- Engine state restoration.
- Tests covering save and load behavior.

If the engine expects fields that the save system does not create or preserve, loading may fail or restore an incomplete state.

Save and load behavior should therefore be tested as a complete round trip.

## 16. Statistics Flow

Statistics are separate from active game saves.

A typical completed-game flow is:

```text
Game Completes
      |
      v
    Engine
      |
      v
Statistics Component
      |
      v
Record Result
      |
      v
Persist Statistics
      |
      v
  FileManager
      |
      v
statistics.json
```

The statistics component should update the appropriate records when a game is completed.

The application should avoid recording the same completed game multiple times if the completion logic can be reached repeatedly.

Unfinished game state and long-term performance statistics should remain separate concepts.

## 17. Gameplay Flow

A complete gameplay session follows the intended sequence below:

```text
Application Starts
        |
        v
      main.py
        |
        v
  Initialize Engine
        |
        v
 Player Configuration
        |
        v
 Difficulty Selection
        |
        v
 Game Mode Selection
        |
        v
   Select Word
        |
        v
 Initialize Game State
        |
        v
 Start Timer if Required
        |
        v
    Gameplay Loop
        |
        v
   Render Current State
        |
        v
 Receive Player Guess
        |
        v
  Validate Player Input
        |
        v
  Process Valid Guess
        |
        v
 Update Game State
        |
        v
 Check Victory / Defeat / Timeout
        |
        +----------------------+
        |                      |
        v                      v
 Continue Playing          Game Ends
        |                      |
        |                      v
        |                Finalize Result
        |                      |
        |                      v
        |                Update Player
        |                      |
        |                      v
        |                Record Statistics
        |                      |
        |                      v
        |                Display Result
        |                      |
        +----------------------+
```

The precise sequence may differ according to game mode and the implemented engine behavior.

## 18. Guess Processing Flow

Each guess should pass through a consistent processing pipeline.

```text
Player
  |
  v
Receive Guess
  |
  v
Validator
  |
  v
Input Valid?
  |
  +-------------------+
  |                   |
  v                   v
   No                 Yes
   |                   |
   v                   v
Show Error       Process Guess
                       |
                       v
                  Guess Correct?
                   /        \
                  /          \
                 v            v
               Yes            No
                |              |
                v              v
        Record Correct    Record Incorrect
             Guess             Guess
                |              |
                v              v
         Update Display   Update Lives
                |              |
                +------+-------+
                       |
                       v
                Update Game State
                       |
                       v
                Update Score
                       |
                       v
              Check End Conditions
                       |
                       v
                 Render State
```

The implementation should ensure that each guess updates the game state exactly once.

Correct guesses should not be recorded or scored twice because the same processing path is invoked redundantly.

Repeated guesses should follow one consistent policy, such as rejecting the guess without applying an additional score or life change.

## 19. Victory Flow

When the player correctly reveals the entire word, the engine should finalize the victory.

```text
Word Completely Revealed
          |
          v
     Check Victory
          |
          v
    Finalize Victory
          |
          v
 Calculate Final Score
          |
          v
   Stop Game Timer
          |
          v
 Update Player Profile
          |
          v
 Record Game Statistics
          |
          v
 Persist Statistics
          |
          v
   Display Victory Screen
```

The engine coordinates the sequence, while the scoring, player, statistics, timer, and renderer components perform their specialized tasks.

Completion logic should be protected against repeated execution so that the same game is not finalized more than once.

## 20. Defeat and Timeout Flow

A game may end when the player exhausts the permitted mistakes or when a configured time limit expires.

### 20.1 Defeat by Incorrect Guesses

```text
Permitted Mistakes Exhausted
            |
            v
       Check Defeat
            |
            v
       Finalize Defeat
            |
            v
        Reveal Word
            |
            v
       Stop Game Timer
            |
            v
      Update Player Data
            |
            v
      Record Statistics
            |
            v
      Persist Statistics
            |
            v
      Display Game Over
```

### 20.2 Defeat by Timeout

```text
Time Limit Reached
        |
        v
   Detect Timeout
        |
        v
   Finalize Result
        |
        v
   Stop Game Timer
        |
        v
   Record Statistics
        |
        v
   Display Result
```

The engine must define how timeout interacts with victory and other end conditions.

Only one terminal result should be recorded for a single game session.

## 21. Dependency Direction

The preferred dependency direction is from higher-level application coordination toward specialized systems and lower-level utilities.

```text
Application Entry Point
          |
          v
       Game Layer
          |
          v
     Utility Layer
          |
          v
 Python Standard Library
```

The assets and data directories provide resources consumed by the appropriate modules.

This diagram represents a general design guideline, not a claim that every module currently imports only the layer immediately below it.

### 21.1 Dependency Rules

- `main.py` may coordinate the engine and application menus.
- The engine may depend on specialized game components.
- Game components may use reusable utility functions.
- Persistence components may use the file manager.
- The renderer may use presentation assets and utilities.
- Generic utility modules should not import the engine.
- Lower-level modules should not depend on higher-level application control.

### 21.2 Avoid Circular Dependencies

Circular imports make initialization harder to understand and can create runtime errors.

For example, `utils/file_manager.py` should not import `game/engine.py`.

If two modules require shared functionality, move that functionality into an appropriate lower-level module rather than making each module import the other.

## 22. Dependency Responsibilities

The following table describes the intended dependency relationships.

| Component | Main collaborators |
|---|---|
| `main.py` | Engine and application-level functionality |
| `Engine` | Player, WordManager, Validator, ScoreBoard, Statistics, SaveSystem, GameTimer, difficulty, game mode, Renderer |
| `Renderer` | Assets and presentation utilities |
| `WordManager` | FileManager and word data |
| `SaveSystem` | FileManager and save data |
| `Statistics` | FileManager and statistics data |
| `GameTimer` | Standard-library time functionality or an equivalent timing mechanism |
| `DifficultyManager` | Difficulty settings |
| `GameModeManager` | Game mode settings |
| `FileManager` | Python file and JSON functionality |
| `Banner` | Logo resource and presentation utilities |

The exact dependencies must be confirmed against the current source code.

The objective is to keep dependencies explicit and avoid unnecessary coupling.

## 23. Separation of Responsibilities

Each component should have one primary reason to change.

| Component | Primary responsibility |
|---|---|
| `main.py` | Start and coordinate the application |
| `Engine` | Orchestrate gameplay |
| `Player` | Maintain player-specific state |
| `WordManager` | Manage word selection and word data |
| `Validator` | Validate player input |
| `ScoreBoard` | Calculate scoring changes |
| `Statistics` | Maintain long-term performance records |
| `SaveSystem` | Manage saved game state |
| `GameTimer` | Track gameplay time |
| `DifficultyManager` | Manage difficulty configuration |
| `GameModeManager` | Manage game mode configuration |
| `Renderer` | Present game state in the terminal |
| `FileManager` | Perform low-level file operations |
| `Animations` | Provide terminal animation effects |
| `Banner` | Display application branding |
| `Helper` | Provide reusable helper functions |
| `Assets` | Supply static presentation resources |

This separation makes individual modules easier to test, understand, and maintain.

## 24. Why the Architecture Is Modular

A monolithic implementation could place input handling, validation, scoring, saving, statistics, word selection, rendering, and timing in one file.

As the application grows, this approach makes it harder to locate bugs and safely modify existing functionality.

The modular architecture instead assigns these responsibilities to separate components coordinated by the engine.

### 24.1 Benefits

- Easier debugging.
- Better code readability.
- Lower coupling between systems.
- More focused automated tests.
- Reduced duplication of business logic.
- Clearer ownership of game state.
- Simpler feature additions.
- More manageable future refactoring.

### 24.2 Avoiding Over-Engineering

Modularity should remain practical.

A separate module or class is useful when it provides a clear responsibility, reusable behavior, or a meaningful testing boundary.

Small, unrelated helpers do not need additional architectural layers without a concrete benefit.

## 25. Testing Architecture

Automated tests are stored in:

```text
tests/
├── test_engine.py
├── test_player.py
├── test_validator.py
├── test_word_manager.py
├── test_scoreboard.py
└── test_statistics.py
```

Tests should verify the behavior of production modules without requiring the entire application to run interactively.

### 25.1 Test Responsibilities

| Test module | Primary focus |
|---|---|
| `test_engine.py` | Game state, guess processing, and game flow |
| `test_player.py` | Player data and player-related operations |
| `test_validator.py` | Input validation and invalid input |
| `test_word_manager.py` | Word loading and word selection |
| `test_scoreboard.py` | Scoring calculations |
| `test_statistics.py` | Statistics updates and persistence behavior |

The exact test coverage depends on the implemented test cases.

### 25.2 Unit Testing

Individual modules should be tested independently whenever possible.

For example:

```text
Validator
    |
    v
test_validator.py
```

```text
ScoreBoard
    |
    v
test_scoreboard.py
```

```text
WordManager
    |
    v
test_word_manager.py
```

Unit tests should cover expected results, invalid inputs, boundary conditions, and failure scenarios.

### 25.3 Integration Testing

Unit tests alone cannot establish that the complete application works correctly.

Integration tests should verify interactions between:

- The application and engine.
- The engine and renderer.
- The engine and validator.
- The engine and word manager.
- The engine and scoring system.
- The engine and save system.
- The engine and statistics.
- The persistence components and JSON files.

A successful end-to-end test should confirm that the application can start, complete a game, handle a result, and persist supported data without errors.

## 26. Mocking and Isolation

Some components interact with external or environment-dependent behavior.

Examples include:

- Terminal input.
- Terminal output.
- File operations.
- Timers.
- Random word selection.
- Animation delays.

Tests can replace these dependencies with controlled mock objects or test fixtures.

For example, a test verifying that a correct guess updates the score should not need to wait for a real animation or read input from a physical keyboard.

### 26.1 Recommended Test Practices

- Use temporary files for persistence tests.
- Mock random selection when testing deterministic behavior.
- Replace interactive input with controlled test values.
- Avoid unnecessary sleep calls in automated tests.
- Reset shared state between tests.
- Verify that invalid input does not corrupt game state.
- Verify that saved data can be loaded back into a valid state.

## 27. Documentation Architecture

Technical documentation is stored in:

```text
docs/
├── architecture.md
├── main.md
├── game.md
├── utils.md
├── assets.md
├── data.md
└── tests.md
```

Each document focuses on a particular part of the project.

| Document | Purpose |
|---|---|
| `architecture.md` | Overall structure, layers, and component relationships |
| `main.md` | Application entry point and menu flow |
| `game.md` | Game systems and gameplay responsibilities |
| `utils.md` | Shared utility functions and file operations |
| `assets.md` | Static resources and terminal presentation assets |
| `data.md` | Word databases, statistics, and saved game data |
| `tests.md` | Test organization and verification practices |

Documentation should be updated when module responsibilities, public methods, file formats, or architectural dependencies change.

Documentation describes the intended design, but it should not be treated as proof that a feature has been implemented or tested.

## 28. Error Handling Architecture

Errors should be handled at the level that understands how to respond to them.

### 28.1 File-Related Errors

The file manager should handle or report errors related to reading, writing, deleting, or creating files.

Examples include:

- Missing files.
- Invalid JSON.
- Permission errors.
- Invalid paths.
- Failed write operations.

Higher-level components can then decide whether to create defaults, retry, display a message, or stop the affected operation.

### 28.2 Input-Related Errors

The validator should identify invalid player input and provide a predictable result.

Invalid input should not unexpectedly alter the player's score, remaining lives, or current word.

### 28.3 Gameplay Errors

The engine should handle gameplay-level decisions, such as whether a game can continue after a particular condition.

It should avoid treating every unexpected error as an ordinary incorrect guess.

### 28.4 Error Handling Principles

- Handle expected errors explicitly.
- Avoid silently discarding important failures.
- Provide useful messages to the user.
- Keep low-level utilities independent of gameplay decisions.
- Preserve valid state when an operation fails.
- Test important failure scenarios.

## 29. Configuration Architecture

Configuration belongs in the module responsible for the behavior it controls.

### 29.1 Application-Wide Constants

File:

```text
utils/constants.py
```

Contains values shared across the application, such as default names and reusable configuration constants.

### 29.2 Difficulty Configuration

File:

```text
game/difficulty.py
```

Contains difficulty levels and their associated settings.

### 29.3 Game Mode Configuration

File:

```text
game/game_mode.py
```

Contains game mode definitions and their settings.

### 29.4 Data File Configuration

Word database paths, statistics paths, and save paths should be defined or resolved consistently.

Path handling should not depend unnecessarily on the current working directory. Where appropriate, use paths derived from the project location or a centralized configuration.

## 30. Extensibility

The architecture allows new functionality to be added through the appropriate components.

### 30.1 Adding a Difficulty

Update:

```text
game/difficulty.py
```

Depending on the implementation, this may require:

- Adding a difficulty enum value.
- Defining its settings.
- Providing a word database.
- Updating selection or validation logic where needed.
- Adding corresponding tests.
- Updating documentation.

### 30.2 Adding a Game Mode

Update:

```text
game/game_mode.py
```

Implement the mode's behavior in the appropriate gameplay components.

Also review timer handling, game progression, save behavior, menus, tests, and documentation as applicable.

Adding an enum value alone does not implement a complete game mode.

### 30.3 Adding Words

Add or modify the appropriate JSON word database.

Ensure that the data follows the format expected by `game/word_manager.py`.

### 30.4 Adding a Visual Effect

Update:

```text
utils/animations.py
```

Connect the effect to the renderer without making the animation responsible for gameplay decisions.

### 30.5 Adding a New Screen

Update the appropriate methods in:

```text
game/renderer.py
```

If the screen introduces new application navigation, update `main.py` as well.

### 30.6 Adding a Persistent Field

Update the save structure in:

```text
game/save_system.py
```

Also review engine serialization and restoration, default values, backward compatibility where required, and associated tests.

### 30.7 Adding a New Statistic

Update the statistics component, its persisted data structure, the appropriate game-completion flow, and the corresponding tests.

## 31. Architectural Rules

The following rules should be maintained as the project evolves.

### Rule 1 — Keep Application Startup in `main.py`

The entry point should initialize and coordinate the application rather than duplicate gameplay logic.

### Rule 2 — Keep Game-Specific Logic in `game/`

Game rules and game-specific state belong in the game package.

### Rule 3 — Keep Generic Functionality in `utils/`

Reusable utility functions should not depend on high-level gameplay components.

### Rule 4 — Keep Static Visual Resources in `assets/`

ASCII artwork, terminal colors, and similar presentation resources belong in the assets package.

### Rule 5 — Keep Persistent Files in `data/`

Word databases, statistics, and saved game files should remain in the designated data directory.

### Rule 6 — Keep Automated Tests in `tests/`

Tests should remain separate from production modules.

### Rule 7 — Keep Technical Documentation in `docs/`

Architecture and module documentation should remain separate from executable code.

### Rule 8 — Avoid Circular Dependencies

Modules should not depend on each other in a way that creates circular imports.

### Rule 9 — Avoid Duplicated Business Logic

A rule owned by a specialized component should not be independently reimplemented throughout the engine.

### Rule 10 — Keep the Engine Focused on Orchestration

The engine should coordinate systems rather than becoming a collection of unrelated utilities.

### Rule 11 — Keep Save and Load Schemas Consistent

Save creation, serialization, and restoration should agree on required fields and valid state.

### Rule 12 — Update Tests When Behavior Changes

Changes to gameplay rules, data formats, and module interfaces should trigger a review of the corresponding tests.

### Rule 13 — Keep Documentation Synchronized

Changes to the directory structure, module responsibilities, or supported game modes should be reflected in the documentation.

### Rule 14 — Verify Integration Before Release

A modular codebase is not complete merely because its individual files exist. Imports, method calls, data formats, and end-to-end behavior must work together.

## 32. Integration and Consistency Checks

Before considering the architecture fully implemented, verify the following areas.

### 32.1 Game Mode Consistency

The game mode enum, application menus, engine configuration, and game mode manager must use the same supported mode names.

The documented modes are:

```text
CLASSIC
TIMED
ENDLESS
DAILY
```

If another name, such as `SURVIVAL`, appears in application code, either implement it consistently or change the application to use a supported mode.

### 32.2 Application Method Consistency

Every method called by `main.py` must exist on the relevant object or be replaced with the correct implemented interface.

For example, leaderboard functionality should not be called through the engine unless the corresponding method is implemented.

### 32.3 Save Schema Consistency

Check that:

- Default saves contain the fields expected by the engine.
- Saving writes all necessary state.
- Loading handles missing or malformed data.
- A saved game can be restored without missing-key errors.
- The restored state behaves correctly when play resumes.

### 32.4 Guess Processing Consistency

Verify that each guess updates the game state once.

Correct letters, incorrect guesses, scoring, remaining lives, and victory or defeat checks should not be updated redundantly.

### 32.5 Game Completion Consistency

Victory, defeat, and timeout should lead to a single completed-game result.

Statistics and final scoring should not be recorded more than once for the same game.

### 32.6 Data Path Consistency

Verify that the word manager, save system, statistics component, and file manager resolve paths consistently regardless of the directory from which the application is launched.

### 32.7 Test and Runtime Consistency

Run the automated tests and manually exercise the main application flows.

A successful test run is evidence of the tested behavior, not proof that every possible runtime path is correct.

## 33. Overall Architecture Diagram

The following diagram summarizes the major components and their intended relationships.

```text
                         Advanced Hangman
                                |
                                v
                             main.py
                                |
                                v
                       +------------------+
                       |      Engine      |
                       +------------------+
                                |
             +------------------+------------------+
             |                  |                  |
             v                  v                  v
           Player           WordManager         Validator
             |                  |                  |
             +------------------+------------------+
                                |
                 +--------------+--------------+
                 |              |              |
                 v              v              v
             ScoreBoard      GameTimer       Renderer
                 |                             |
                 |                             v
                 |                        Terminal UI
                 |
                 +------------------+
                                    |
                       +------------+------------+
                       |                         |
                       v                         v
                  Statistics                 SaveSystem
                       |                         |
                       +------------+------------+
                                    |
                                    v
                                FileManager
                                    |
                                    v
                                   data/
                                    |
                     +--------------+--------------+
                     |              |              |
                     v              v              v
                 Word JSONs    statistics.json  savegame.json


              Presentation and Shared Support
                           |
                +----------+----------+
                |                     |
                v                     v
             assets/                utils/
                |                     |
                +----------+----------+
                           |
                           v
                        Renderer


                       Verification
                           |
                           v
                         tests/


                       Documentation
                           |
                           v
                          docs/
```

This is a conceptual diagram of the system. The exact call relationships and dependency graph should be confirmed from the implementation.

## 34. Final Architectural Summary

Advanced Hangman is organized around a central gameplay engine supported by specialized game components and reusable utilities.

The intended application flow is:

```text
main.py
   |
   v
Engine
   |
   v
Specialized Game Systems
   |
   v
Utilities and Resources
   |
   v
Persistent Data
```

The engine coordinates the game, while individual components have clearly defined responsibilities.

```text
Player        -> Player information
WordManager   -> Word selection and word data
Validator     -> Input validation
ScoreBoard    -> Scoring
Statistics    -> Long-term performance records
SaveSystem    -> Saved game state
GameTimer     -> Time tracking
Difficulty    -> Difficulty configuration
GameMode      -> Game mode configuration
Renderer      -> Terminal presentation
FileManager   -> Low-level file operations
```

The supporting directories provide:

```text
assets/  -> Static visual resources
utils/   -> Reusable utility functionality
data/    -> Word databases and persistent information
tests/   -> Automated verification
docs/    -> Technical documentation
```

The main architectural principle is separation of concerns. Each module should have a clear responsibility, dependencies should remain manageable, and data should move between components through consistent interfaces.

This structure provides a maintainable foundation for future development. Its effectiveness ultimately depends on keeping the implementation, tests, data formats, and documentation synchronized.

