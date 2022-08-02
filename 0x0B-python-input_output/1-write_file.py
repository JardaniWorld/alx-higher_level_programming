#!/usr/bin/python3
"""This function writes a string to a text file
   and also returns the number of characters written
"""


def write_file(filename="", text=""):
    """This function writes to a text file using write()
    Return:
        Returns the number of characters written
    Args:
        filename: The file to be read from
        text: The string to write into the file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
