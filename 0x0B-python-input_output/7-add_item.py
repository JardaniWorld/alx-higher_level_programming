#!/usr/bin/python3
"""This script adds all arguments to a Python
   list, and then save them to a file.
"""


from sys import argv

s = __import__('5-save_to_json_file.py').save_to_json_file
l = __import__('6-load_from_json_file.py').load_from_json_file

try:
    files_before = l('add_item.json')
except FileNotFoundError:
    files_before = []

lists = files_before + argv[1:]

s(lists, 'add_item.json')
