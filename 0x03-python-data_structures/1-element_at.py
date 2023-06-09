#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= 0:
        list_len = len(my_list)
        if idx >= list_len:
            return None
        elif idx < list_len:
            return my_list[idx]
