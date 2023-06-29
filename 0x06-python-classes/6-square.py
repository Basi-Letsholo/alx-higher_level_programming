#!/usr/bin/python3
""" Defines a Class for Square. """


class Square:
    """
    Initialises Square attributes.
    """
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

    """
    Gets size of Square.
    """
    @property
    def size(self):
        return self.__size

    """
    Sets size of Square.
    """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    """
    Gets position of Square.
    """
    @property
    def position(self):
        return self.__position

    """
    Sets position of Square.
    """
    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    """
    Defines area of Square.
    """
    def area(self):
        return pow(self.__size, 2)
        

    """
    Prints Out Square using '#'.
    """
    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                for j in range(self.__size):
                    print('#', end='')
                print('')

