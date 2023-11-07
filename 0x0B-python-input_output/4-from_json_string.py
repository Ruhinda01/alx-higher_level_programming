#!/usr/bin/python3
"""string to obj module"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str (json str)
    Return:
        an object reprsented by a JSON string
    """
    return json.loads(my_str)
