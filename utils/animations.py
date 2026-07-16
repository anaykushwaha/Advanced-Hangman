# animations.py 
# Provides simple terminal animations for the game 

# These animations improve the overall user experience by making menus, victories, defeats, 
# loading screens and text transitions feel much more polished in general 

from __future__ import annotations 
from typing import Iterable 
import itertools 
import sys 
import time 
import os 

class Animation: 
    DEFAULT_DELAY = 0.05 

    @staticmethod 
    def clear_screen() -> None: 
        # Clears the terminal 

        os.system(
            "cls" if os.name == "nt" else "Clear" 
        ) 
    
    @staticmethod 
    def pause(seconds: float = 1.0) -> None: 
        # Pauses execution 

        time.sleep(seconds) 
    
    @staticmethod 
    def type_text(text: str, delay: float = DEFAULT_DELAY, end: str = "\n") -> None: 
        # Prints text one character at a time 

        for character in text: 
            print(
                character, 
                end = "", 
                flush = True 
            ) 

            time.sleep(delay) 
        print (end = end) 
    
    @staticmethod 
    def print_lines(lines: Iterable[str], delay: float = 0.15) -> None: 
        # Prints multiple lines with a delay between each line 

        for line in lines: 
            print (line) 
            time.sleep(delay) 
    
    @staticmethod 
    def spinner(duration: float = 2.0, message: str = "Loading") -> None: 
        # Displays a rotating loading spinner 

        end_time = time.time() + duration 

        spinner = itertools.cycle(
            ["|", "/", "-", "\\"] 
        ) 

        while time.time() < end_time: 
            sys.stdout.write(
                f"\r{message} {next(spinner)}" 
            ) 
            sys.stdout.flush() 
            time.sleep(0.1) 
        sys.stdout.write("\r" + " " * 30) 
        sys.stdout.write("\r") 
    
    @staticmethod 
    def countdown(seconds: int = 3) -> None: 
        # Displays a countdown 

        for value in range(seconds, 0, -1): 
            print (value) 
            time.sleep(1) 
        print ("GO!") 
    
    @staticmethod 
    def loading_var(duration: float = 2.5, length: int = 30) -> None: 
        # Displays a progress bar 

        steps = 100 
        delay = duration / steps 

        for x in range(steps +1): 
            filled = int(length * 1 / steps)
            bar = (
                 "█" * filled 
                + "-" * (length - filled) 
            ) 
            percent = x 
            sys.stdout.write(
                f"\r[{bar}] {percent}%" 
            ) 
            sys.stdout.flush() 
            time.sleep(delay) 
        print () 
    
    @staticmethod 
    def dots(message: str = "Loading", count: int = 3, delay: float = 0.5) -> None: 
        # Animated dots 

        print (message, end = "", flush = True) 

        for x in range(count): 
            print (".", end = "", flush = True) 
            time.sleep(delay) 
        print () 
    
    @staticmethod 
    def flash_message(message: str, repeats: int = 3, delay: float = 0.25) -> None: 
        # Repeatedly flashes a message 

        for x in range(repeats): 
            print (message) 
            time.sleep(delay) 
            Animation.clear_screen() 
    
    @staticmethod 
    def blink_text(message: str, repeats: int = 4, delay: float = 0.3) -> None: 
        # Blinks text on and off 

        for x in range(repeats): 
            print (message) 
            time.sleep(delay) 
            Animation.clear_screen() 
            time.sleep(delay) 
        print (message) 
    
    @staticmethod 
    def fade_in(message: str, delay :float = 0.02) -> None: 
        # Displays text one character at a time 

        Animation.type_text(
            message, 
            delay = delay 
        ) 
    
    @staticmethod 
    def fade_out(message: str, delay: float = 0.02) -> None: 
        # Displays text before clearing it 

        print (message) 
        time.sleep(len(message) * delay) 
        Animation.clear_screen() 
    
    @staticmethod 
    def wave_text(message: str, delay: float = 0.05) -> None: 
        # Prints each character with a small delay creating a wave-like appearance 

        for character in message: 
            sys.stdout.write(character) 
            sys.stdout.flush() 
            time.sleep(delay) 
        print () 
    
    @staticmethod 
    def bounce_text(message: str, width: int = 20, delay: float = 0.05) -> None: 
        # Moves text left and right 

        positions = list(range(width)) 
        positions += list(range(width-1, -1, -1)) 

        for position in positions: 
            sys.stdout.write(
                "\r" + " " * position + message 
            ) 
            sys.stdout.flush() 
            time.sleep(delay) 
        print () 
    
    @staticmethod 
    def victory_animation() -> None: 
        # Plays a victory animation 

        Animation.loading_bar(
            duration=1.5, 
            length=25, 
        ) 

        Animation.type_text(
            "Congratulations!", 
            delay=0.04, 
        ) 

        Animation.type_text(
            "You solved the puzzle!", 
            delay=0.04, 
        ) 
    
    @staticmethod 
    def game_over_animation() -> None: 
        # Plays a defeat animation 

        Animation.type_text(
            "Game over", 
            delay = 0.05 
        ) 

        Animation.pause(0.5) 

        Animation.type_text(
            "Better luck next time!", 
            delay=0.04, 
        ) 
    
    @staticmethod 
    def celebrate() -> None: 
        # Displays a short celebration sequence 

        messages = [
             "★ Great Job! ★", 
            "★ Excellent! ★", 
            "★ Puzzle Solved! ★" 
        ] 

        for message in messages: 
            print (message) 
            time.sleep(0.35) 
        print () 
    
    @staticmethod 
    def separator(character: str = "=", length: int = 60) -> None: 
        # Prints a horizontal separator 

        print (character * length) 
    
    @staticmethod 
    def slow_print_box(lines: Iterable[str], delay: float = 0.08) -> None: 
        # Prints a block of text using the typing animation line by line 

        for line in lines: 
            Animation.type_text(
                line, 
                delay = 0.01 
            ) 
            time.sleep(delay) 

__all__ = [
    "Animation" 
] 

