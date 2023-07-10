#!/usr/bin/python3
""" Base Geometry module. """


class BaseGeometry:
    """
    Raises an exception.
    """
    def area(self):
        raise Exception("area() is not implemented")

    """
    Validates value is a positive int.
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
