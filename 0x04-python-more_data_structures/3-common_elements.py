#!/usr/bin/python3

def common_elements(set_1, set_2):
    if len(set_1) < 1 or len(set_2) < 1:
        return

    new_set = set_1.intersection(set_2)
    return new_set
