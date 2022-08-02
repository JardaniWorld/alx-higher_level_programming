#!/usr/bin/python3
"""This function reads a file and prints it to stdout"""


def read_file(filename=""):
    """Combining the utf-8 encoder and
       the with keyword, this function
       reads a file and prints to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
