#!/usr/bin/python3
"""Square module"""


class Square:
    """
    A class representing a Square.
    """
    def __init__(self, size=0):
        """
        Initialises square with a size.

        Args:
            size (int): size of square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
