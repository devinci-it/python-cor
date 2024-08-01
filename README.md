# Utility Package for Terminal-Based Applications

## Overview

This Python package provides a collection of utility functions and classes designed to simplify terminal-based interactions and formatting. It offers tools to manage terminal output, handle user interactions, and apply text styling.

## Features

- **Terminal Management**: Clear screens, retrieve terminal dimensions, and adjust terminal size.
- **Text Formatting**: Print styled messages, headers, and dividers with uniform formatting.
- **User Interaction**: Prompt for user input, display key-value pairs, and wait for user actions.
- **Styling**: Apply various text styles and colors to enhance readability and presentation.

## Installation

Clone the repository and include it in your Python project. No additional installation is required.

## Usage

Here’s a brief example of using the utilities:

```python
from src.terminal_utils import clear_screen, get_terminal_size
from src.formatting import line, header
from src.user_interaction import prompt_for_input

# Clear the terminal screen
clear_screen()

# Print a header
header("Welcome to the Utility Package")

# Prompt for user input
user_name = prompt_for_input("Enter your name:", str)

# Print a formatted line
line(f"Hello, {user_name}", type="success")
```

## Directory Structure

```
.
├── LICENSE
├── MANIFEST
├── README.md
├── script.sh
└── src
    ├── display.py
    ├── formatting.py
    ├── __init__.py
    ├── screen.py
    ├── styles.py
    ├── terminal_handler.py
    ├── terminal_utils.py
    └── user_interaction.py
```

## Core Goal

The primary aim of this package is to provide a clean and minimalistic foundation for terminal-based applications. By centralizing and standardizing core functionalities, this package promotes consistency and efficiency, reducing redundancy and ensuring a polished, uniform look for your terminal applications.

## License

This project is licensed under the terms of the [MIT License](LICENSE).

## Author

- **Vincent de Torres** - [GitHub Profile](https://github.com/devinci-it)

For more details and examples, refer to the source code and inline documentation in the `src` directory.

---

