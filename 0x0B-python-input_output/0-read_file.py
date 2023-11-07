#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """
    Reads the text file and prints it out to stdout
    Args:
        filename
    """
    with open(filename, encoding='utf-8') as f:
        data = f.read()
        print(data, end="")
