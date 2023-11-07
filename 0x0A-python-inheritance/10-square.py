#!/usr/bin/python3
"""Square child module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        __init__ method
        Args:
            size (int): size
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Area of the square
        """
        return self.__size * self.__size
