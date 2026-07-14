# helper.py 
# General helper functions used throughout the game 
# Only place generic utility functions are used 

# None of the following are done here: 
# 1. validation 
# 2. rendering 
# 3. animations 
# 4. file handling 

from __future__ import annotations 
import os 
import random 
import shutil 
import textwrap 
from typing import Iterable, Sequence, TypeVar 

T = TypeVar("T") 


## Terminal 

def clear_screen() -> None: 
    # Clears the terminal screen 

    os.system("cls" if os.name == "nt" else "clear") 

def terminal_width(default: int = 80) -> int: 
    # Returns the terminal width 

    return shutil.get_terminal_size(
        fallback = (default, 25) 
    ).columns 

def center(text: str, width: int | None = None) -> str: 
    # Centers a string 

    if width is None: 
        width = terminal_width() 

    return text.center(width) 

def separator(
        character: str = "=", 
        width: int | None = None
) -> None: 
    # Creates a separator line 

    if width is None: 
        width = terminal_width(width) 

    return character * width 


## Text 

def wrap(
        text: str, 
        width: int = 70
) -> str: 
    # Wraps text 

    return textwrap.fill(
        text, 
        width = width 
    ) 

def title_case(text: str) -> str: 
    # Converts text to title case 

    return text.title() 

def normalize(text: str) -> str: 
    # Removes surrounding whitespace 

    return text.strip() 


## Random 

def choose(items: Sequence[T]) -> T: 
    # Returns a random line 

    return random.choice(items) 

def shuffle(items: list[T]) -> None: 
    # Shuffles a list in-place 

    random.shuffle(items) 


## Numbers 

def clamp(
        value: int, 
        minimum: int, 
        maximum: int
) -> int: 
    # Restricts a value to a range 

    return max(
        minimum, 
        min(value, maximum) 
    ) 

def percentage(
        value: float, 
        total: float 
) -> float: 
    # Returns a percentage 

    if total == 0: 
        return 0.0 
    return (value / total) * 100 


#3 Collections 

def sorted_letters(letters: Iterable[str]) -> list[str]: 
    # Returns sorted uppercase letters 

    return sorted(
        letter.upper()
        for letter in letters 
    ) 

def comma_join(items: Iterable[str]) -> str: 
    # Joins strings using commas 

    return ", ".join(items) 


## User input 

def pause(message: str = "Press Enter to continue") -> None: 
    # Waits for the user 

    input (message) 

def ask_yes_no(message: str) -> bool: 
    # Prompts the user until a valid yes/no answer is received 

    while True: 
        answer = input(
            f"{message} (Y/N): "
        ).strip().upper() 

        if answer in ("Y", "YES"): 
            return True 
        
        if answer in ("N", "NO"): 
            return False 
        
        print ("Please enter Y or N") 


## Display 

def print_centered(text: str, width: int | None = None) -> None: 
    # Prints centered text 

    print (center(text, width)) 

def print_header(title: str, width: int | None = None) -> None: 
    # Prints a simple section header 

    if width is None: 
        width = terminal_width(width) 

    print (separator("=", width)) 
    print (title.center(width)) 
    print (separator("=", width)) 

