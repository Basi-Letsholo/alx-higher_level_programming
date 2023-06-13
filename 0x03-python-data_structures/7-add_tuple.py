#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a < 2:
        if len_a == 1:
            list_a = [(tuple_a[0]), 0]
        elif len_a < 1:
            list_a = [0, 0]
    elif len_a >= 2:
        list_a = [(tuple_a[0]), (tuple_a[1])]

    if len_b < 2:
        if len_b == 1:
            list_b = [(tuple_b[0]), 0]
        elif len_b < 1:
            list_b = [0, 0]
    elif len_b >= 2:
        list_b = [(tuple_b[0]), (tuple_b[1])]

    new_tup = ((list_a[0] + list_b[0]), (list_a[1] + list_b[1]))
    return new_tup
