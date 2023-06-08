#!/usr/bin/python3

import hidden_4

if __name__ == '__main__':
    names = dir(hidden_4)
    names_len = len(names)
    for i in range(0, names_len):
        if names[i][0] != '_':
            print(("{}").format(names[i]))
