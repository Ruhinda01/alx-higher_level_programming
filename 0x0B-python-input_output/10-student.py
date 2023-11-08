#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """
        Instantiation
        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary rep of the student instance
        Args:
            attr (list)
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
