#!/usr/bin/python3
"""A string-to_JSON function"""
import json


def to_json_strin(my_obj):
    """
    returns JSON represenation of a string object
    """
    return json.dumps(my_obj)
