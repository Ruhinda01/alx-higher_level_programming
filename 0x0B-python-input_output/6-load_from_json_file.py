#!/usr/bin/python3
"""Object from json file module"""
import json


def load_from_json_file(filename):
    """
    creates an object from JSON file
    Args:
        filename (str)
    """
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
    return data
