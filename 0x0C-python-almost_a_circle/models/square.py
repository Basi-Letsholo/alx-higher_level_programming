#!/usr/bin/python3
""" Square Class Module, inherits Rectangle. """

import sys
import os


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from  models.rectangle import Rectangle


class Square(Rectangle):
    """ Initialise Square attributes.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """ Retrieves size.
    """
    @property
    def size(self):
        return self.width

    """ Sets size of Square.
    """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    """ Defines str repr of Square.
    """
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    """ Assigns attributes.
    """
    def update(self, *args, **kwargs):
        if len(args) > 0:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i >= len(attr):
                    break
            setattr(self, attr[i], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """ Returns dictionary repr of Square.
    """
    def to_dictionary(self):
        sq_dict = {}
        sq_dict['id'] = self.id
        sq_dict['size'] = self.width
        sq_dict['x'] = self.x
        sq_dict['y'] = self.y

        return sq_dict
