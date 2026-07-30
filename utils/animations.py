# animations.py
# Provides simple terminal animations for the game

# These animations improve the overall user experience by making menus,
# victories, defeats, loading screens and text transitions feel polished 

from __future__ import annotations

import itertools
import os
import sys
import time
from typing import Iterable

from utils.constants import (
    DEFAULT_TIME_LIMIT,
    FAST_TYPEWRITER_DELAY,
    LOADING_DELAY,
    LOSE_DELAY,
    MENU_DELAY,
    TYPEWRITER_DELAY,
    WIN_DELAY,
)
from utils.helper import clear_screen


class Animation:
    # Collection of reusable terminal animations 

    DEFAULT_DELAY = TYPEWRITER_DELAY

    @staticmethod
    def clear_screen() -> None:
        # Clears the terminal.

        clear_screen()

    @staticmethod
    def pause(seconds: float = 1.0) -> None:
        # Pauses execution.

        time.sleep(seconds)

    @staticmethod
    def type_text(
        text: str,
        delay: float = DEFAULT_DELAY,
        end: str = "\n"
    ) -> None:
        # Prints text one character at a time.

        for character in text:
            print(
                character,
                end="",
                flush=True
            )
            time.sleep(delay)

        print(end=end)

    @staticmethod
    def print_lines(
        lines: Iterable[str],
        delay: float = MENU_DELAY
    ) -> None:
        # Prints multiple lines 

        for line in lines:
            print(line)
            time.sleep(delay)

    @staticmethod
    def spinner(
        duration: float = 2.0,
        message: str = "Loading"
    ) -> None:
        # Displays a rotating loading spinner 

        end_time = time.time() + duration

        frames = itertools.cycle(
            ["|", "/", "-", "\\"]
        )

        while time.time() < end_time:
            sys.stdout.write(
                f"\r{message} {next(frames)}"
            )
            sys.stdout.flush()
            time.sleep(LOADING_DELAY)

        sys.stdout.write("\r" + " " * (len(message) + 4))
        sys.stdout.write("\r")
        sys.stdout.flush()

    @staticmethod
    def countdown(seconds: int = 3) -> None:
        # Displays a countdown 

        for value in range(seconds, 0, -1):
            print(value)
            time.sleep(1)

        print("GO!")

    @staticmethod
    def loading_bar(
        duration: float = 2.5,
        length: int = 30
    ) -> None:
        # Displays a progress bar 

        steps = 100
        delay = duration / steps

        for step in range(steps + 1):

            filled = int(length * step / steps)

            bar = (
                "█" * filled +
                "-" * (length - filled)
            )

            sys.stdout.write(
                f"\r[{bar}] {step:3d}%"
            )
            sys.stdout.flush()

            time.sleep(delay)

        print()

    @staticmethod
    def dots(
        message: str = "Loading",
        count: int = 3,
        delay: float = 0.5
    ) -> None:
        # Animated loading dots 

        print(
            message,
            end="",
            flush=True
        )

        for _ in range(count):
            print(
                ".",
                end="",
                flush=True
            )
            time.sleep(delay)

        print()

    @staticmethod
    def flash_message(
        message: str,
        repeats: int = 3,
        delay: float = 0.25
    ) -> None:
        # Flashes a message 

        for _ in range(repeats):
            print(message)
            time.sleep(delay)
            Animation.clear_screen()

    @staticmethod
    def blink_text(
        message: str,
        repeats: int = 4,
        delay: float = 0.3
    ) -> None:
        # Blinks text 

        for _ in range(repeats):
            print(message)
            time.sleep(delay)

            Animation.clear_screen()

            time.sleep(delay)

        print(message)

    @staticmethod
    def fade_in(
        message: str,
        delay: float = FAST_TYPEWRITER_DELAY
    ) -> None:
        # Displays text gradually 

        Animation.type_text(
            message,
            delay=delay
        )

    @staticmethod
    def fade_out(
        message: str,
        delay: float = FAST_TYPEWRITER_DELAY
    ) -> None:
        # Displays text before clearing it 

        print(message)

        time.sleep(
            len(message) * delay
        )

        Animation.clear_screen()

    @staticmethod
    def wave_text(
        message: str,
        delay: float = TYPEWRITER_DELAY
    ) -> None:
        # Prints characters individually 

        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(delay)

        print()

    @staticmethod
    def bounce_text(
        message: str,
        width: int = 20,
        delay: float = 0.05
    ) -> None:
        # Moves text left and right 

        positions = list(range(width))
        positions += list(
            range(width - 1, -1, -1)
        )

        for position in positions:
            sys.stdout.write(
                "\r" +
                " " * position +
                message
            )

            sys.stdout.flush()
            time.sleep(delay)

        print()

    @staticmethod
    def victory_animation() -> None:
        # Plays the victory animation 

        Animation.loading_bar(
            duration=1.5,
            length=25
        )

        Animation.type_text(
            "Congratulations!",
            delay=WIN_DELAY
        )

        Animation.type_text(
            "You solved the puzzle!",
            delay=WIN_DELAY
        )

    @staticmethod
    def game_over_animation() -> None:
        # Plays the defeat animation 

        Animation.type_text(
            "Game Over!",
            delay=LOSE_DELAY
        )

        Animation.pause(0.5)

        Animation.type_text(
            "Better luck next time!",
            delay=LOSE_DELAY
        )

    @staticmethod
    def celebrate() -> None:
        # Displays a short celebration 

        messages = [
            "★ Great Job! ★",
            "★ Excellent! ★",
            "★ Puzzle Solved! ★"
        ]

        for message in messages:
            print(message)
            time.sleep(0.35)

        print()

    @staticmethod
    def separator(
        character: str = "=",
        length: int = 60
    ) -> None:
        # Prints a separator 

        print(character * length)

    @staticmethod
    def slow_print_box(
        lines: Iterable[str],
        delay: float = 0.08
    ) -> None:
        # Prints a block of text line by line 

        for line in lines:
            Animation.type_text(
                line,
                delay=FAST_TYPEWRITER_DELAY
            )

            time.sleep(delay)


__all__ = [
    "Animation",
] 

