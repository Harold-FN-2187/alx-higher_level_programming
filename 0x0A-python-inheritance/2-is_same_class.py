#!/usr/bin/python3
"""Checks a class for some condition"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class

    Arguments:
    obj : The object to run check against

    Return:
    TRUE if object is exactly an instance of a_class
    FALSE otherwise
    """
    if type(obj) == a_class:
        return True
    return False
