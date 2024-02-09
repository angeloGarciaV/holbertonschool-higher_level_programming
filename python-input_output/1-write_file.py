#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """ Write a string to a text file

    Args:
        filename (str, optional): File to write to. Defaults to "".
        text (str, optional): Line to write to file. Defaults to "".

    Returns:
        int: Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
