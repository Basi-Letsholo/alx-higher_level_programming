#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    if key in a_dictionary:
        pop_key = a_dictionary.pop(key)

    dict_add = {key: value}
    a_dictionary.update(dict_add)

    return a_dictionary
