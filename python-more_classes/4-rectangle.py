#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle. Must be integer and >= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle. Must be integer and >= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        x = self.width
        y = self.height
        return x * y

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        x = self.width
        y = self.height
        p = 2 * (x + y)
        if x == 0 or y == 0:
            return 0
        return p

    def __str__(self):
        """Prints the rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)