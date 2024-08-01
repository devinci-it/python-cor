"""

Author    : Vincent de Torres
GitHub    : https://github.com/devinci-it
File      : src/utils/exit_handler.py

This module includes functions for gracefully handling program exits, including clearing the screen
and printing an exit message.
"""

import os
from src.utils.formatting import line

def handle_exit():
    """
    Handle the exit of the program by clearing the screen and printing an exit message.
    
    Returns:
    - None
    """
    clear_screen()
    line("Exiting the program. Goodbye!", type="muted")
    os.sys.exit(0)

def clear_screen():
    """
    Clear the terminal screen.
    
    Returns:
    - None
    """
    os.system('cls' if os.name == 'nt' else 'clear')

