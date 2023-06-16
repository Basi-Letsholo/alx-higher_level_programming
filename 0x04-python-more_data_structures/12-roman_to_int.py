#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0

    list_str = list(roman_string)

    sum = 0
    _len = len(list_str)
    for i in range(0, _len):
        if list_str[i] == 'I':
            if _len - i > 1:
                if list_str[i + 1] == 'V':
                    sum += -1
                elif list_str[i + 1] == 'X':
                    sum += -1
                else:
                    sum += 1
            else:
                sum += 1
        elif list_str[i] == 'V':
            sum += 5
        elif list_str[i] == 'X':
            if _len - i > 1:
                if list_str[i + 1] == 'C':
                    sum += -10
                else:
                    sum += 10
            else:
                sum += 10
        elif list_str[i] == 'L':
            sum += 50
        elif list_str[i] == 'C':
            if _len - i > 1:
                if list_str[i + 1] == 'D':
                    sum += -100
                    continue
                if list_str[i + 1] == 'M':
                    sum += -100
                else:
                    sum += 100
            else:
                sum += 100
        elif list_str[i] == 'D':
            sum += 500
        elif list_str[i] == 'M':
            sum += 1000

    return sum
