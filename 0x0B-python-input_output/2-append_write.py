#!/usr/bin/python3
""" Appends to text file. """


def append_write(filename="", text=""):
    """
    Appends text to filename, returns number of chars appended.
    """
    with open(filename, 'a', encoding='UTF8') as a_file:
        chars_added = a_file.write(text)

    return chars_added
