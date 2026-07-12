# banner.py 
# Displays ASCII banners using pyfiglet 

from __future__ import annotations
from pyfiglet import Figlet 
from assets.colors import Colors 

class Banner: 
    # Utility class for creating ASCII banners 

    DEFAULT_FONT = "slant" 


    @staticmethod 
    def print_banner(
        text: str, 
        font: str = DEFAULT_FONT, 
        color: str = Colors.TITLE, 
        center: bool = True, 
        width: int = 80 
    ) -> None: 
        # Prints a large ASCII banner 

        figlet = Figlet(font=font) 
        banner = figlet.renderText(text) 
        lines = banner.rstrip().splitlines() 

        if center: 
            for line in lines: 
                print (color + line.center(width)) 
        else: 
            for line in lines: 
                print (color + line) 
    
    @staticmethod 
    def print_logo(width: int = 80) -> None: 
        # Prints the game logo 

        Banner.print_banner(
            "Hangman", 
            center = True, 
            width = width 
        ) 
    
    @staticmethod 
    def print_title(title: str, width: int = 80) -> None: 
        # Prints any title 

        Banner.print_banner(
            title, 
            center = True, 
            width = width 
        ) 

