#!/usr/bin/python3
""" Module to write to text file. """


def write_file(filename="", text=""):
    """
    writes text to file, returns number of characters written.
    """
    with open(filename, 'w', encoding='UTF8') as w_file:
        w_file.write(text)

    with open(filename, 'r', encoding='UTF8') as r_file:
        chars_read = len(r_file.read())

    return chars_read
