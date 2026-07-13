# timer.py 
# Provides timing functionality for the game 

# Supports: 
# 1. Stopwatch mode 
# 2. Countdown Mode 
# 3. Pause / Resume 
# 4. Reset 
# 5. Formatted Time Display 

from __future__ import annotations 
import time 

class GameTimer: 
    # Handles all game timing 
    # If a time limit is supplied, the timer behaves like a countdow, or else it's a stopwatch 

    def __init__(self, time_limit: int | None = None): 

        self.time_limit = time_limit 
        self.start_time = None 
        self.pause_start = None 
        self.pause_duration = 0.0 
        self.running = False 
        self.paused = False 

    ## Timer control 

    def start(self) -> None: 
        # Starts the timer 

        self.start_time = time.time() 
        self.pause_start = None 
        self.pause_duration = 0.0 
        self.running = True 
        self.paused = False 

    def stop(self) -> None: 
        # Stops the timer 

        self.running = False 
        self.paused = False 
    
    def reset(self) -> None: 
        # Resets the timer 

        self.start = None 
        self.pause_start = None 
        self.pause_duration = 0.0 
        self.running = False 
        self.paused = False 
    
    def pause(self) -> None: 
        # Pauses the timer 

        if not self.running: 
            return 
        
        if self.paused: 
            return 
        
        self.pause_start = time.time() 
        self.paused = True 
    
    def resume(self) -> None: 
        # Resumes the timer 

        if not self.paused: 
            return 
        
        self.pause_duration += (
            time.time() - self.pause_start 
        ) 
        self.pause_start = None 
        self.paused = False 
    

    ## Time 

    def elapsed(self) -> None: 
        # Returns elapsed time in terms of seconds 

        if not self.running: 
            return 0.0 
        
        if self.paused: 
            current = self.pause_start 
        else: 
            current = time.time() 
        
        return (
            current 
            - self.start_time 
            - self.pause_duration 
        )
    
    def remaining(self) -> float | None: 
        # Returns remaining seconds 
        # Returns None for stopwatch mode 

        if self.time_limit is None: 
            return None 
        
        return max(
            0.0, 
            self.time_limit - self.elapsed() 
        ) 
    
    def expired(self) -> bool: 
        # Returns True if the countdown reaches 0 

        if self.time_limit is None: 
            return None 
        return self.remaining() <= 0 
    

    ## Formatting 

    @staticmethod 
    def format(seconds: float) -> str: 
        # Converts seconds into MM:SS format 

        seconds = max(0, int(seconds)) 
        minutes = seconds // 60 
        seconds = seconds % 60 

        return f"{minutes:02}:{seconds:02}" 
    
    def formatted_elapsed(self) -> str: 
        # Returns elpased time as MM:SS 

        return self.format(self.elapsed()) 
    
    def formatted_remaining(self) -> str: 
        # Returns remaining time as MM:SS 
        # Stopwatch mode returns elapsed time 

        if self.time_limit is None: 
            return self.formatted_elapsed() 
        
        return self.format(self.remaining()) 
    
    
    ## Properties 

    @property 
    def running(self) -> bool: 
        # Returns whether the timer is running 

        return self.running 
    
    @property 
    def paused(self) -> bool: 
        # Returns whether the timer is paused 

        return self.paused 
    
    @property 
    def countdown(self) -> bool: 
        # Returns True if using countdown 

        return self.time_limit is not None 
    
    
    ## Representation 

    def __str__(self) -> str: 
        if self.countdown: 
            return (
                f"Countdown Timer " 
                f"({self.formatted_remaining()} remaining)" 
            )

        return (
            f"Stopwatch " 
            f"({self.formatted_elapsed()} elapsed)" 
        ) 
    
    def __repr__(self) -> str: 
        return (
            f"Game Timer("
            f"time_limit = {self.time_limit}, " 
            f"running = {self.running}, " 
            f"paused = {self.paused}" 
        ) 

