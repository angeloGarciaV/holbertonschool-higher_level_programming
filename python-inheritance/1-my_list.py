#!/usr/bin/python3
"""MyList module."""


class MyList(list):
    """_summary_

    Args:
        list (list): list to be inherited from
    """

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
