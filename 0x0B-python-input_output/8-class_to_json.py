#!/usr/bin/python3
""" Class to JSON module."""


def class_to_json(obj):
    """
    Returns the dict descr for json object.
    """
    my_dict = {}
    for attribute in dir(obj):
        if not attribute.startswith('__'):
            value = getattr(obj, attribute)
            if isinstance(value, (list, dict, str, int, bool)):
                my_dict[attribute] = value

    return my_dict
