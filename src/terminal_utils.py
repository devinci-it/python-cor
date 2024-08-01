# src/utils/terminal.py

"""
Terminal utilities for managing terminal output and interactions.

Author    : Vincent de Torres
GitHub    : https://github.com/devinci-it
File      : src/utils/terminal.py

This module provides functions for terminal management, including clearing the screen, 
getting terminal size, and other utilities specific to terminal operations.
"""

import os

def clear_screen():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    """
    Get the current terminal size.
    """
    try:
        col, row = os.get_terminal_size()
    except Exception as e:
        print(f"Error getting terminal size: {e}")
        col, row = 80, 24  # Default size if error occurs
    return col, row

def get_terminal_width(offset=8):
    """
    Get the width of the terminal window.
    """
    width = os.get_terminal_size().columns - offset
    return width

def get_terminal_height(offset=8*5):
    """
    Get the height of the terminal window.
    """
    height = os.get_terminal_size().lines - offset
    return height

