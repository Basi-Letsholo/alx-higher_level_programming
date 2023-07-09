#!/usr/bin/python3
""" Defines a class, Rectangle. """


class Rectangle:
    """
    Initialies width and height of Rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """
    Retrieves width property.
    """
    @property
    def width(self):
        return self.__width

    """
    Retrieves height property.
    """
    @property
    def height(self):
        return self.__height

    """
    Sets width of Rectangle.
    """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """
    Sets height of Rectangle.
    """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """
    Defines area of Rectangle.
    """
    def area(self):
        return self.__height * self.__width

    """
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return ((self.__width * 2) + (self.__height * 2))
