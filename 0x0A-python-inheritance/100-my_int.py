#!/usr/bin/python3
""" MyInt Class which inherits from int."""


class MyInt(int):
    """
    Initialises MyInt attributes.
    """
    def __init__(self, value):
        self.__value = int(value)

    """
    Inverts '=='.
    """
    def __eq__(self, other):
        return not (self.__value == other)

    """
    Inverts '!='.
    """
    def __ne__(self, other):
        return not (self.__value != other)
