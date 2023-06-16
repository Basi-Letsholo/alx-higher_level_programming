#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None:
        return

    len_list = len(my_list)
    if len_list < 1:
        return my_list

    new_list = my_list[:]
    for i in range(0, len_list):
        if search == my_list[i]:
            idx = i
            new_list[idx] = replace

    return new_list
