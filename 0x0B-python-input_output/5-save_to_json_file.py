#!/usr/bin/python3
"""Object to a text file module"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation
    Args:
        my_obj (object)
        filename (str)
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
