#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return

    sorted_dict = {k: v for k, v in sorted(a_dictionary.items())}

    for key, value in sorted_dict.items():
        print(("{}: {}").format(key, value))
