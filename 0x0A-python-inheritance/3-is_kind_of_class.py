#!/usr/bin/python3
"""is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    checks if object is instance of or if the object is an instance
    of a class that inherited from the specified class
    Args:
        obj (object): object
        a_class (type): data type
    Return:
        True
        False
    """
    if isinstance(obj, a_class):
        return True
    return False
