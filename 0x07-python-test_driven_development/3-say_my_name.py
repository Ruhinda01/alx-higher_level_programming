#!/usr/bin/python3
"""Say my name"""


def say_my_name(first_name, last_name=""):
    """
    Say my name
    Args:
        first_name (str): string 1
        last_name (str): string 2
    Raises:
        TypeError: first / last name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
