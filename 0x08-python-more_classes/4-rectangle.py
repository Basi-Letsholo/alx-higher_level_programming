#!/usr/bin/python3
""" Rectangle class module. """


class Rectangle:
    """
    Initialises Rectangle attributes.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Retrieves width property.
    """
    @property
    def width(self):
        return self.__width

    """ Retrieves height property.
    """
    @property
    def height(self):
        return self.__height

    """ Sets width of Rectangle.
    """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """ Sets height of Rectangle.
    """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """ Defines area of Rectangle.
    """
    def area(self):
        return self.__width * self.__height

    """ Defines perimeter of Rectangle.
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''

        rect = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect = rect + '#'
            if i < self.__height - 1:
                rect = rect + '\n'

        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
