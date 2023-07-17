#!/usr/bin/python3
""" Rectangle class module, inherits Base. """


import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)


from models.base import Base


class Rectangle(Base):
    """
    Initialise attributes.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """ Retrieve width.
    """
    @property
    def width(self):
        return self.__width

    """ Retrieves height.
    """
    @property
    def height(self):
        return self.__height

    """ Retrieves x.
    """
    @property
    def x(self):
        return self.__x

    """ Retrieves y.
    """
    @property
    def y(self):
        return self.__y

    """ Set width.
    """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    """ Set height.
    """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("must be > 0")

        self.__height = value

    """ Set x.
    """
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    """ Set y.
    """
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    """ Defines area of Rectangle.
    """
    def area(self):
        return self.__width * self.__height

    """ Prints Rectangle with '#'.
    """
    def display(self):
        for _ in range(self.__y):
            print('')
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            for j in range(self.__width):
                print('#', end='')
            print('')

    """ Defines str repr of Rectangle.
    """
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    """ Assigns attributes.
    """
    def update(self, *args, **kwargs):
        attr = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i >= len(attr):
                break
            setattr(self, attr[i], arg)

        for key, value in kwargs.items():
            setattr(self, key, value)

    """ Returns dictionary repr of Rectangle.
    """
    def to_dictionary(self):
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.__width
        rect_dict['height'] = self.__height
        rect_dict['x'] = self.__x
        rect_dict['y'] = self.__y

        return rect_dict
