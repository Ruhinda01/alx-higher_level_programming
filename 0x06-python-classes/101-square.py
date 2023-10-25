#!/usr/bin/python3
"""Square module."""


class Square:
    """
    A class representing a Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises square with a size and position
        Args:
            size (int): size of the square
            position (tuple): coordinates of a square
        """
        self.size = size
        self.position = position

        def area(self):
            """
            Area gets the area of the square

            Return:
                the current square area
            """
            return self.__size * self.__size

        @property
        def size(self):
            """
            Gets the size attribute.
            """
            return self.__size

        @size.setter
        def size(self, value):
            """
            Setter of the size attribute

            Args:
                value (int): size of the square
            Raises:
                TypeError: if the size is not an integer
                ValueError: if size is less than zero
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        @property
        def position(self):
            """
            Retrieves the position attribute
            """
            return self.__position

        @position.setter
        def position(self, value):
            """
            Setter of the position value

            Args:
                value (tuple): position of the square
            Raises:
                TypeError: if position is not a tuple of 2 positive integers
            """
            if not isinstance(value, tuple):
                raise TypeError("position must be a tuple of 2 positive integers")
            if len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            if not (isinstance(value[0], int) and isinstance(value[1], int)):
                raise TypeError("position must be a tuple of 2 positive integers")
            if (value[0] < 0 or value[1] < 0):
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

        def __str__(self):
            """
            Prints the representation of a square based on a size."""
            result = ""
            if self.__size == 0:
                return result
            else:
                for i in range(self.__position[1]):
                    result += "\n"
                for j in range(self.__size - 1):
                    result += " " * self.__position[0] + "#" * self.__size + "\n"
                result += " " * self.__position[0] + "#" * self.__size
            return result
