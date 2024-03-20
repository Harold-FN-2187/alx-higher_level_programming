#!/usr/bin/python3
"""defines a line-counting funct for text files"""


def number_of_lines(filename=""):
    """returns the number of lines in a text file"""
    line_num = 0
    with open(filename) as f:
        for line in f:
            line_num += 1
        return line_num
