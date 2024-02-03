#!/usr/bin/python3
"""Class Square with size attribute"""


class Square:
    """Class Square with size attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes size as private attribute for Square class"""
        self._size = size
        self.position = position

    @property
    def size(self):
        """getter for size attribute
        """
        return self._size

    @size.setter
    def size(self, new_size):
        """setter for size attribute
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self._size = new_size

    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the area of a square
        Returns:
            int: the area of the square
        """
        return self._size**2

    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for j in range(self.position[0]):
                    print(" ", end='')
                for k in range(self.size):
                    print("#", end='')
                print()
