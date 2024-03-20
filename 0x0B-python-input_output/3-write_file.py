#!/usr/bin/python3
"""File writing function"""


def write_file(filename="", text=""):
    """
    Writes a string to an UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
