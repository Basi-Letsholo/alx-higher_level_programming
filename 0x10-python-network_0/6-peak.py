#!/usr/bin/python3
""" Finds the Peak of a list of integers."""


def find_peak(list_of_integers):
    """Peak Function."""

    if list_of_integers is None or len(list_of_integers) < 1:
        return None

    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    length = len(list_of_integers)
    peak = None

    for i in range(1, length - 1):
        if (list_of_integers[i - 1] <= list_of_integers[i]) and (
                list_of_integers[i + 1] <= list_of_integers[i]):
            peak = list_of_integers[i]
        elif list_of_integers[1] < list_of_integers[0] and peak is None:
            peak = list_of_integers[0]
        elif list_of_integers[length - 1] > list_of_integers[length - 2] and (
                peak is None):
            peak = list_of_integers[length - 1]

    return peak
