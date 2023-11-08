#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """
    Args:
        obj: an instance of class
    Return:
        the dictionary description
    """
    return obj.__dict__


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

    def to_json(self):
        """
        Retrieves a dictionary rep of the student instance
        """
        return class_to_json(self)
