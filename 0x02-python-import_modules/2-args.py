#!/usr/bin/python3

from sys import argv

argv_len = len(argv)

if __name__ == '__main__':
    if argv_len == 1:
        print(("{:d} arguments.").format(0))
    elif argv_len > 1:
        if argv_len == 2:
            print(("{:d} argument:").format(1))
        elif argv_len > 2:
            print(("{:d} arguments:").format(argv_len - 1))

        for i in range(1, argv_len):
            print(("{:d}: {}").format(i, argv[i]))
