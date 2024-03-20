#!/usr/bin/python3
"""A JSON-to-object function"""
import json


def from_json_string(my_str):
    """
    return object representation of a json string
    """
    return json.loads(my_str)
