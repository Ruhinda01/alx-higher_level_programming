#!/usr/bin/python3
"""Append module"""


def append_write(filename="", text=""):
    """
    Append a string at the end of the text file
    Args:
        filename (str)
        text (str)
    Return:
        number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        written = f.write(text)
    return written
