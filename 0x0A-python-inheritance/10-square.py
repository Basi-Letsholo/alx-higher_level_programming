#!/usr/bin/python3
""" Defines Class Square which inherits from Rectangle. """


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
    Defines str repr.
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
