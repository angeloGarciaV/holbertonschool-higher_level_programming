#!/usr/bin/python3
""" Module for read_file method"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
