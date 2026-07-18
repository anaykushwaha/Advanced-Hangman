# main.py 
# Entry point for the game 

# Responsible for: 
# 1. Initializating the application 
# 2. Displays menus 
# 3. Creating the game engine 
# 4. Collecting user choices 
# 5. Starting gameplay 

from __future__ import annotations 
import sys 
from game.engine import Engine 
from game.difficulty import Difficulty 
from game.game_mode import GameMode 

from utils.banner import (
    print_banner, 
    print_goodbye 
) 

from utils.helper import clear_screen 

from utils.constants import DEFAULT_PLAYER_NAME 

class HangmanApplication: 
    # Main application controller 
    # Responsible for managing menus and delegating gameplay to the Engine 

    def __init__(self) -> None: 
        self.engine = Engine() 
        self.running = True 
    

    ## Startup 
    
    def start(self) -> None: 
        # Starts the appliation 

        clear_screen() 
        print_banner() 
        self.main_menu() 
    
    def quit(self) -> None: 
        # Exists the application 

        print_goodbye() 
        self.running = False 
        sys.exit() 
    

    ## Main menu 

    def main_menu(self) -> None: 
        # Displays the main menu 

        while self.running: 
            clear_screen() 
            print_banner() 
            print("=" * 50) 
            print("              MAIN MENU") 
            print("=" * 50) 
            print() 
            print("1. New Game") 
            print("2. Continue Saved Game") 
            print("3. Statistics") 
            print("4. Leaderboard") 
            print("5. Help") 
            print("6. Settings") 
            print("7. Quit") 
            print() 

            choice = input("Select an option: ") 
            self.handle_main_menu(choice) 
    
    def handle_main_menu(self, choice: str) -> None: 
        # Handles the selected menu option 

        match choice: 
            case "1": 
                self.new_game_menu() 
            case "2": 
                self.engine.continue_game() 
            case "3": 
                self.engine.show_statistics() 
            case "4": 
                self.engine.show_leaderboard() 
            case "5": 
                self.engine.show_help() 
            case "6": 
                self.engine.show_settings() 
            case "7": 
                self.quit() 
            case _: 
                print() 
                print("Invalid selection.") 
                input("\nPress Enter to continue...") 
    
    
    ## New game setup

    def new_game_menu(self) -> None: 
        # Collects all information required to start a new game 

        clear_screen() 
        print_banner() 
        print("=" * 50) 
        print("              NEW GAME") 
        print("=" * 50) 
        print() 

        player_name = self.get_player_name() 
        difficulty = self.select_difficulty() 
        game_mode = self.select_game_mode() 
        self.engine.create_new_game(
            player_name, 
            difficulty, 
            game_mode, 
        ) 

    def get_player_name(self) -> str: 
        # Prompts the player to enter their name 

        print() 

        name = input("Enter your name: ") 
        if not name: 
            return DEFAULT_PLAYER_NAME 
        return name 

    def select_difficulty(self) -> Difficulty: 
        # Allows the player to choose a difficulty 

        while True: 
            clear_screen() 
            print_banner() 
            print ("=" * 50) 
            print ("           SELECT DIFFICULTY") 
            print ("=" * 50) 
            print () 
            print ("1. Easy") 
            print ("2. Medium") 
            print ("3. Hard") 
            print ("4. Impossible") 
            print () 

            choice = input("Choice: ") 
            mapping = {
                "1": Difficulty.EASY, 
                "2": Difficulty.MEDIUM, 
                "3": Difficulty.HARD, 
                "4": Difficulty.IMPOSSIBLE, 
            } 

            difficulty = mapping.get(choice) 

            if difficulty: 
                return difficulty 
            print () 
            print ("Invalid selection.") 

            input ("\nPress Enter to continue...") 

    def select_game_mode(self) -> GameMode: 
        # Allows the player to choose a game 

        while True: 
            clear_screen() 
            print_banner() 
            print ("=" * 50) 
            print ("            GAME MODE") 
            print ("=" * 50) 
            print () 
            print ("1. Classic") 
            print ("2. Timed") 
            print ("3. Survival") 
            print () 

            choice = input ("Choice: ") 

            mapping = { 
                "1": GameMode.CLASSIC, 
                "2": GameMode.TIMED, 
                "3": GameMode.SURVIVAL, 
            } 

            mode = mapping.get(choice) 

            if mode: 
                return mode 
            print () 
            print ("Invalid selection.") 
            input ("\nPress Enter to continue...") 
    

## Application entry point 

    def main() -> None: 
        # Entry point for the game application 

        application = HangmanApplication() 

        try: 
            application.start() 
        except KeyboardInterrupt: 
            print () 
            print ("\nExiting Advanced Hangman...") 
            application.quit() 
        except Exception as error: 
            print () 
            print ("An unexpected error occurred.") 
            print (error) 
            input ("\nPress Continue to exit...") 

    if __name__ == "__main__": 
        main() 

