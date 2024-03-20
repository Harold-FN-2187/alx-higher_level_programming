#!/usr/bin/python3
"""A JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Creates a python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
