#!/usr/bin/python3

def multiple_returns(sentence):
    len_sentence = len(sentence)
    if len_sentence == 0:
        return new_tuple(0, None)
    else:
        new_tuple = (len_sentence, sentence[0])
        return new_tuple
