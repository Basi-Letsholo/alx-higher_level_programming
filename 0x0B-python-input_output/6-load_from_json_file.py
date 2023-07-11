#!/usr/bin/python3
""" Load from JSON file module. """


import json


def load_from_json_file(filename):
    """
    Returns py object from json file.
    """
    with open(filename, 'r') as r_file:
        data = r_file.read()

    my_obj = json.loads(data)

    return my_obj
