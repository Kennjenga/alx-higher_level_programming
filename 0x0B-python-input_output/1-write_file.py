#!/usr/bin/python3

"""Defines a file-writing function with error handling."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        None
    """

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
    except (IOError, OSError) as e:
        print(f"Error writing to file '{filename}': {e}")


