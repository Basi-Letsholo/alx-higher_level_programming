#!/usr/bin/python3
""" To Json string module. """


import json


def to_json_string(my_obj):
    """
    Returns JSON repr of string.
    """
    json_str = json.dumps(my_obj)

    return json_str
