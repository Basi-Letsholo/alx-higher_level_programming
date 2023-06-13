#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list

#    new_list = []
    list_len = len(my_list)

    if idx >= list_len:
        return my_list
    else:
#        for i in range(0, idx):
#            new_list.append(my_list[i])
#        for j in range(idx, list_len - 1):
#            my_list[j] = my_list[j+1]
#    my_list = my_list[:-1]
        my_list = my_list[0: idx] + my_list[idx + 1: list_len]

    return my_list
