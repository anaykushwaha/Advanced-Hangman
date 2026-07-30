# helper.py
# General helper functions used throughout the game
# Only generic utility functions belong here

# This file does NOT contain:
# 1. Validation logic
# 2. Rendering
# 3. Animations
# 4. File handling

from __future__ import annotations

import os
import random
import shutil
import textwrap

from typing import Iterable, Sequence, TypeVar

from utils.constants import (
    SCREEN_WIDTH,
    YES_RESPONSES,
    NO_RESPONSES,
)

T = TypeVar("T")


## Terminal

def clear_screen() -> None:
    # Clears the terminal screen

    os.system(
        "cls" if os.name == "nt"
        else "clear"
    )


def terminal_width(
    default: int = SCREEN_WIDTH
) -> int:
    # Returns the terminal width

    return shutil.get_terminal_size(
        fallback=(default, 25)
    ).columns


def center(
    text: str,
    width: int | None = None
) -> str:
    # Centers a string

    if width is None:
        width = terminal_width()

    return text.center(width)


def separator(
    character: str = "=",
    width: int | None = None
) -> str:
    # Creates a separator line

    if width is None:
        width = terminal_width()

    return character * width


## Text

def wrap(
    text: str,
    width: int = 70
) -> str:
    # Wraps text

    return textwrap.fill(
        text,
        width=width
    )


def title_case(text: str) -> str:
    # Converts text to title case

    return text.title()


def normalize(text: str) -> str:
    # Removes whitespace and converts to uppercase

    return text.strip().upper()


def is_blank(text: str) -> bool:
    # Returns True if the string is empty

    return normalize(text) == ""


## Random

def choose(items: Sequence[T]) -> T:
    # Returns a random item

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


def safe_int(
    value: str,
    default: int = 0
) -> int:
    # Converts text to an integer safely

    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def safe_float(
    value: str,
    default: float = 0.0
) -> float:
    # Converts text to a float safely

    try:
        return float(value)
    except (TypeError, ValueError):
        return default


## Collections

def sorted_letters(
    letters: Iterable[str]
) -> list[str]:
    # Returns sorted uppercase letters

    return sorted(
        letter.upper()
        for letter in letters
    )


def unique_sorted_letters(
    letters: Iterable[str]
) -> list[str]:
    # Returns unique sorted uppercase letters

    return sorted({
        letter.upper()
        for letter in letters
    })


def comma_join(
    items: Iterable[object]
) -> str:
    # Joins items using commas

    return ", ".join(
        map(str, items)
    )


## User Input

def pause(
    message: str = "Press Enter to continue"
) -> None:
    # Waits for the user

    input(message)


def ask_yes_no(
    message: str
) -> bool:
    # Prompts until the user enters Y/YES or N/NO

    while True:
        answer = normalize(
            input(f"{message} (Y/N): ")
        )

        if answer in YES_RESPONSES:
            return True

        if answer in NO_RESPONSES:
            return False

        print("Please enter Y or N.")


## Display

def print_centered(
    text: str,
    width: int | None = None
) -> None:
    # Prints centered text

    print(center(text, width))


def print_header(
    title: str,
    width: int | None = None
) -> None:
    # Prints a simple section header

    if width is None:
        width = terminal_width()

    print(separator("=", width))
    print(title.center(width))
    print(separator("=", width)) 

