#!/usr/bin/python3
"""This function appends a string at the end
   of a text file and also returns the number
   of characters added.
"""


def append_write(filename="", text=""):
    """This appends a string at the end of a file.
    Return:
        The number of characters appended to the file
    Args:
        filename: Text file to append to
        text: The string to append to text file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
