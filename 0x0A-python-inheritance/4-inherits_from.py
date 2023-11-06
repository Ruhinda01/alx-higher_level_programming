#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """
    If object is an instance of a class that inherited
    (directly or indirectly) from specified class
    Args:
        obj
        a_class
    Return:
        True
        False
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
