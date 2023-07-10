#!/usr/bin/python3
""" LookUp Module. """


def lookup(obj):
    """
    Returns list of available attributes and methods.
    """
    lookup_list = list(dir(obj))
    return lookup_list
