#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """
    lookup function

    Args:
        obj (class)
    Return:
        the list of availble attributes and methods of an object
    """
    att_n_meth = dir(obj)
    return att_n_meth
