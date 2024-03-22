#!/usr/bin/python3
"""Checks object for some condition"""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of class
    that inherited directly/indirectly from the specified class

    Args:
    obj:  Object to run check on
    a_class: Specified class to run check against

    Return:
    TRUE - if obj is an instance
    FALSE - otherwise
    """

    if issubclass(type(obj), a_class) and not isinstance(obj, a_class):
        return True
    return False
