#!/usr/bin/python3

# Needs to return OG my_list too!!

def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0:
        return new_list

    elif idx >= 0:
        len_list = len(new_list)

        if idx >= len_list:
            return new_list

        elif idx < len_list:
            new_list[idx] = element
            return new_list
