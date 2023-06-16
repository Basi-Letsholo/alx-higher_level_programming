# 'snippet' of code from first draft


    list_str = list(roman_string)
    print(list_str)
#    for c in roman_string:
#        list_str.append(c)

    sum = 0
    for i in range(len(list_str)):
        if list_str[i] == 'I' and list_str[i + 1] == 'V':
            sum += -1
        elif list_str[i] == 'I' and list_str[i + 1] == 'X':
            sum += -1
        elif list_str[i] == 'X' and list_str[i + 1] == 'C':
            sum += -10
        elif list_str[i] == 'C' and list_str[i + 1] == 'D':
            sum += -100
        elif list_str[i] == 'C' and list_str[i + 1] == 'M':
            sum += -100
        else:
            if list_str[i] == 'I':
                sum += 1
            elif list_str[i] == 'V':
                sum += 5
            elif list_str[i] == 'X':
                sum += 10
            elif list_str[i] == 'L':
                sum += 50
            elif list_str[i] == 'C':
                sum += 100
            elif list_str[i] == 'D':
                sum += 500
            elif list_str[i] == 'M':
                sum += 1000

    return sum
