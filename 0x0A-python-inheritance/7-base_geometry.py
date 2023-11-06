#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """
    This is the base geometry class
    """
    def area(self):
        """
        This is the area method
        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        Raises:
            TypeError
            ValueError
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
