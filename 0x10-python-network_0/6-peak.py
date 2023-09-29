#!/usr/bin/python3
""" Finds the Peak of a list of integers. """


def find_peak(list_of_integers):
    """Peak Function."""

    if list_of_integers is None or len(list_of_integers) < 1:
        return None

    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    peak = list_of_integers[0]
    for i in range(1, len(list_of_integers) - 1):
        if (list_of_integers[i - 1] <= list_of_integers[i]) and (
                list_of_integers[i + 1] < list_of_integers[i]):
            peak = list_of_integers[i]

    return peak
