#!usr/bin/python3
# 0-lookup.py
"""This defines an object attribute lookup function."""


def lookup(obj):
    """The function returns the list of an object's available attributes."""
    return (dir(obj))
