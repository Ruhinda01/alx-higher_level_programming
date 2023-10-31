#!/usr/bin/python3
"""A rectangle module"""


class Rectangle:
    """
    A class representing a rectangle with its sides

    Attributes:
        number_of_instances (int): number of new rectangle instances
        print_symbol : symbol of string repr
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialises rectangle by width and height
        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter of the width
        Args:
            value (int): width of rectangle
        Raises:
            TypeError: width must be integer
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
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter of the height
        Args:
            value (int): height of rectangle
        Raises:
            TypeError: height must be an integer
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
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Representation of string as '#'
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height - 1):
            for j in range(self.width):
                string += str(self.print_symbol)
            string += "\n"
        string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """
        String rep of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        Deletes the instance of the rectangle
        Sends the message.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
