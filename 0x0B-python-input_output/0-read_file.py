#!/usr/bin/python3
""" Module to read a text file. """


def read_file(filename=""):
    """
    Opens and reads text file.
    """
    with open(filename, "r", encoding="UTF8") as file_r:
        print(file_r.read(), end='')
