#!/usr/bin/python3

def uppercase(str):
    for c in str: 
        if ord('a') <= ord(c) <= ord('z'):
            print(chr(ord(c) - ord('a') + ord('A')), end='')
        elif ord(c) < 97 or ord(c) > 122:
            print(c, end='')
    print('')
