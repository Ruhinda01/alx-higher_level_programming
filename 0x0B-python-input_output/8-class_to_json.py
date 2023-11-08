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
