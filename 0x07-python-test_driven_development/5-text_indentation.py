#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 newlines
    Args:
        text (str): string
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_str = ""
    x = 0
    while x < len(text):
        new_str += text[x]
        if text[x] in ['.', '?', ':']:
            new_str = new_str.strip()
            print(new_str)
            print()
            if x + 1 < len(text) and text[x + 1] == ' ':
                x += 1
            new_str = ""
        x += 1

    if len(new_str) > 0:
        print(new_str, end="")
