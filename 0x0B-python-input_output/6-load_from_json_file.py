#!/usr/bin/python3
"""This function creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file.
    Args:
        filename: The JSON file to be loaded
    Return:
        The created object
    """
    with open(filename) as f:
        return json.loads(f.read())
