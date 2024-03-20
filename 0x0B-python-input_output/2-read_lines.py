#!/usr/bin/python3
"""defines a reading funct for text files"""


def read_lines(filename="", num_lines=0):
    """
    Print given number of lines from UTF8 file
    """
    with open(filename, encoding="utf-8") as f:
        if num_lines <= 0:
            print(f.read(), end="")
            return

        lines = 0
        for line in f:
            lines += 1
        f.seek(0)
        if num_lines >= lines:
            print(f.read(), end="")
            return

        else:
            n = 0
            while n < num_lines:
                print(f.readline(), end="")
                n += 1
