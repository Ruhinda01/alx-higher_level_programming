#!/usr/bin/python3
"""Rectangle module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a child class
    Args:
        BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Gets the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """
        String representation of the rectangle
        """
        return "[{}] {:d}/{:d}".format(
                self.__class__.__name__, self.__width, self.__height)
