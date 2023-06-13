#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list

    list_len = len(my_list)
    if idx >= list_len:
        return my_list

    elif idx < list_len:
        for i in range(idx, list_len -1):
            my_list[i] = my_list[i + 1]
        my_list = my_list[:list_len - 1]

    return my_list
