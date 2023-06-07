#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    if (i % 2) == 0:
        x = i
    elif (i % 2) != 0:
        x = i - ord('a') + ord('A')
    print(("{}").format(chr(x)), end='')
