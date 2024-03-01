#!/usr/bin/python3
""""Peak finding algorithm"""


def find_peak(list_of_integers):
    """
    Finds a peak
    Args:
        list_of_integers (list): list of ints
    Return:
        peak (int)
    """
    list_len = len(list_of_integers)

    if list_of_integers == []:
        return None

    left = 0
    right = list_len - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
