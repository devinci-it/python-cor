from .terminal import get_terminal_width
from .styles import Styles
from .formatting import justify_text, divider

def key_underline(key, value, as_list=False):
    """
    Print a key with an underline.

    Parameters:
    - key (str): The key to be printed.
    - value (str): The value associated with the key.
    - as_list (bool): If True, print key-value pairs as a list, otherwise as a single formatted line.

    Returns:
    - None
    """
    content = justify_text(align='left', text=f"{value.upper()}", indent=3)
    label = justify_text(align='left', text=f"{key}", indent=3)
    
    if as_list:
        print("\n" * 3)
        print(f"\t{Styles.BOLD}{Styles.COMMENT} {label} | {Styles.ACCENT} {content:{get_terminal_width()}}{Styles.RESET}")
        print(f"\t{Styles.BOLD}{divider(stringify=True)}{Styles.RESET}")
    else:
        print(f"{Styles.BOLD}{label} | {Styles.DEFAULT}{content}{Styles.RESET}")
