#!/usr/bin/python3

def islower(c):
    if 97 <= ord(c) <= 122:
        return True
    elif ord(c) < 97 or ord(c) > 122:
        return False
