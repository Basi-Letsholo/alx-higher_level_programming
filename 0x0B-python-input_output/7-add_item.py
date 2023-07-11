#!/usr/bin/python3
""" Script that adds arguments to py list then saves as JSON file. """


import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


py_list = []
if len(argv) > 1:
    for i in range(1, len(argv)):
        py_list.append(argv[i])
try:
    data = load_from_json_file("add_item.json")
    py_list = data + py_list

except:
    pass

save_to_json_file(py_list, "add_item.json")
