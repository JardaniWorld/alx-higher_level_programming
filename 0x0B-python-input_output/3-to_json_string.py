#!/usr/bin/python3
"""This function returns the JSON representation
of an object(string).
"""


def to_json_string(my_obj):
    """Returns the JSON rep of an object(string).
    Args:
        my_obj: The string to be returned
    Return:
        The JSON representation of my_obj
    """
    return json.dumps(my_obj)
