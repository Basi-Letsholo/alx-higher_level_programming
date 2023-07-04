#!/usr/bin/python3
"""" Text Indentation Module. """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    new_text = ''
    i = 0
    while i < len(text) - 1:
        if text[i] == '.' and i + 1 < len(text) - 1:
            new_text += text[i]
            new_text += '\n\n'
            if text[i + 1] == ' ':
                i += 1
        elif text[i] == ':' and i + 1 < len(text) - 1:
            new_text += text[i]
            new_text += '\n\n'
            if text[i + 1] == ' ':
                i += 1
        elif text[i] == '?' and i + 1 < len(text) - 1:
            new_text += text[i]
            new_text += '\n\n'
            if text[i + 1] == ' ':
                i += 1

        else:
            new_text += text[i]

        i += 1
    new_text += text[len(text) - 1]

    print(new_text, end='')
