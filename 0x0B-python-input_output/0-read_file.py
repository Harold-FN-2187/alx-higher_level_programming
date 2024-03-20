#!/usr/bin/python3
"""defines a file-reading func"""


def read_file(filename=""):
    """Prints the content of a UTF9 file to standard output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
