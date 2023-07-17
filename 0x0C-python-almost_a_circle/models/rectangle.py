#!/usr/bin/python3
""" Rectangle class module, inherits Base. """


import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialise attributes.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieve property.
        """
        return self.__width

    @property
    def height(self):
        """ Retrieve property.
        """
        return self.__height

    @property
    def x(self):
        """ Retrieve property.
        """
        return self.__x

    @property
    def y(self):
        """ Retrieve property.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """ Set width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """ Set height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """ Set x.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """ Set y.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Defines area of Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """ Prints Rectangle with '#'.
        """
        for _ in range(self.__y):
            print('')
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            for j in range(self.__width):
                print('#', end='')
            print('')


    def __str__(self):
        """ Defines str repr of Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
         """ Assigns attributes.
        """

        attr = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i >= len(attr):
                break
            setattr(self, attr[i], arg)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary repr of Rectangle.
        """

        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.__width
        rect_dict['height'] = self.__height
        rect_dict['x'] = self.__x
        rect_dict['y'] = self.__y

        return rect_dict
