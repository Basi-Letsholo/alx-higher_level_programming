#!/usr/bin/python3
""" Module to write to text file. """


def write_file(filename="", text=""):
    """
    writes text to file, returns number of characters written.
    """
    with open(filename, 'w', encoding='UTF8') as w_file:
        chars_read = w_file.write(text)

    return chars_read
