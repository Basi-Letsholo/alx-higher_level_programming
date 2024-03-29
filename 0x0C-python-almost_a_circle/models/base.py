#!/usr/bin/python3
""" Base Class module. """


import json


class Base:
    """ Base class.
    """

    """ initialise instance counter.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialise attributes.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON str of list dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        if list_dictionaries == {}:
            return "[]"

        json_str = json.dumps(list_dictionaries)
        return json_str

    def from_json_string(json_string):
        """ Returns list of json str rep.
        """
        if json_string is None:
            return []

        j_list = list(json.loads(json_string))
        return j_list

    def save_to_file(cls, list_objs):
        """ Writes json str to file.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + '.json'
        dict_list = [obj.to_dictionary() for obj in list_objs]
        str_to_file = cls.to_json_string(list_objs)

        with open(filename, 'w') as w_file:
            w_file.write(str_to_file)
