# scoreboard.py 
# Calculates every score awarded or deducted during the game 
# DOESN'T STORE SCORES 
# Just calculates how many points should be added / removed 
# Player object actually stores score 

from __future__ import annotations 
from game.player import Player 
from game.difficulty import DifficultyManager 

from utils.constants import (
    POINTS_CORRECT_GUESS,
    POINTS_GAME_WON,
    POINTS_WORD_COMPLETED,
    POINTS_FAST_FINISH,
    POINTS_PER_UNUSED_LIFE,
    POINTS_STREAK_BONUS,
    POINTS_HINT_PENALTY,
    POINTS_WRONG_GUESS,
    POINTS_DUPLICATE_GUESS,
    FAST_FINISH_TIME,
    COMBO_START,
    COMBO_BONUS,
    MAX_COMBO_MULTIPLIER, 
)

class ScoreBoard: 
    # Calculates every score event 

    ## Internal 

    @staticmethod 
    def multiplier() -> float: 
        # Returns the current difficulty multiplier 

        return (
            DifficultyManager
            .get_settings()
            .score_multiplier 
        )
    
    @staticmethod 
    def scaled(points: int) -> int: 
        # Applies the difficulty multiplier 

        return int(
            points * ScoreBoard.multiplier() 
        ) 
    

    ## Guess scores 

    @staticmethod 
    def correct_guess(player: Player) -> int: 
        # Score for a correct letter 

        score = POINTS_CORRECT_GUESS 

        if player.current_streak >= COMBO_START: 
            combo = min(
                player.current_streak, 
                MAX_COMBO_MULTIPLIER 
            ) 

            score += combo * COMBO_BONUS 
        
        return ScoreBoard.scaled(score) 
    
    @staticmethod 
    def wrong_guess() -> int: 
        # Penalty for a wrong guess 

        return POINTS_WRONG_GUESS 
    
    @staticmethod 
    def duplicate_guess() -> int: 
        # Penalty for guessing the same letter twice 

        return POINTS_DUPLICATE_GUESS 
    
    @staticmethod 
    def hint_used() -> int: 
        # Penalty for using a hint 
        # Uses the value stored in DifficultySettings 

        return (
            -DifficultyManager 
            .get_settings() 
            .hint_penalty 
        ) 
    

    ## Bonuses 

    @staticmethod 
    def word_completed() -> int: 
        # Bonus for revealing every letter 

        return ScoreBoard.scaled(POINTS_WORD_COMPLETED) 
    
    @staticmethod 
    def game_won(player: Player) -> int: 
        # Final score bonus 

        bonus = POINTS_GAME_WON 

        bonus += (
            player.lives_remaining * POINTS_PER_UNUSED_LIFE 
        ) 

        return ScoreBoard.scaled(bonus) 
    
    @staticmethod 
    def fast_finish(elapsed_seconds: float) -> int: 
        # Bonus for finishing quickly 

        if elapsed_seconds <= FAST_FINISH_TIME: 
            return ScoreBoard.scaled(POINTS_FAST_FINISH) 
        
        return 0 
    

    ## Utility 

    @staticmethod 
    def calculate_final_score(player: Player, elapsed_seconds: float) -> int: 
        # Calculates every bonus awarded when a game is won 

        score = 0 

        score += ScoreBoard.game_won(player) 

        score += ScoreBoard.fast_finish(elapsed_seconds) 

        return score 
    

    ## Formatting 

    @staticmethod 
    def format(score: int) -> str: 
        # Returns a formatted score 
        # E.g. 15420 becomes 15,420 

        return f"{score:,}" 
    

    ## Preview 

    @staticmethod 
    def preview(player: Player) -> None: 
        # Prints scoring information 
        # Useful for debugging 

        print ("=" * 50) 
        print ("SCORING PREVIEW") 
        print ("=" * 50) 

        print (
            f"Difficulty Multipler: " 
            f"x{ScoreBoard.multiplier()}" 
        ) 

        print (
            f"Correct guess        : " 
            f"{ScoreBoard.correct_guess(player)}" 
        ) 

        print (
            f"Wrong guess          : " 
            f"{ScoreBoard.wrong_guess()}" 
        ) 

        print (
            f"Duplicate guess      : " 
            f"{ScoreBoard.duplicate_guess()}" 
        ) 

        print (
            f"Hints penalty        : " 
            f"{ScoreBoard.hint_used()}" 
        ) 

        print (
            f"Word complete bonus  : " 
            f"{ScoreBoard.word_completed()}" 
        ) 

        print (
            f"Win bonus            : " 
            f"{ScoreBoard.game_won(player)}" 
        ) 

        print ("=" * 50) 

