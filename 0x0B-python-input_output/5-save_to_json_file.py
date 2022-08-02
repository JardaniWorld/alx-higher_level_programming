#!/usr/bin/python3
"""This function writes an object to a text file,
   using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation.
    Args:
        my_obj: Object to be converted to a JSON object
        filename: A pointer to JSON file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
