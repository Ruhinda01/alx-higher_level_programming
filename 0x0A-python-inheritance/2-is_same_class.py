#!/usr/bin/python3
"""is_same_class function"""


def is_same_class(obj, a_class):
    """
    Args:
        obj (object): object
        a_class (type): data type
    Return:
        true if object is an instance of class
        false is not
    """
    return type(obj) == a_class
