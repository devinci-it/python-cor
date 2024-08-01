# src/utils/user_interaction.py

"""
User interaction utilities for handling input and output.

Author    : Vincent de Torres
GitHub    : https://github.com/devinci-it
File      : src/utils/user_interaction.py

This module includes functions for interacting with users, such as prompting for input, 
waiting for user confirmation, and displaying formatted key-value pairs.
"""

import getpass
from src.utils.formatting import line

def prompt_for_input(
    prompt_message: str, 
    input_type: type, 
    validation_func=None, 
    error_message: str = None,
    hidden: bool = False,
    refresh=None,
) -> any:
    """
    Get and validate user input.
    """
    while True:
        try:
            if hidden:
                print(line(f"\n\t ❯ {prompt_message}", type="message", stringify=True), end="", flush=True)
                user_input = getpass.getpass("🙈")
            else:
                print(line(f"\n\t ❯ {prompt_message}", type="message", stringify=True), end="", flush=True)
                user_input = input('').strip()
            print("")
            converted_input = input_type(user_input)
            if refresh:
                refresh()
            if validation_func is not None:
                validation_func_input = validation_func(converted_input)
                if validation_func_input is None:
                    raise ValueError("Invalid input")
                else:
                    line(f"Successfully assigned value of {converted_input}", type="success")
            line(f"Returning {converted_input} with type {str(type(converted_input))}", type="success")
            return converted_input if not validation_func else validation_func_input

        except (ValueError, TypeError) as e:
            if error_message:
                line(f"{error_message}: {e}", type="error")
            else:
                line(f"Invalid input: {e}", type="error")

def wait_for_enter():
    """
    Wait for the user to press Enter.
    """
    prompt_message = f"\n{Styles.MUTED}\tPress Enter to continue...{Styles.RESET}\n"
    print(f"\t{prompt_message}", end='', flush=True)
    input("")

def display_key_value(key, value, full_width=True, stringify=False):
    """
    Display a key-value pair in a formatted manner.
    """
    key, value = str(key), str(value)
    terminal_width = get_terminal_width() - 8  # Fixed width for full-width display
    key_width = round(terminal_width * 1 / 3)
    value_width = terminal_width - key_width - 16  # Subtract 8 for padding and spacing 
    
    key = key.strip()
    value = value.strip()
    formatted_str = f"\t\t{Styles.HEADER}{key:<{key_width}}{Styles.RESET}{value:<{value_width}}"

    print(formatted_str, flush=True)

    if stringify:
        return formatted_str

