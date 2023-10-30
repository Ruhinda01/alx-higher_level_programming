#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """
    A class representing a Square
    """
    def __init__(self, width=0, height=0):
        """
        Initialises rectangle with width and height
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width

        Return:
            the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter of the width
        Args:
            value (int): width of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height

        Return:
            the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter of the height
        Args:
            value (int): height of the rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
