# file_manager.py
# Handles reading and writing text and JSON files
#
# This is the only module in the project responsible for
# interacting directly with the file system.

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class FileManager:
    # Utility class for file operations

    ## Text Files

    @staticmethod
    def load_text(filepath: str | Path) -> str:
        # Reads an entire text file

        path = Path(filepath)

        with path.open(
            "r",
            encoding="utf-8"
        ) as file:
            return file.read()

    @staticmethod
    def save_text(
        filepath: str | Path,
        text: str
    ) -> None:
        # Writes text to a file

        path = Path(filepath)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with path.open(
            "w",
            encoding="utf-8"
        ) as file:
            file.write(text)

    ## JSON Files

    @staticmethod
    def load_json(filepath: str | Path) -> Any:
        # Loads a JSON file

        path = Path(filepath)

        with path.open(
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    @staticmethod
    def save_json(
        filepath: str | Path,
        data: Any,
        indent: int = 4
    ) -> None:
        # Saves data as JSON

        path = Path(filepath)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with path.open(
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                indent=indent,
                ensure_ascii=False
            )

    ## Utilities

    @staticmethod
    def exists(filepath: str | Path) -> bool:
        # Returns True if a file exists

        return Path(filepath).exists()

    @staticmethod
    def delete(filepath: str | Path) -> bool:
        # Deletes a file if it exists

        path = Path(filepath)

        if path.exists():
            path.unlink()
            return True

        return False

    @staticmethod
    def create_folder(folder: str | Path) -> None:
        # Creates a folder if necessary

        Path(folder).mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def file_size(filepath: str | Path) -> int:
        # Returns the file size in bytes

        path = Path(filepath)

        if not path.exists():
            return 0

        return path.stat().st_size

    @staticmethod
    def clear_file(filepath: str | Path) -> None:
        # Empties a file

        path = Path(filepath)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            "",
            encoding="utf-8"
        )

