#!usr/bin/python3
# 0-lookup.py
def lookup(obj):
    """The function: lookup, returns the list of all

    available attributes and methods of an object.
    """
    return [func for func in dir(lookup) if callable(getattr(lookup, func))]
