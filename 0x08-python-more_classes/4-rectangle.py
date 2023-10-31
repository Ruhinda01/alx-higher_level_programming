#!/usr/bin/python3
"""A rectangle module"""


class Rectangle:
    """
    A class representing a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialises rectangle by width and height
        Args:
            width (int): width
            height (int): height
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
            value (int): width of rectangle
        Raises:
            TypeError: width must be int
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
            value (int): height of rectangle
        Raises:
            TypeError: height must be an int
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of rectangle

        Return:
            area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter of rectangle

        Return:
            the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Representation of string as '#'

        Returns:
            string
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height - 1):
            for j in range(self.width):
                string += "#"
            string += "\n"
        string += '#' * self.width
        return string

    def __repr__(self):
        """
        String rep of the rectangle

        Return:
            the string rep
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
