#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """ Append a string to a text file

    Args:
        filename (str, optional): File to append string and
        create if necessary. Defaults to "".
        text (str, optional): String to append. Defaults to "".

    Returns:
        int: Number of characters appended
    """
    with open(filename, 'a', encoding="utf-8")as f:
        return f.write(text)
