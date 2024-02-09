#!/usr/bin/python3
"""MyList module."""


class MyList(list):
    """Class that inherits from list.

    Args:
        list (list): list to be inherited from
    """

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
