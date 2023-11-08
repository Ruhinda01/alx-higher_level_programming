#!/usr/bin/python3
"""Append after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line to text to a file
    after each line containing a specific string
    Args:
        filename (str)
        search_string (str)
        new_string (str)
    """
    new_lines = []
    with open(filename, 'r+', encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        for ln in new_lines:
            f.write(ln)
