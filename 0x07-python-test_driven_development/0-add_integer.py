#!/usr/bin/python3
"""
add_integer function that adds 2 intgers
"""


def add_integer(a, b=89):
    """
    adds two integers (a, b)
    Args:
        a (int): number 1
        b (int): number 2
    Raises:
        TypeError: a or b must be an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
