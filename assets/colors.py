# color.py 
# Stores every color used throughout the game 


from colorama import Fore, Back, Style, init

# Automatically reset colors after every print
init(autoreset=True)


class Colors:
    # Basic colors
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE

    # Bright colors
    BRIGHT_RED = Fore.LIGHTRED_EX
    BRIGHT_GREEN = Fore.LIGHTGREEN_EX
    BRIGHT_YELLOW = Fore.LIGHTYELLOW_EX
    BRIGHT_BLUE = Fore.LIGHTBLUE_EX
    BRIGHT_MAGENTA = Fore.LIGHTMAGENTA_EX
    BRIGHT_CYAN = Fore.LIGHTCYAN_EX
    BRIGHT_WHITE = Fore.LIGHTWHITE_EX

    # Backgrounds
    BG_RED = Back.RED
    BG_GREEN = Back.GREEN
    BG_BLUE = Back.BLUE
    BG_YELLOW = Back.YELLOW
    BG_MAGENTA = Back.MAGENTA
    BG_CYAN = Back.CYAN
    BG_WHITE = Back.WHITE

    # Styles
    BOLD = Style.BRIGHT
    DIM = Style.DIM
    NORMAL = Style.NORMAL
    RESET = Style.RESET_ALL

    # Semantic colors used by the game
    TITLE = BRIGHT_CYAN + BOLD
    MENU = BRIGHT_WHITE
    PROMPT = BRIGHT_YELLOW
    SUCCESS = BRIGHT_GREEN + BOLD
    ERROR = BRIGHT_RED + BOLD
    WARNING = BRIGHT_YELLOW + BOLD
    INFO = BRIGHT_BLUE
    SCORE = BRIGHT_MAGENTA + BOLD
    HANGMAN = WHITE
    CORRECT = GREEN
    WRONG = RED