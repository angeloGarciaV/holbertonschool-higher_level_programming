#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize the rectangle with width and height.
        Counts instances of Rectangle"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        x = self.width
        y = self.height
        if x == 0 or y == 0:
            return ""
        else:
            return "\n".join([str(self.print_symbol) * x for _ in range(y)])

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted
        and decrements the count of instances of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
