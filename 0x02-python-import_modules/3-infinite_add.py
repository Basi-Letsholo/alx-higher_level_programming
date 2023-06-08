#!/usr/bin/python3

from sys import argv

len_argv = len(argv)

if __name__ == '__main__':
    if len_argv == 1:
        print(("{}").format(0))
    elif len_argv > 1:
        sum = 0
        for i in range(1, len_argv):
            sum += int(argv[i])
        print(("{:d}").format(sum))
