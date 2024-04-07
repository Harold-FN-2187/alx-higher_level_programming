#!/usr/bin/python3
"""Defines a class MyList that inherits from `list`"""


class MyList(list):
    """Sorting printing for built-in `list` class"""
    def print_sorted(self):
        """Prints a sorted list in asceding order"""
        print(sorted(self))
