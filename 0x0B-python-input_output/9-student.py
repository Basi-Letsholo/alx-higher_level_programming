#!/usr/bin/python3
""" Student Class module. """


class Student:
    """
    Initialises Student Attributes.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    Retrieves dictionary repr of Student instance.
    """
    def to_json(self):
        my_dict = {}
        for attr in dir(self):
            if not attr.startswith('__'):
                value = getattr(self, attr)
                if isinstance(value, (list, dict, str, int, bool)):
                    my_dict[attr] = value

        return my_dict
