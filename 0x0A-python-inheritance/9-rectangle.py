#!/usr/bin/python3
""" Rectangle class which inherits BaseGeometry. """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Initialises Rectangle attributes.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """
    Define area for Rectangle.
    """
    def area(self):
        return self.__width * self.__height

    """
    Define str representation for Rectangle.
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
