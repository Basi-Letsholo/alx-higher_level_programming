#!/usr/bin/python3
""" Module to read a text file. """


def read_file(filename=""):
    """
    Opens and reads text file.
    """
    with open(filename, mode="r", encoding="utf-8") as read_file:
        read_file.read()
