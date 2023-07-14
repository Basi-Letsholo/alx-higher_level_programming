#!/usr/bin/python3
""" Rectanlge Class module. """


class Rectangle:
    """ Initialise public class attributes.
    """
    number_of_instances = 0

    """
    Initialise Rectangle attributes.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        if not hasattr(self, "_print_symbol"):
            self._print_symbol = '#'
        Rectangle.number_of_instances += 1

    """ Retrieves property for public attr.
    """
    @property
    def print_symbol(self):
        return self._print_symbol

    """ Sets public attr.
    """
    @print_symbol.setter
    def print_symbol(self, value):
        self._print_symbol = value

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

    """ Sets Rectangle width.
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

    """ Prints rectangle with char '#' .
    """
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''

        rect = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect = rect + str(self.print_symbol)
            if i < self.__height - 1:
                rect = rect + '\n'

        return rect

    """ Defines string repr of Rectangle.
    """
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """ Method called when an instance is being destroyed.
    """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """ Returns bigger rect (by area).
    """
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 == area_2:
            return rect_1
        if area_1 > area_2:
            return rect_1
        return rect_2

    """ Class method that creates a new Rect instance.
    """
    @classmethod
    def square(cls, size=0):
        square = cls(size, size)
        return square
