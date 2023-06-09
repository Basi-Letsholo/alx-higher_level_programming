#!/usr/bin/python3
""" Defines a class called Square. """


class Square:
    """
    Defines Square attributes.
    """
    def __init__(self, size=0):
        self.__size = size

    """
    Gets size of square.
    """
    @property
    def size(self):
        return self.__size

    """
    Sets size.
    """
    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    """
    Defines area of square.
    """
    def area(self):
        _area = pow(self.__size, 2)

        return _area
