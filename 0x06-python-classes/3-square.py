#!/usr/bin/python3
"""Class that defins a square with some attributes and instantiation"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Initializes a Square instance"""

        """Args used:
            size : size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return current area of the square"""

        return (self.__size * self.__size)
