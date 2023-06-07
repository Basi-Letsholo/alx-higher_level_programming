#!/usr/bin/python3

def uppercase(str):
   for c in str:
        if 97 <= ord(c) <= 122:
            print(("{}").format(chr(ord(c + 32))))
        elif ord(c) < 97 or ord(c) > 122:
            print(("{}").format(c))
