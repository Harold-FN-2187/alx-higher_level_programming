#!/usr/bin/python3
"""Checks an object for some condition"""


def is_kind_of_class(obj, a_class):
    """
    Check of object is an instance of a class
    or if object is instance of inherited class

    Arguments:
    obj : Object to run check against
    a_class : Class that object is run against

    Return:
    TRUE - if object is an instance or inherited instance of a_class
    FALSE - otherwise

    """
    if isinstance(obj, a_class):
        return True
    return False
