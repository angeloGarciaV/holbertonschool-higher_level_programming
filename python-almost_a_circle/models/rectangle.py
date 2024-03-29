#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base

    Args:
        Base (class): Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x coordinate of the rectangle. Defaults to 0.
            y (int, optional): y coordinate of the rectangle. Defaults to 0.
            id (int, optional): id of the rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for width

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width

        Args:
            value (int): width for the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height

        Args:
            value (int): height for the rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x

        Returns:
            int : value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x

        Args:
            value (int): value for x
        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y

        Returns:
            int: value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """String representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the rectangle

        Args:
            args (tuple): tuple of arguments
            kwargs (dict): dictionary of arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle

        Returns:
            dict: dictionary representation of the Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "y": self.y,
            "x": self.x
        }
