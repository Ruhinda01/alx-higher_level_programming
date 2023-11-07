#!/usr/bin/python3
"""add_attribute function"""


def add_attribute(obj, attr, value):
    """
    Add an attribute to an object if possible
    Args:
        obj: object
        attr: atrribute to be named
        value: value to be assigned to the attribute
    Raises:
        TypeError
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
