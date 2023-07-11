#!/usr/bin/python3
""" From JSON to object module. """


import json


def from_json_string(my_str):
    """
    Returns a python object from JSON str.
    """
    py_data = json.loads(my_str)

    return py_data
