#!/usr/bin/python3
"""JSON to obj module"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    Args:
        my_obj (str)
    """
    return json.dumps(my_obj)
