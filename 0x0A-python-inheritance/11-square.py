#!/usr/bin/python3
""" Defines a class, Square, which inherits from Rectangle. """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Initialises Square attributes.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    """
    Defines area of Square.
    """
    def area(self):
        return pow(self.__size, 2)

    """
    Defines str repr of Square.
    """
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
