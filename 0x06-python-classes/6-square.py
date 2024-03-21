#!/usr/bin/python3
class Square:
    """Represents a Square"""

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        """Retrieve private instance attribute"""
        return (self.__position)

    @size.setter
    def size(self, value):
        """Retrieves private instance attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mut be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Return current position of square"""
        self.__position = value

    def area(self):
        """Return current area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square using # character"""
        if self.__size == 0:
            print("")
            return
        
        for j in range(0, self.__size):
            [print(" ", end="")for k in range(0, self.__position[0])]
            [print("#", end="") for l in range(self.__size)]
            print("")