#!/usr/bin/python3
""" Defines a class, Rectangle. """


class Rectangle:
    """
    Initialises Rectangle attributes.
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
    Defines perimeter of Rectangle.
    """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0

        return ((self.__width * 2) + (self.__height * 2))

    """
    """
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ''

        rect = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect = rect + '#'
            if i < self.__height - 1:
                rect = rect + '\n'

        return rect
