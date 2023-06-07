#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            x = ord(c) - ord('a') + ord('A')
        elif ord(c) < 97 or ord(c) > 122:
            x = ord(c)
        print(chr(x), end='')
    print('')
