#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle

    Args:
        Rectangle (class): Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new instance of Square.

        Args:
            size (int): size of the square
            x (int, optional): x position of the square. Defaults to 0.
            y (int, optional): y position of square. Defaults to 0.
            id (int, optional): id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square class.

        Returns:
            string: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Getter for size

        Returns:
            int: size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
