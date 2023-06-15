#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    score_list = []
    for value in a_dictionary.values():
        score_list.append(value)

    best_score = 0
    for i in range(0, len(score_list)):
        if best_score < score_list[i]:
            best_score = score_list[i]

    best_score_key = ''
    for key, value in a_dictionary.items():
        if value == best_score:
            best_score_key = key

    return best_score_key
