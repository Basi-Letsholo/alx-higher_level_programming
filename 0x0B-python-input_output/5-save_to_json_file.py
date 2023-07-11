#!/usr/bin/python3
""" Save to JSON module. """


import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to textfile in json.
    """
    j_str = json.dumps(my_obj)

    with open(filename, 'w') as json_file:
        json_file.write(j_str)
