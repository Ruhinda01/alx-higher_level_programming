#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    Args:
        filename (string)
        text (string)
    Return:
        number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        written = f.write(text)
    return written
