# renderer.py 
# Responsible for every visual element displayed during gameplay 

# Cannot contain gameplay logic 
# Receives information from the game engine and formats it into a polished terminal interface 

from __future__ import annotations 
from typing import Iterable 
from assets.colors import Colors 
from assets.hangman_frames import HangmanFrames 
from utils.animations import Animation 
from utils.banner import Banner 
from utils.constants import SCREEN_WIDTH 
from utils.helper import center_text 

class Renderer: 
    # Handles all rendering for Advanced Hangman 

    ## Initialization 

    def __init__(self) -> None: 
        self.width = SCREEN_WIDTH 

    
    ## Generic helpers 

    def clear(self) -> None: 
        # Clears the terminal 

        Animation.clear_screen() 
    
    def pause(self, seconds: float = 1.0) -> None: 
        Animation.pause(seconds) 
    
    def separator(self, character: str = "=") -> None: 
        print (character * self.width) 
    
    def blank_line(self, count: int = 1) -> None: 
        for x in range(count): 
            print () 
    
    def centered(
        self, 
        text: str, 
        color: str = Colors.RESET, 
    ) -> None: 
        # Prints centered colored text 

        print(
            color 
            + center_text( 
                text, 
                self.width, 
            ) 
            + Colors.RESET 
        ) 
    
    def title(self, text: str) -> None: 
        # Prints a formatted title 

        self.blank_line() 
        self.separator("=") 
        self.centered(
            text, 
            Colors.CYAN, 
        ) 
        self.separator("=") 
        self.blank_line() 
    
    def subtitle(self, text: str) -> None: 
        self.centered(
            text, 
            Colors.YELLOW 
        ) 
        self.separator("-") 
    
    
    ## Logo 

    def logo(self) -> None: 
        # Displays the game logo 

        Banner.show() 
    
    
    ## Menus 

    def menu_option(self, number: int, text: str) -> None: 
        print (
            f"{Colors.GREEN}" 
            f"[{number}]" 
            f"{Colors.RESET}" 
            f" {text}" 
        ) 
    
    def wait_for_enter(self) -> None: 
        input (
             f"\n{Colors.YELLOW}" 
            "Press ENTER to continue..." 
            f"{Colors.RESET}" 
        ) 
    
    def loading_screen(self, message: str = "Loading") -> None: 
        # Shows a loading animation 

        self.clear() 
        self.logo() 
        self.blank_line() 

        Animation.loading_bar(duration = 1.5) 
        self.centered(message, Colors.CYAN) 

        self.blank_line() 
    
    def message(self, text: str, color: str = Colors.WHITE) -> None: 
        # Prints a centered message 

        self.centered(text, color) 
    
    def succes(self, text: str) -> None: 
        self.message(text, Colors.GREEN) 
    
    def warning(self, text: str) -> None: 
        self.message(text, Colors.YELLOW) 
    
    def error(self, text: str) -> None: 
        self.message(text, Colors.RED) 
    
    def info(self, text: str) -> None: 
        self.message(text, Colors.CYAN) 
    

    ## Gameplay rendering 

    def draw_hangman(self, stage: int) -> None: 
        # Displays the current hangman frame 

        frame = HangmanFrames.get_frame(stage) 
        print (frame) 
    
    def draw_hidden_word(self, display_word: str) -> None: 
        # Displays the hidden word or phrase 

        print () 

        self.centered(display_word, Colors.BOLD + Colors.WHITE) 

        print () 
    
    def draw_category(self, category: str) -> None: 
        # Displays the category 

        print (
            f"{Colors.CYAN}" 
            f"Category: " 
            f"{Colors.RESET}" 
            f"{category}" 
        ) 
    
    def draw_difficulty(self, difficulty: str) -> None: 
        # Displays the active difficulty 

        print (
             f"{Colors.MAGENTA}" 
            f"Difficulty: " 
            f"{Colors.RESET}" 
            f"{difficulty}" 
        ) 
    
    def draw_score(self, score: int) -> None: 
        # Displays the player's score 

        print (
            f"{Colors.GREEN}" 
            f"Score: " 
            f"{Colors.RESET}" 
            f"{score}" 
        ) 
    
    def draw_timer(self, seconds: int) -> None: 
        # Displays elapsed game time 

        minutes = seconds // 60 
        remaining = seconds % 60 

        print (
              f"{Colors.YELLOW}" 
            f"Time: " 
            f"{Colors.RESET}" 
            f"{minutes:02}:{remaining:02}" 
        ) 
    
    def draw_remaining_lives(self, lives: int) -> None: 
        # Displays remaining lives 

        print (
              f"{Colors.RED}" 
            f"Lives: " 
            f"{Colors.RESET}" 
            f"{lives}" 
        ) 
    
    def draw_player(self, player_name: str) -> None: 
        # Displays the current player 

        print (
            f"{Colors.BLUE}" 
            f"Player: " 
            f"{Colors.RESET}" 
            f"{player_name}" 
        ) 
    
    def draw_correct_letters(self, letters: list[str]) -> None: 
        # Displays all correctly guessed letters 

        if not letters: 
            text = "-" 
        else: 
            text = ", ".join(sorted(letters)) 
        print (
            f"{Colors.GREEN}" 
            f"Correct Letters: " 
            f"{Colors.RESET}" 
            f"{text}" 
        ) 
    
    def draw_wrong_letters(self, letters: list[str]) -> None: 
        # Displays all incorrect guesses 

        if not letters: 
            text = "-" 
        else: 
            text = ", ".join(sorted(letters)) 
        print (
            f"{Colors.RED}" 
            f"Wrong Letters: " 
            f"{Colors.RESET}" 
            f"{text}" 
        ) 
    
    def draw_guess_count(self, guesses: int) -> None: 
        # Displays the total number of guesses 

        print (
            f"{Colors.CYAN}" 
            f"Total Guesses: " 
            f"{Colors.RESET}" 
            f"{guesses}" 
        ) 
    
    def promot_guess(self) -> str: 
        # Prompts the player for a letter 

        return input (
            f"\n{Colors.YELLOW}" 
            "Enter a letter: " 
            f"{Colors.RESET}" 
        ).strip().upper() 
    
    def prompt_menu_choice(self) -> str: 
        # Prompts the player for a menu selection 

        return input(
            f"\n{Colors.CYAN}" 
            "Choose an option: " 
            f"{Colors.RESET}" 
        ).strip() 
    

    ## Complete game screen rendering 

    def draw_status_game(
            self, 
            *, 
            player: str, 
            difficulty: str, 
            category: str, 
            score: int, 
            lives: int, 
            elapsed_time: int, 
    ) -> None: 
        # Displays the player's current status 

        self.separator() 
        self.draw_player(player) 
        self.draw_difficulty(difficulty) 
        self.draw_category(category) 
        self.draw_score(score) 
        self.draw_remaining_lives(lives) 
        self.draw_timer(elapsed_time) 
        self.separator() 
    
    def draw_letter_game(
            self, 
            correct: list[str], 
            wrong: list[str] 
    ) -> None: 
        # Displays both guessed letter lists 

        self.draw_correct_letters(correct) 
        self.draw_wrong_letters(wrong) 
    
    def draw_game_screen(
            self, 
            *, 
            player: str, 
            difficulty: str, 
            category: str, 
            score: int, 
            lives: int, 
            elapsed_time: int, 
            hangman_stage: int, 
            display_word: str, 
            correct_letters: list[str], 
            wrong_letters: list[str], 
    ) -> None: 
        # Draws the complete gameplay interface 

        self.clear() 
        self.logo() 
        self.blank_line() 
        self.draw_status_panel(
            player = player, 
            difficulty = difficulty, 
            category = category, 
            score = score, 
            lives = lives, 
            elapsed_time = elapsed_time 
        ) 

        print () 
        self.draw_hangman(hangman_stage) 

        print () 
        self.draw_hidden_word(display_word) 

        print () 
        self.draw_letter_panels(
            correct_letters, 
            wrong_letters 
        ) 

        self.blank_line() 
    
    def draw_pause_screen(self) -> None: 
        # Displays the pause menu 

        self.clear() 
        self.title("GAME PAUSED") 
        self.menu_option(1, "Resume Game") 
        self.menu_option(2, "Save Game") 
        self.menu_option(3, "Return to Main Menu") 
        self.menu_option(4, "Quit") 
    
    def draw_help_screen(self) -> None: 
        # Displays gameplay instructions 

        self.clear() 
        self.title("HOW TO PLAY") 

        instructions = [
            "Guess one letter at a time.", 
            "Correct guesses reveal every occurrence.", 
            "Incorrect guesses build the hangman.", 
            "Spaces are shown automatically.", 
            "Win by revealing every letter.", 
            "Lose when the hangman is complete." 
        ] 

        for line in instructions: 
            print (f" • {line}") 

        self.blank_line() 
    
    def draw_statistics_summary(
            self, 
            *, 
            games_played: int, 
            wins: int, 
            losses: int, 
            win_rate: float, 
            highest_score: int, 
    ) -> None: 
        # Displays a short statistics summary 

        self.title("STATISTICS") 

        print (
            f"Games Played : {games_played}" 
        ) 
        print (
            f"Wins         : {wins}" 
        ) 
        print (
            f"Losses       : {losses}" 
        ) 
        print (
            f"Win Rate     : {win_rate:.1f}%" 
        ) 
        print (
            f"Highest Score: {highest_score}"  
        ) 
        self.blank_line() 
    
    def draw_player_summary(
            self, 
            *, 
            player: str, 
            score: int, 
            streak: int 
    ) -> None: 
        # Displays player information 

        self.title("PLAYER") 
        print (f"Name   : {player}") 
        print (f"Score  : {score}") 
        print (f"Streak : {streak}") 
        self.blank_line() 
    
    def draw_confirmation(self, message: str) -> None: 
        # Displays a confirmation prompt 
        # Returns True for yes 

        choice = input (
            f"{message} (Y/N)" 
        ).strip().upper() 

        return choice == "Y" 
    
    def draw_notification(self, message: str, color: str = Colors.CYAN) -> None: 
        # Displays a centered notification 

        self.blank_line() 
        self.centered(
            message, 
            color 
        ) 
        self.blank_line() 
    

    ## Main menu screens 

    def draw_main_menu(self) -> None: 
        # Displays the main menu 

        self.clear() 
        self.logo() 
        self.blank_line() 
        self.title("MAIN MENU") 
        self.menu_option(1, "New Game") 
        self.menu_option(2, "Continue Game") 
        self.menu_option(3, "Statistics") 
        self.menu_option(4, "Leaderboard") 
        self.menu_option(5, "Settings") 
        self.menu_option(6, "Help") 
        self.menu_option(7, "Quit") 
        self.blank_line() 
    
    def draw_new_game_menu(self) -> None: 
        # Displays the new game menu 

        self.clear() 
        self.title("NEW GAME") 
        self.menu_option(1, "Classic Mode") 
        self.menu_option(2, "Timed Mode") 
        self.menu_option(3, "Challenge Mode") 
        self.menu_option(4, "Back") 
        self.blank_line() 
    
    def draw_difficulty_menu(self) -> None: 
        # Displays the difficulty selection menu 

        self.clear() 

        self.title("SELECT DIFFICULTY") 
        self.menu_option(1, "Easy") 
        self.menu_option(2, "Medium") 
        self.menu_option(3, "Hard") 
        self.menu_option(4, "Impossible") 
        self.menu_option(5, "Back") 
        self.blank_line() 
    
    def draw_game_mode_menu(self) -> None: 
        # Displays available game modes 

        self.clear() 

        self.title("GAME MODES") 
        self.menu_option(1, "Classic") 
        self.menu_option(2, "Timed") 
        self.menu_option(3, "Survival") 
        self.menu_option(4, "Back") 
        self.blank_line() 
    
    def draw_continue_menu(self, player_name: str) -> None: 
        # Displays the continue game screen 

        self.clear() 

        self.title("CONTINUE GAME") 
        print(f"Saved Player : {player_name}") 
        self.blank_line() 
        self.menu_option(1, "Continue") 
        self.menu_option(2, "Delete Save") 
        self.menu_option(3, "Back") 
        self.blank_line() 
    
    def draw_settings_menu(self) -> None: 
        # Displays the settings screen 

        self.clear() 

        self.title("SETTINGS") 
        self.menu_option(1, "Toggle Animations") 
        self.menu_option(2, "Change Colors") 
        self.menu_option(3, "Reset Statistics") 
        self.menu_option(4, "Back") 
        self.blank_line() 
    

    ## End game screens 

    def draw_victory_menu(
            self, 
            *, 
            player: str, 
            word: str, 
            score: int, 
            elapsed_time: int 
    ) -> None: 
        # Displays the victory screen 

        self.clear() 

        Animation.victory_animation() 
        self.title("YOU WIN!") 
        print(f"Player : {player}") 
        print(f"Word   : {word}") 
        print(f"Score  : {score}") 
        self.draw_timer(elapsed_time) 
        self.blank_line() 
        self.success("Congratulations!") 
    
    def draw_game_over_screen(
            self, 
            *, 
            player: str, 
            word: str, 
            score: int  
    ) -> None: 
        # Displays the defeat screen 

        self.clear() 

        Animation.game_over_animation() 
        self.title("GAME OVER") 
        print(f"Player : {player}") 
        print(f"Answer : {word}") 
        print(f"Score  : {score}") 
        self.blank_line() 
        self.error("Better luck next time!") 
    
    def draw_final_score(self, score: int) -> None: 
        # Displays the player's final score 

        self.title("FINAL SCORE") 

        self.centered(
            str(score), 
            Colors.GREEN 
        ) 
        self.blank_line() 
    
    def draw_leaderboard(self, leaderboard: list[tuple[str, int]]) -> None: 
        # Displays the leaderboard 

        self.title("LEADERBOARD") 
        if not leaderboard: 
            self.warning(
                "No scores available" 
            ) 
            return 
        
        print (
            f"{'Rank':<6}" 
            f"{'Player':<20}" 
            f"{'Score':>10}" 
        ) 

        self.separator("-") 

        for index, (
            player, 
            score 
        ) in enumerate (
            leaderboard, 
            start = 1 
        ): 
            print (
                f"{index:<6}" 
                f"{player:<20}" 
                f"{score:>10}" 
            ) 
        self.blank_line() 
    
    def draw_statistics_screen(self, statistics: dict) -> None: 
        # Displays every recorded statistic 

        self.title("STATISTICS") 

        if not statistics: 
            self.warning(
                "No statistics available" 
            ) 
            return 

        for key, value in statistics.items(): 
            print (
                f"{key:<30}: {value}" 
            ) 

        self.blank_line() 
    
    def draw_box(self, title: str, lines: list[str]) -> None: 
        # Displays a formatted information box 

        width = 60 
        print ("+" + "-" * width + "+") 
        print (
            "|" 
            + title.center(width) 
            + "|" 
        ) 
        print ("+" + "-" * width + "+")

        for line in lines: 
            print (
                "| " 
                + line.ljust(width - 2) 
                + "|" 
            ) 
        print ("+" + "-" * width + "+") 

        self.blank_line() 
    
    def draw_footer(self, text: str) -> None: 
        # Displays a center footer 

        self.separator("-") 

        self.centered(
            text, 
            Colors.YELLOW 
        ) 

        self.separator("-") 
    

    ## Dialog boxes 

    def draw_info_boxes(self, message: str) -> None: 
        # Displays an informational message box 

         self.draw_box(
            "INFORMATION", 
            [message], 
        ) 
    
    def draw_success_box(self, message: str) -> None: 
        # Displays a success message box 

          self.draw_box(
            "SUCCESS", 
            [message], 
        ) 
    
    def draw_warning_box(self, message: str) -> None: 
        # Displays a warning message box 

        self.draw_box(
            "WARNING", 
            [message], 
        ) 
    
    def draw_error_box(self, message: str) -> None: 
        # Displays an error message box 

        self.draw_box(
            "ERROR", 
            [message], 
        ) 
    

    ## Miscellaneous screens 

    def draw_goodbye_screen(self) -> None: 
        # Displays the goodbye screen 

        self.clear() 

        self.logo() 
        self.blank_line() 
        self.title("GOODBYE") 
        self.centered(
            "Thank you for playing", 
            Colors.GREEN, 
        ) 

        self.centered(
            "Advanced Hangman!", 
            Colors.CYAN, 
        ) 

        self.blank_line() 

        Animation.type_text(
            "See you next time...", 
            delay = 0.03, 
        ) 
    
    def draw_credits_screen(self) -> None: 
        # Displays the project credits 

        self.clear() 

        self.title("CREDITS") 
        credits = [
            "Advanced Hangman", 
            "", 
            "Developed in Python", 
            "Created as a portfolio project.", 
            "", 
            "ASCII Art", 
            "JSON Data", 
            "Terminal Rendering", 
            "Statistics System", 
            "Save System", 
            "Thank you for playing!" 
        ] 

        for line in credits: 
            self.centered(
                line, 
                Colors.WHITE, 
            ) 

        self.blank_line() 
    
    def wait_for_key(self) -> None: 
        # Waits for the user before continuing 

        input (
            "\nPress ENTER to continue..." 
        ) 
    
    def splash_screen(self) -> None: 
        # Displays the game's splash screen 

        self.clear() 

        self.logo() 
        self.blank_line() 
        Animation.loading_bar(
            duration = 1.5, 
        ) 

        self.blank_line() 
    
    def __str__(self) -> None: 
        # Returns a summary of the renderer 

        return (
            f"Renderer(" 
            f"width={self.width})" 
        ) 
    
    def __repr__(self) -> None: 
        # Official representation 
        return self.__str__() 

