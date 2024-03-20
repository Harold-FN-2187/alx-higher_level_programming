#!/usr/bin/python3
"""A python class-to-JSON function"""


def class_to_json(obj):
    """returns dictionary representation of a data structure"""
    return obj.__dict__
