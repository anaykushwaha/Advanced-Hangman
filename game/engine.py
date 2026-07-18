# engine.py 
# Core gameplay engine for the game 

# Engine class coordinates every subsystem of the game 
# It manages gameplay flow, player input, validation, scoring, 
# rendering, saving, statistics and win/loss conditions 

from __future__ import annotations 
from typing import Optional 
from game.player import Player 
from game.word_manager import WordManager 
from game.validator import Validator 
from game.scoreboard import ScoreBoard 
from game.statistics import Statistics 
from game.save_system import SaveSystem 
from game.timer import GameTimer 
from game.difficulty import Difficulty 
from game.game_mode import GameMode 
from game.renderer import Renderer 
from utils.constants import ( 
    MAX_HANGMAN_STAGE, 
    DEFAULT_PLAYER_NAME, 
) 

class Engine: 
    # Controls the complete gameplay loop 
    # Responsible for coordinating every other module in the project 

    ## Initialization 

    def __init__(self) -> None: 
        # Creates a new game engine 

        # Core systems 
        self.renderer = Renderer() 
        self.word_manager = WordManager() 
        self.validator = Validator() 
        self.scoreboard = ScoreBoard() 
        self.statistics = Statistics() 
        self.save_system = SaveSystem() 
        self.timer = GameTimer() 

        # Current player 
        self.player = Player(DEFAULT_PLAYER_NAME) 

        # Game configuration 
        self.difficulty = Difficulty.EASY 
        self.game_mode = GameMode.CLASSIC 

        # Current puzzle 
        self.word: str = "" 
        self.category: str = "" 
        self.display_word: str = "" 

        # Guess tracking 
        self.correct_letters: set[str] = set() 
        self.wrong_letters: set[str] = set() 

        # Game state 
        self.score = 0 
        self.hangman_stage = 0 
        self.remaining_lives = MAX_HANGMAN_STAGE 

        self.game_running = False 
        self.game_won = False 
        self.game_over = False 
    

    ## Game initialization 
    
    def reset_game(self) -> None: 
        # Resets the engine for a brand-new game 

        self.word = "" 
        self.category = "" 
        self.display_word = "" 

        self.correct_letters.clear() 
        self.wrong_letters.clear() 

        self.score = 0 
        self.hangman_stage = 0 
        self.remaining_lives = MAX_HANGMAN_STAGE 

        self.game_running = False 
        self.game_won = False 
        self.game_over = False 

        self.timer.reset() 
    
    def set_player(self, name: str) -> None: 
        # Creates a new player profile 

        self.player = Player(name) 
    
    def set_difficulty(self, difficulty: Difficulty) -> None: 
        # Sets the active difficulty 

        self.difficulty = difficulty 
    
    def set_game_mode(self, mode: GameMode) -> None: 
        # Sets the active game mode 

        self.game_mode = mode 

    def load_new_word(self) -> None: 
        # Retrieves a new puzzle from the WordManager 

        word, category = self.word_manager.get_random_word(
            self.difficulty 
        ) 

        self.word = word.upper() 
        self.category = category 

        self.display_word = (
            self.word_manager.create_display_word(
                self.word 
            ) 
        ) 
    
    def start_game(self) -> None: 
        # Starts a new game 

        self.reset_game() 
        self.load_new_word() 
        self.timer.start() 
        self.game_running = True 
    

    ## Core gameplay logic 

    def update_display_word(self) -> None: 
        # Updates the visible version of the word using the current correct guesses 

        self.display_word = (
            self.word_manager.create_display_word(
                self.word, 
                self.correct_letters, 
            ) 
        ) 

    def process_guess(self, guess: str) -> bool: 
        # Processes a player's guess 
        # Returns True if the guess was correct 

        guess = guess.upper() 

        if not self.validator.is_valid_letter(guess):
            return False 

        if (
            guess in self.correct_letters 
            or guess in self.wrong_letters 
        ): 
            return False 

        if guess in self.word: 
            self.handle_correct_guess(guess) 
            return True 

        self.handle_wrong_guess(guess) 
        return False 

    def handle_correct_guess(self, letter: str) -> None: 
        # Handles a correct guess 

        self.correct_letters.add(letter) 
        self.update_display_word() 
        occurrences = self.word.count(letter) 
        self.score += occurrences * 10 
    
    def handle_wrong_guess(self, letter: str) -> None: 
        # Handles an incorrect guess 

        self.wrong_letters.add(letter) 
        self.hangman_stage += 1 
        self.remaining_lives -= 1 

    def reveal_word(self) -> None: 
        # Reveals the complete word 

        self.display_word = self.word 

    def is_word_complete(self) -> bool: 
        # Returns True when every letter has been guessed 

        for character in self.word: 
            if character == " ": 
                continue 
            if character not in self.correct_letters: 
                return False 
        return True 

    def is_game_won(self) -> bool: 
        # Determines whether the player has won 

        return self.is_word_complete() 

    def is_game_over(self) -> bool: 
        # Determines whether the player has lost 

        return (
            self.hangman_stage 
            >= MAX_HANGMAN_STAGE 
        ) 

    def finish_game(self) -> None: 
        # Stops gameplay 

        self.game_running = False 
        self.game_over = True 
        self.timer.stop() 

    def finish_victory(self) -> None: 
        # Finalizes a winning game 

        self.game_won = True 
        self.finish_game() 

    def finish_defeat(self) -> None: 
        # Finalizes a losing game 

        self.game_won = False 
        self.reveal_word() 
        self.finish_game() 

    def elapsed_time(self) -> int: 
        # Returns the elapsed game time 

        return (self.timer.elapsed_seconds()) 

    def remaining_guess_count(self) -> int: 
        # Returns remaining guesses 

        return self.remaining_lives 

    def total_guesses(self) -> int: 
        # Returns the total number of guesses 

        return (len(self.correct_letters) + len(self.wrong_letters)) 
    
    ## Gameplay loop 

    def build_render_state(self) -> dict: 
        # Builds the current game state dictionary used by the renderer 

        return { 
            "player": self.player.name, 
            "difficulty": self.difficulty.name.title(), 
            "category": self.category, 
            "score": self.score, 
            "lives": self.remaining_lives, 
            "elapsed_time": self.elapsed_time(), 
            "hangman_stage": self.hangman_stage, 
            "display_word": self.display_word, 
            "correct_letters": sorted(self.correct_letters), 
            "wrong_letters": sorted(self.wrong_letters), 
        } 

    def render_game(self) -> None: 
        # Draws the complete game screen 

        self.renderer.draw_game_screen(
            **self.build_render_state() 
        ) 

    def get_player_guess(self) -> str: 
        # Prompts the player for a guess 

        return self.renderer.prompt_guess() 

    def process_turn(self) -> None: 
        # Processes one complete turn 

        guess = self.get_player_guess() 
        if not guess: 
            return 
        if (
            not self.validator.is_valid_letter(
                guess 
            ) 
        ): 
            self.renderer.error(
                "Please enter a single alphabetic letter" 
            ) 
            self.renderer.pause(1.2) 
            return 
        if (
            guess in self.correct_letters 
            or guess in self.wrong_letters 
        ): 
            self.renderer.warning(
                "You already guessed that letter" 
            ) 
            self.renderer.pause(1.2) 
            return 

        correct = self.process_guess(guess) 
        if correct: 
            self.renderer.success("Correct!") 
        else: 
            self.renderer.error("Incorrect!") 
        self.renderer.pause(0.8) 

    def update_game_state(self) -> None: 
        # Determines whether the game has ended after the latest guess 

        if self.is_game_won(): 
            self.finish_victory() 
            return 
        if self.is_game_over(): 
            self.finish_defeat() 

    def play(self) -> None: 
        # Runs the complete gameplay loop 

        self.game_running = True 
        while self.game_running: 
            self.render_game() 
            self.process_turn() 
            self.update_game_state() 
        self.end_game() 

    def end_game(self) -> None: 
        # Handles post-game processing 

        if self.game_won: 
            self.handle_victory() 
        else: 
            self.handle_defeat() 
    
    
    ## End Game Processing 

    def record_statistics(self) -> None: 
        # Records statistics for the completed game 

        self.statistics.record_game(
            won=self.game_won, 
            score=self.score, 
            difficulty=self.difficulty.name, 
            elapsed_time=self.elapsed_time(), 
            wrong_guesses=len(self.wrong_letters) 
        ) 

    def update_player_profile(self) -> None: 
        # Updates the player's profile 

        self.player.score = self.score 
        self.player.games_played += 1 
        if self.game_won: 
            self.player.games_won += 1 
        else: 
            self.player.games_lost += 1 

    def update_leaderboard(self) -> None: 
        # Adds the player's score to the leaderboard 

        self.scoreboard.add_score(
            self.player.name, 
            self.score, 
        ) 

    def save_statistics(self) -> None: 
        # Saves updated statstics 

        self.statistics.save() 

    def save_leaderboard(self) -> None: 
        # Saves the leaderboard 

        self.scoreboard.save() 

    def finalize_results(self) -> None: 
        # Performs every common end-game action 

        self.update_player_profile() 
        self.record_statistics() 
        self.update_leaderboard() 
        self.save_statistics() 
        self.save_leaderboard() 

    def handle_victory(self) -> None: 
        # Handles a completed victory 

        self.finalize_results() 

        self.renderer.draw_victory_screen(
            player=self.player.name, 
            word=self.word, 
            score=self.score, 
            elapsed_time=self.elapsed_time(), 
        ) 
        self.renderer.wait_for_key() 

    def handle_defeat(self) -> None: 
        # Handles a completed defeat 

        self.finalize_results() 
        self.renderer.draw_game_over_screen( 
            player=self.player.name, 
            word=self.word, 
            score=self.score, 
        ) 
        self.renderer.wait_for_key() 

    def show_statistics(self) -> None: 
        # Displays recorded statistics 

        self.renderer.draw_statistics_screen(self.statistics.export()) 
        self.renderer.wait_for_key() 

    def show_leaderboard(self) -> None: 
        # Displays leaderboard rankings 

        self.renderer.draw_leaderboard( 
            self.scoreboard.get_scores() 
        ) 
        self.renderer.wait_for_key() 
    

    ## Save / load system 

    def build_save_data(self) -> dict: 
        # Builds a dictionary containing the current game state 

        return {
            "player_name": self.player.name, 
            "difficulty": self.difficulty.name, 
            "game_mode": self.game_mode.name, 
            "word": self.word, 
            "category": self.category, 
            "display_word": self.display_word, 
            "correct_letters": sorted(self.correct_letters), 
            "wrong_letters": sorted(self.wrong_letters), 
            "score": self.score, 
            "hangman_stage": self.hangman_stage, 
            "remaining_lives": self.remaining_lives, 
            "elapsed_time": self.elapsed_time() 
        } 

    def save_game(self) -> bool: 
        # Saves the current game 
        # Returns True if successful 

        data = self.build_save_data() 
        success = self.save_system.save_game(data) 
        if success: 
            self.renderer.success(
                "Game saved successfully" 
            ) 
        else: 
            self.renderer.error(
                "Failed to save game" 
            ) 
        return success 

    def load_game(self) -> bool: 
        # Loads a previously saved game 
        # Returns True if successful 

        data = self.save_system.load_game() 
        if not data: 
            self.renderer.warning(
                "No save file found" 
            ) 
            return False 

        self.player = Player(data["player_name"]) 
        self.difficulty = Difficulty[data["difficulty"]] 
        self.game_mode = GameMode[data["game_mode"]] 
        self.word = data["word"] 
        self.category = data["category"] 
        self.display_word = data["display_word"] 
        self.correct_letters = set(data["correct_letters"]) 
        self.wrong_letters = set(data["wrong_letters"]) 
        self.score = data["score"] 
        self.hangman_stage = data["hangman_stage"] 
        self.remaining_lives = data["remaining_lives"] 
        self.timer.reset() 
        self.timer.start() 
        self.renderer.success("Save loaded successfully") 
        return True 

    def delete_save(self) -> bool: 
        # Deletes the current save file 

        success = (self.save_system.delete_save()) 

        if success: 
            self.renderer.success("Save deleted") 
        else: 
            self.renderer.warning("No save file exists") 
        return success 

    def autosave(self) -> None: 
        # Automatically saves the game 

        self.save_system.save_game(self.build_save_data()) 

    def has_saved_game(self) -> bool: 
        # Returns True if a save exists 

        return (
            self.save_system.save_exists() 
        ) 

    def continue_game(self) -> bool: 
        # Loads and resumes a saved game 

        if not self.load_game(): 
            return False 
        self.game_running = True 
        self.play() 
        return True 


    ## Menu & game setup

    def create_new_game(
        self, 
        player_name: str, 
        difficulty: Difficulty, 
        game_mode: GameMode, 
    ) -> None: 
        # Creates and starts a completely new game 

        self.set_player(player_name) 
        self.set_difficulty(difficulty) 
        self.set_game_mode(game_mode) 
        self.start_game() 
        self.play() 

    def pause_game(self) -> None: 
        # Displays the pause menu and processes the player's choice 

        while True: 
            self.renderer.draw_pause_screen() 
            choice = (
                self.renderer.prompt_menu_choice() 
            ) 
            match choice: 
                case "1": 
                    return 
                case "2": 
                    self.save_game() 
                    self.renderer.wait_for_key() 
                case "3": 
                    self.game_running = False 
                    return 
                case "4": 
                    self.finish_defeat() 
                    return 
                case _: 
                    self.renderer.warning("Invalid option") 
                    self.renderer.pause(1) 

    def choose_difficulty(self, choice: str) -> bool: 
        # Applies the selected difficulty 
        # Returns True if valid 

        mapping = {
            "1": Difficulty.EASY, 
            "2": Difficulty.MEDIUM, 
            "3": Difficulty.HARD, 
            "4": Difficulty.IMPOSSIBLE 
        } 

        difficulty = mapping.get(choice) 

        if difficulty is None: 
            return False 
        self.set_difficulty(difficulty) 
        return True 

    def choose_game_mode(self, choice: str) -> bool: 
        # Applies the selected game mode 
        # Returns True if valid 

        mapping = {
            "1": GameMode.CLASSIC, 
            "2": GameMode.TIMED, 
            "3": GameMode.SURVIVAL 
        } 

        mode = mapping.get(choice) 

        if mode is None: 
            return False 
        self.set_game_mode(mode) 
        return True 

    def show_help(self) -> None: 
        # Displays the help screen 

        self.renderer.draw_help_screen() 
        self.renderer.wait_for_key() 

    def show_settings(self) -> None: 
        # Displays the settings screen 
        # Additional configurable settings can easily be added here in the future 

        self.renderer.draw_settings_menu() 
        self.renderer.wait_for_key() 

    def reset_progress(self) -> None: 
        # Clears the current game state without affecting stored statistics 

        self.reset_game() 
        self.player = Player(DEFAULT_PLAYER_NAME) 

    def reset_everything(self) -> None: 
        # Restores the engine to its initial state 

        self.reset_progress() 
        self.statistics.reset() 
        self.scoreboard.clear() 
        self.save_system.delete_save() 

    def current_state(self) -> dict: 
        # Returns a snapshot of the engine's current state 

        return {
            "player": self.player.name, 
            "difficulty": self.difficulty.name, 
            "game_mode": self.game_mode.name, 
            "score": self.score, 
            "word": self.word, 
            "display_word": self.display_word, 
            "correct_letters": sorted(self.correct_letters), 
            "wrong_letters": sorted(self.wrong_letters), 

            "remaining_lives": (self.remaining_lives), 
            "game_running": (self.game_running), 
            "game_won": (self.game_won), 
            "game_over": (self.game_over) 
        } 
    

    #3 Utility methods

    def is_running(self) -> bool: 
        # Returns True while a game is active 

        return self.game_running 

    def has_won(self) -> bool: 
        # Returns True if the current game ended in victory 

        return self.game_won 

    def has_lost(self) -> bool: 
        # Returns True if the player has lost 

        return (
            self.game_over 
            and not self.game_won 
        ) 

    def guessed_letters(self) -> list[str]: 
        # Returns every guessed letter in the alphabetical order 

        return sorted(
            self.correct_letters.union(
                self.wrong_letters 
            ) 
        ) 

    def guess_count(self) -> int: 
        # Returns the total number of guesses 

        return len(self.correct_letters) + len(self.wrong_letters) 

    def accuracy(self) -> float: 
        # Returns the player's current guessing accuracy as a percentage 

        total = self.guess_count() 

        if total == 0: 
            return 0.0 
        return round((len(self.correct_letters) / total) * 100, 2) 

    def __str__(self) -> str: 
        # Returns a readable summary of the engine 

        return (
            "Engine(" 
            f"player={self.player.name}, " 
            f"difficulty={self.difficulty.name}, " 
            f"mode={self.game_mode.name}, " 
            f"score={self.score}, " 
            f"running={self.game_running}" 
            ")" 
        ) 

    def __repr__(self) -> str: 
        # Official representation of the engine 

        return self.__str__() 

