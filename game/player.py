# player.py 
# Stores all the information related to the current player and 
# their progress in the active Hangman game 

from dataclasses import dataclass, field 
from typing import Set 

@dataclass 
class Player: 
    # represents the current player 
    # this class only stores data 
    # game logic is handled by GameEngine 

    ## Identity 
    name: str = "Player" 

    ## Score 
    score: int = 0 
    high_score: int = 0 

    ## Lives 
    max_lives: int = 12 
    lives_remaining: int = 12 

    ## Guess tracking 
    correct_letters: Set[str] = field(default_factory=set) 
    wrong_letters: Set[str] = field(default_factory=set) 

    ## Statistics 
    total_guesses: int = 0 
    correct_guesses: int = 0 
    wrong_guesses: int = 0 

    ## State 
    won: bool = False 
    lost: bool = False 



    ### Methods 

    def reset(self) -> None: 
        # resets the player 


        self.score = 0 

        self.lives_remaining = self.max_lives 

        self.correct_letters.clear() 
        self.wrong_letters.clear() 

        self.total_guesses = 0 
        self.correct_guesses = 0 
        self.wrong_guesses = 0 

        self.hints_used = 0 

        self.current_streak = 0 
        self.longest_streak = 0 

        self.won = False 
        self.lost = False 

    

    def add_correct_guess(self, letter:str) -> None: 
        # records a correct guess 
        
        letter = letter.upper() 

        if letter in self.correct_letters: 
            return 
        
        self.correct_letters.add(letter) 

        self.total_guesses += 1 
        self.correct_guesses += 1 

        self.current_streak += 1 

        if self.current_streak > self.longest_streak: 
            self.longest_streak = self.current_streak 

    

    def add_wrong_guess(self, letter: str) -> None: 
        # records an incorrect guess 

        letter = letter.upper() 

        if letter in self.wrong_letters: 
            return 
        
        self.wrong_letters.append(letter) 

        self.total_guesses += 1 
        self.wrong_guesses += 1 

        self.current_streak = 0 

        self.lives_remaining -= 1 

        if self.lives_remaining <= 0: 
            self.lost = True 
        
    
    def use_hint(self) -> None: 
        # records hint usage 

        self.hints_used += 1 

    
    def add_score(self, points: int) -> None: 
        # increases score 

        self.score += points 

        if self.score < 0: 
            self.score = 0 
        
    
    def mark_win(self) -> None: 
        # marks the current game as won 

        self.won = True 
        self.lost = False 
    
    def mark_loss(self) -> None: 
        # marks the current game as lost 

        self.won = False 
        self.lost = True 

    def has_guessed(self, letter: str) -> None: 
        # returns True if the player has already guessed the letter 

        letter = letter.upper() 

        return (
            letter in self.correct_letters 
            or letter in self.wrong_letters
        )
    

    @property 
    def accuracy(self) -> float: 
        # percentage of correct guesses 

        if self.total_guesses == 0: 
            return 0.0 
        
        return (
            self.correct_guesses / self.total_guesses 
        ) * 100 
    

    @property 
    def is_alive(self) -> bool: 
        # True if the player still has lives remaining 

        return self.lives_remaining > 0 
    

    @property 
    def guesses_remaining(self) -> int: 
        # number of incorrect guesses the player can still make 

        return self.lives_remaining 
    

    def __str__(self) -> str: 
        return (
            f"Player(name={self.name}, " 
            f"score={self.score}, " 
            f"lives={self.lives_remaining} / {self.max_lives})"
        )