#!/usr/bin/python3
"""Empty class that defines a rectangle"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Retrieves private instance attribute size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width * self.__height)
