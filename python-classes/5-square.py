#!/usr/bin/python3
"""Class Square with size attribute"""


class Square:
    """Class Square with size attribute"""

    def __init__(self, size=0):
        """Initializes size as private attribute for Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        """calculates the area of a square

        Returns:
            int: the area of the square
        """
        if not isinstance(self._size, int):
            raise TypeError("size must be an integer")
        elif self._size < 0:
            raise ValueError("size must be >= 0")
        return self._size**2

    @property
    def size(self):
        """getter for size attribute

        Returns:
            int: size of the square
        """
        return self._size

    @size.setter
    def size(self, new_size: int):
        """setter for size attribute
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = new_size

    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if not self._size:
            print()
        else:
            for i in range(self._size):
                for j in range(self._size):
                    print("#", end='')
                print()
