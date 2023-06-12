#!/usr/bin/python3

def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len <= 0:
        return None
    else:
        max = my_list[0]
        for i in range(0, list_len):
            if max < my_list[i]:
                max = my_list[i]

    return max
