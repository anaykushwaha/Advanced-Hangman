# word_manager.py 
# Handles loading, selecting, validating and managing words used throughout the game 

from __future__ import annotations 
from dataclasses import dataclass 
from pathlib import Path 
from typing import Dict, List 
import random 

from game.difficulty import DifficultyManager 
from utils.constants import ( 
    EASY_WORDS_FILE, 
    MEDIUM_WORDS_FILE, 
    HARD_WORDS_FILE, 
    IMPOSSIBLE_WORDS_FILE, 
)
 
from utils.file_manager import FileManager 

## Word object 

@dataclass(slots = True) 
class Word: 
    # Represents a playable Hangman word or phrase 

    text: str 
    category: str 
    difficulty: str 

    @property 
    def length(self) -> int: 
        # Number of letters (spaces not counted) 

        return len(self.text.replace(" ", "")) 
    
    @property 
    def word_count(self) -> int: 
        # Number of separate words 

        return len(self.text.split()) 
    

## Word manager 

class WordManager: 

    def __init__(self) -> None: 
        self.difficulty = DifficultyManager() 

        self.words: Dict [str, List[Word]] = {
            "Easy": [], 
            "Medium": [], 
            "Hard": [], 
            "Impossible": [], 
        } 

        self.current_word: Word | None = None 
        self.load_all() 
    
    def load_all(self) -> None: 
        # Loads every JSON word file 

        self.words["Easy"] = self.load_file(
            EASY_WORDS_FILE, 
            "Easy" 
        ) 
        self.words["Medium"] = self._load_file(
            MEDIUM_WORDS_FILE, 
            "Medium" 
        ) 
        self.words["Hard"] = self._load_file(
            HARD_WORDS_FILE, 
            "Hard" 
        ) 
        self.words["Impossible"] = self._load_file(
            IMPOSSIBLE_WORDS_FILE, 
            "Impossible" 
        ) 
    
    def load_file(self, filename: str, difficulty: str) -> List[Word]: 
        # Reads a JSON word list and converts it into Word objects 

        path = Path(filename) 
        
        if not FileManager.exist(path): 
            return [] 
        
        raw = FileManager.load_json(path) 
        words: List[Word] = [] 

        for category, entries in raw.items(): 
            for text in entries: 
                words.append(
                    Word (
                        text = text.upper(), 
                        category = category, 
                        difficulty = difficulty 
                    ) 
                ) 
        return words 
    
    def random_word(self, difficulty: str | None = None) -> Word: 
        # Returns a random word 

        if difficulty is None: 
            difficulty = (
                self.difficulty 
                .get_settings() 
                .name 
            ) 
        
        pool = self.words[difficulty] 

        if not pool: 
            raise ValueError(
                f"No words loaded for {difficulty}" 
            ) 
        
        self.current_word = random.choice(pool) 
        return self.current_word 
    
    def current(self) -> Word: 
        # Returns the active word 

        if self.current_word is None: 
            raise RuntimeError(
                "No active word selected" 
            ) 
        
        return self.current_word
    
    def all_words(self, difficulty: str) -> List[Word]: 
        # Returns every word for a difficulty 

        return self.words[difficulty] 
    
    def total_words(self, difficulty: str | None = None) -> int: 
        # Counts words 

        if difficulty is None: 
            return sum(
                len(lst) 
                for lst in self.words.values() 
            ) 
        
        return len(self.words[difficulty]) 
    
    def difficulties(self) -> List[str]: 
        # Returns available difficulties 

        return list(self.words.key()) 
    
    def categories(self, difficulty: str) -> List[str]: 
        # Returns categories for one difficulty 

        categories = {
            word.category 
            for word in self.words[difficulty] 
        } 

        return sorted(categories) 
    
    def random_category_word(self, difficulty: str, category: str) -> Word: 
        # Returns a random word from a category 

        candidates = {
            word 
            for word in self.words[difficulty] 
            if word.category.lower() == category.lower() 
        } 

        if not candidates: 
            raise ValueError(
                "Category doesn't exist" 
            ) 
        
        self.current_word = random.choice(candidates) 
    
    def exists(self, word: str) -> bool: 
        # Returns True if the supplied word exists in any difficulty 

        word = word.upper() 
        
        for pool in self.words.values(): 
            for entry in pool: 
                if entry.text == word: 
                    return True 
        return False 
    

    ## Searching 

    def words_by_length(self, length: int, difficulty: str | None = None) -> List[Word]: 
        # Returns every word with the requested number of letters (spaces not counted) 

        if difficulty is None: 
            pool = [] 
            for words in self.words.values(): 
                pool.extend(words) 

        else: 
            return [
                word 
                for word in pool 
                if word.length == length 
            ] 
        
    def phrases(self, difficulty: str | None = None) -> List[Word]: 
        # Returns every phrase (multiple words) 

        if difficulty is None: 
            pool = [] 
            for words in self.words.values(): 
                pool.extend(words) 
        else: 
            pool = self.words[difficulty] 
        
        return [
            word 
            for word in pool 
            if word.word_count > 1 
        ] 
    
    def single_words(self, difficulty: str | None = None) -> List[Word]: 
        # Returns only single-word entries 

        if difficulty is None: 
            pool = [] 
            for words in self.words.values(): 
                pool.extend(words) 
        else: 
            return [
                word 
                for word in pool 
                if word.word_count == 1 
            ] 
    
    def longest_word(self, difficulty: str | None = None) -> Word: 
        if difficulty is None: 
            pool = [] 
            for word in self.words.values(): 
                pool.extend(words) 
        else: 
            pool = self.words[difficulty] 
        
        return max(
            pool, 
            key = lambda word: word.length 
        ) 
    
    def shortest_word(self, difficulty: str | None = None) -> Word: 
        if difficulty is None: 
            pool = [] 
            for word in self.words.values(): 
                pool.extend(words) 
        else: 
            pool = self.words[self.difficulty] 
        
        return min(
            pool, 
            key = lambda word: word.length 
        ) 
    

    ## Validation 

    def is_valid_word(self, word: str) -> bool: 
        # Determines whether a word is valid for the game 

        if not word: 
            return False 
        
        word = word.strip() 

        if len(word) == 0: 
            return False 
        
        for character in word: 
            if character == " ": 
                continue 
            if not character.isalpha(): 
                return False 
            
        return True 
    
    def sanitize(self, word: str) -> str: 
        # Cleans a word before storing it 

        return " ".join(
            word.upper().strip().split() 
        ) 
    
    def contains(self, text: str) -> bool: 
        # Alias for exists() 

        return self.exists(text) 
    

    ## Custom word management 

    def add_word(self, word: str, category: str, difficulty: str) -> None: 
        # Adds a custom word 

        word = self.sanitize(word) 

        if not self.is_valid_word(word): 
            raise ValueError(
                "Invalid word" 
            ) 
        
        if self.exists(word): 
            raise ValueError(
                "Word already exists" 
            ) 
        
        self.words[difficulty].append(
            Word(
                text = word, 
                category = category, 
                difficulty = difficulty 
            ) 
        ) 
    
    def remove_word(self, word: str, difficulty: str) -> bool: 
        # Removes a custom word 

        word = self.sanitize(word) 
        pool = self.words[difficulty] 
        
        for entry in pool: 
            if entry.text == word: 
                pool.remove(entry) 
                return True 
        return False 
    
    def clear_custom(self, difficulty: str) -> None: 
        # Removes every custom word for a difficulty 
        # Resevred for future expansion as of right now 

        self.words[difficulty] = [
            word 
            for word in self.words[difficulty] 
        ] 
    

    ## Statistics 

    def category_counts(self, difficulty: str | None = None) -> dict[str, int]: 
        # Returns the number of words in each category 

        if difficulty is None: 
            pool = [] 
            for words in self.words.values(): 
                pool.extend(words) 
        else: 
            pool = self.words[difficulty] 
        
        counts: dict[str, int] = {} 

        for word in pool: 
            counts[word.category] = (
                counts.get(word.category, 0) + 1 
            ) 
        
        return dict(sorted(counts.items())) 
    
    def difficulty_counts(self) -> dict[str, int]: 
        # Returns the number of words in each difficulty 

        return {
            difficulty: len(words) 
            for difficulty, words in self.words.items() 
        } 
    
    def total_categories(self) -> int: 
        # Returns the number of unique categories 

        categories = set() 

        for word in self.words.values(): 
            for word in words: 
                categories.add(word.category) 
        
        return len(categories) 
    

    ## Persistence 

    def reload(self) -> None: 
        # Reloads every word list from disk 

        self.words = {
            "Easy": [], 
            "Medium": [], 
            "Hard": [], 
            "Impossible": [], 
        } 

        self.current_word = None 
        self.load_all() 

    def save_custom_word(self) -> None: 
        # Placeholder for future support of persistent custom word lists 
        # Initial version ships with read-only word banks, so this method is empty for now 

        pass 


    ## Utility methods 

    def __len__(self) -> int: 
        # Returns the total number of loaded words 

        return self.total_words() 
    
    def __iter__(self): 
        # Iterates through every loaded word 

        for difficulty in self.words.values(): 
            for word in difficulty: 
                yield word 
    
    def __contains__(self, item: str) -> bool: 
        # Enables if "PYTHON" in manager 

        return self.exists(item) 
    
    def __str__(self) -> str: 
        # Returns a concise summary of the loaded word database 

        counts = self.difficulty_counts() 

        return (
            "WordManager(" 
            f"Easy={counts['Easy']}, " 
            f"Medium={counts['Medium']}, " 
            f"Hard={counts['Hard']}, " 
            f"Impossible={counts['Impossible']}, " 
            f"Total={self.total_words()})" 
        ) 
    
    def __repr__(self) -> str: 
        return self.__str__() 

