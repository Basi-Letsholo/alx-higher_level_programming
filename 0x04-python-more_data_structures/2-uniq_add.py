#!/usr/bin/python3

def uniq_add(my_list=[]):
    if len(my_list) < 1:
        return

    sum_set = 0
    my_set = set(my_list)
    for i in my_set:
        sum_set += i

    return sum_set
