#!/usr/bin/python3
"""This function returns an object(Python data structure)
   represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """This code returns an object rep'd by a JSON string.
    Args:
        my_str: The JSON string to be converted
    Return:
        An object represented by a JSON string
    """
    return json.loads(my_str)
