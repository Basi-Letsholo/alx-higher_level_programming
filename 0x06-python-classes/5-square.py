#!/usr/bin/python3
""" Defines a class for a Square. """


class Square:
    """
    Initialises Attributes.
    """
    def __init__(self,size=0):
        self.__size = size

    """
    Gets Size of square.
    """
    @property
    def size(self):
        return self.__size

    """
    Sets Size of Square.
    """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    """
    Defines area of Square.
    """
    def area(self):
        _area = pow(self.__size, 2)
        return _area

    """
    Prints out Square with '#'
    """
    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print('')










