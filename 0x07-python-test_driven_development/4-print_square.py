#!/usr/bin/python3
"""Print the square"""


def print_square(size):
    """
    prints a square with '#'
    Args:
        size (int): size of thr square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size > 0:
        for i in range(size):
            print("#" * size)
