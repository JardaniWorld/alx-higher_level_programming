#!usr/bin/python3
# 0-lookup.py
"""This defines an object attribute lookup function."""



def lookup(obj):
    """The function: lookup, returns the list of all

    available attributes and methods of an object.
    """
    return (dir(obj))
