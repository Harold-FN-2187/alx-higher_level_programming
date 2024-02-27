#!/usr/bin/python3
"""lass that defins a square with some attributes and instantiation"""
class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Initializes a new Square instance"""
        self.__size = size

    @property
    def size(self):
        """Retrieve private instance attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Retrieves the private instance attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mut be >= 0")
        self.__size = value

    def area(self):
        """Returns area of Square instance"""
        return (self.__size * self.__size)

    def my_print(self):
        for j in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
