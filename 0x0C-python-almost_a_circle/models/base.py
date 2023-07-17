#!/usr/bin/python3
""" Base Class module. """


import json


class Base:
    """ Private class attribute.
    """
    __nb_objects = 0

    """ Initialise attributes.
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """ Returns JSON str of list dictionaries.
    """
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        if list_dictionaries == {}:
            return "[]"

        json_str = json.dumps(list_dictionaries)
        return json_str

    """ Returns list of json str rep. 
    """
    def from_json_string(json_string):
        if json_string is None:
            return []

        j_list = list(json.loads(json_string))
        return j_list
