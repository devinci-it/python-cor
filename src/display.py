# src/utils/display.py

"""
Terminal display utilities for standardized output formats.

Author    : Vincent de Torres
GitHub    : https://github.com/devinci-it
File      : src/utils/display.py

This module provides functions for printing standardized output formats, such as headers and tables. 
It includes functionality to display headers, tables, and other formatted output with customizable styles.
"""

from prettytable import PrettyTable
from src.utils.terminal import get_terminal_width
from src.utils.styles import Styles

def print_header(file_path, task_number):
    """
    Print a standardized header message to the CLI.
    """
    col, _ = get_terminal_size()
    MODERN_BLUE_TEXT = '\033[38;2;94;129;172m'
    LIGHT_SNOW_BACKGROUND = '\033[48;2;236;239;244m'
    border = f"{'━' * (col-8):<{col-8}}"
    header = (
        f" {border}\n"
        f"\t{Styles.BOLD}{Styles.RESET} {file_path} | Task {task_number} | Vincent De Torres | SMCCS87A | FINALS{Styles.RESET}\n"
        f" {border}\n"
        f"{Styles.RESET}"
    )
    print(header)

def print_dataframe_as_pretty_table(
    df, 
    column_widths=None,  # Custom column widths
    align='l',  # Column alignment
    border=True,  # Show table border
    header=True,  # Show table header
    header_style='title',  # Header style
    padding_width=8  # Padding for table cells
):
    """
    Print a DataFrame as a formatted PrettyTable.
    """
    if df.empty:
        print("The DataFrame is empty.")
        return
    
    table = PrettyTable()
    table.field_names = df.columns.tolist()
    
    for column in df.columns:
        if column_widths and column in column_widths:
            table.max_width[column] = column_widths[column]
        else:
            max_length = max(df[column].astype(str).map(len).max(), len(column))
            table.max_width[column] = max_length

    for _, row in df.iterrows():
        table.add_row(row.tolist())
    
    table.align = align  
    table.border = border 
    table.header = header  
    table.header_style = header_style 
    table.padding_width = padding_width  
    
    print_table_with_indent(table, indent=16) 

def print_table_with_indent(table, indent=0):
    """
    Print a PrettyTable object with a specified indent.
    """
    table_str = str(table)
    lines = table_str.split('\n')
    indent_str = ' ' * indent
    for line in lines:
        print(indent_str + line)

