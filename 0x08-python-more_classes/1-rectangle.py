#!/usr/bin/python3
""" Defines a class, Rectangle. """


class Rectangle:
    """
    Initialises width and height attributes.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """
    Retrieves Width.
    """
    @property
    def width(self):
        return self.__width

    """
    Retrieves Height.
    """
    @property
    def height(self):
        return self.__height

    """
    Sets the Width of Rectangle.
    """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """
    Sets the Height of Rectangle.
    """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
