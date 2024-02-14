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
        """ Setter for size

        Args:
            value (int): size of the square
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square class.

        Args:
            args (tuple): tuple of arguments
            kwargs (dict): dictionary of arguments
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square.

        Returns:
            dict: dictionary representation of a Square
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
