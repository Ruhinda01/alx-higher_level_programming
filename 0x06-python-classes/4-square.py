#!/usr/bin/python3
"""Square module"""


class Square:
    def __init__(self, size=0):
        """
        Initialises square with a size
        Args:
            size (int): size of square
        """
        self.size = size

    def area(self):
        """
        Area gets the are of the square

        Return:
            the current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of the size value

        Args:
            value (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
