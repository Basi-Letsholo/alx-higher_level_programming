#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        ans = 1
    elif b > 0:
        ans = 1
        for i in range(0, b):
            ans = ans * a
    elif b < 0:
        ans = 1
        c = -b
        n = 1
        for i in range(0, c):
            n = n * a
        ans = 1 / n

    return ans
