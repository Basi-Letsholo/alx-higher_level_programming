#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= 0:
        list_len = len(my_list)

        if idx >= list_len:
            return my_list
        elif idx < list_len:
            my_list[idx] = element
            return my_list
