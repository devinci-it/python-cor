# src/utils/formatting.py

"""
Formatting utilities for terminal output.

Author    : Vincent de Torres
GitHub    : https://github.com/devinci-it
File      : src/utils/formatting.py

This module provides functions for formatting text for terminal output. 
Includes functionality for printing styled lines, headers, and other formatted text.
"""

from src.utils.styles import Styles

def line(message, pre=None, type="debug", stringify=False):
    """
    Print an information message to the console.
    """
    style = getattr(Styles, type.upper(), Styles.MUTED)
    pre = f"{pre}".ljust(25) if pre else ""
    formatted_str = f"\t{style}{pre}{Styles.DEFAULT}{message:<65}{Styles.RESET}"
    if stringify:
        return formatted_str
    else:
        print(f"{formatted_str:<{get_terminal_size()[0]}}")

def header(text):
    """
    Print a header with the given text.
    """
    print(f"{Styles.HEADER}{text}{Styles.RESET}")

def tasks(text):
    """
    Print a task with the given text.
    """
    print(f"{Styles.ACCENT}{text}{Styles.RESET}")

def newline(n=1):
    """
    Print a newline.
    """
    print("\n" * n)

def divider(stringify=False):
    """
    Print a styled divider line to the CLI.
    """
    col, _ = get_terminal_size()
    border = f"{'━' * (col-8):<{col-8}}"
    if stringify:
        return border
    else:
        print(border)

