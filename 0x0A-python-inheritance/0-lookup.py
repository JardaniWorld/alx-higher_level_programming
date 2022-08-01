#!usr/bin/python3
# 0-lookup.py
def lookup(obj):
    """The function: lookup, returns the list of all

    available attributes and methods of an object.
    """
    return lookup.__dict__.keys()
