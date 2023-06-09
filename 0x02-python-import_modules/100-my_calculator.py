#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, div, mul

if __name__ == '__main__':
    len_argv = len(argv)

    if len_argv != 4:
        print(("{}").format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    elif len_argv == 4:
        a = int(argv[1])
        b = int(argv[3])

        if argv[2] == '+':
            print(("{:d} + {:d} = {:d}").format(a, b, add(a, b)))
            exit(0)
        elif argv[2] == '-':
            print(("{:d} - {:d} = {:d}").format(a, b, sub(a, b)))
            exit(0)
        elif argv[2] == '*':
            print(("{:d} * {:d} = {:d}").format(a, b, mul(a, b)))
            exit(0)
        elif argv[2] == '/':
            print(("{:d} / {:d} = {:d}").format(a, b, div(a, b)))
            exit(0)
        else:
            print(("{}").format("Unknown operator. Available operators: +, -, * and /"))
            exit(1)
