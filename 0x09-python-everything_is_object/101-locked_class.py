#!/usr/bin/python3
"""defines a local class"""


class LockedClass:
    """
    Prevents instantiation of new LockedClass attributes except for
    attributes called 'first_name'
    """

    __slots__ = ["first_name"]
