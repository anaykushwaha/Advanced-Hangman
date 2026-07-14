# validator.py 
# Contains all validation logic used throughout the game 

# Every method returns True / False or raises 
# a ValueError where appropriate 

from __future__ import annotations 
import string 

from utils.constants import (
    VALID_LETTERS,
    VALID_MENU_INPUT,
    YES_RESPONSES,
    NO_RESPONSES,
    QUIT_COMMANDS,
    SAVE_COMMAND,
    LOAD_COMMAND,
    HINT_COMMAND,
) 

class Validator: 
    # Static validation methods 

    ## Letter validation 

    @staticmethod 
    def normalize_letter(letter: str) -> str: 
        # Converts input into uppercase and removes surrounding whitespace 

        return letter.strip().upper() 
    
    @staticmethod 
    def is_single_letter(letter: str) -> bool: 
        # Returns True if input is exactly one letter 

        letter = Validator.normalize_letter(letter) 

        return len(letter) == 1 and letter in VALID_LETTERS 
    
    @staticmethod 
    def validate_letter(letter: str) -> str: 
        # Returns a validated uppercase letter 
        # Raises ValueError 

        letter = Validator.normalize_letter(letter) 

        if not Validator.is_single_letter(letter): 
            raise ValueError(
                "Please enter exactly one letter" 
            ) 
        
        return letter 
    
    @staticmethod 
    def already_guessed(
        letter: str, 
        correct_letters: set[str], 
        wrong_letters: set[str] 
    ) -> bool: 
        # Returns True if the letter has already been guessed 

        letter = Validator.normalize_letter(letter) 

        return (
            letter in correct_letters 
            or letter in wrong_letters 
        ) 
    

    ## Menu validation 

    @staticmethod 
    def valid_menu_choice(choice: str) -> bool: 
        # Checks if a menu option is valid 

        return choice.strip() in VALID_MENU_INPUT 
    

    ## Yes or No 

    @staticmethod 
    def is_yes(text: str) -> bool: 
        return (
            text.strip().upper() 
            in YES_RESPONSES 
        ) 
    
    @staticmethod 
    def is_no(text: str) -> bool: 
        return (
            text.strip().upper() 
            in NO_RESPONSES 
        ) 
    
    
    ## Commands 

    @staticmethod 
    def is_quit(text: str) -> bool: 
        return (
            text.strip().upper() 
            in QUIT_COMMANDS 
        ) 
    
    @staticmethod 
    def is_save(text: str) -> bool: 
        return (
            text.strip().upper() 
            == SAVE_COMMAND 
        ) 
    
    @staticmethod 
    def is_load(text: str) -> bool: 
        return (
            text.strip().upper() 
            == LOAD_COMMAND 
        ) 
    
    @staticmethod 
    def is_hint(text: str) -> bool: 
        return (
            text.strip().upper() 
            == HINT_COMMAND 
        ) 
    

    ## Names 

    @staticmethod 
    def validate_player_name(name: str) -> str: 
        # Cleans and validates the player's name 

        name = name.strip() 

        if len(name) == 0: 
            raise ValueError(
                "Player name cannot be empty" 
            ) 
        
        if len(name) > 20: 
            raise ValueError(
                "Player name must be 20 characters or fewer" 
            ) 
        
        allowed = (
            string.ascii_letters 
            + string.digits 
            + " _-" 
        ) 

        for character in name: 
            if character not in allowed: 
                raise ValueError(
                    "Player name contains invalid characters" 
                ) 
            
    
    ## Numbers 

    @staticmethod 
    def is_positive_number(text: str) -> bool: 
        # Returns True if the string is a positive integer 

        return (
            text.isdigit() 
            and int(text) > 0 
        ) 
    

    ## Words 

    @staticmethod 
    def validate_word(word: str) -> str: 
        # Validates a word loaded from JSON 

        word = word.strip().upper() 

        if len(word) == 0: 
            raise ValueError(
                "Word cannot be empty" 
            ) 
        
        allowed = (
            string.ascii_uppercase 
            + " '-" 
        ) 

        for character in word: 
            if character not in allowed: 
                raise ValueError(
                    f"Invalid character '{character}' in word" 
                ) 
        
        return word 
    

    ## Categories 

    @staticmethod 
    def validate_category(category: str) -> str: 
        # Cleans category names 

        category = category.strip() 

        if not category: 
            raise ValueError(
                "Category cannot be empty" 
            ) 
        
        return category 
    
    
    ## Generic 

    @staticmethod 
    def not_empty(text: str) -> bool: 
        # Returns True if the string contains non-whitespace characters 

        return len(text.strip()) > 0 

