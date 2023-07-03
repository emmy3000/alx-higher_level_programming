#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Finds the peak in a list of integers."""
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)
    lst = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return lst[mid]
    elif mid - 1 < 0:
        return lst[mid] if lst[mid] > lst[mid + 1] else lst[mid + 1]
    elif mid + 1 >= length:
        return lst[mid] if lst[mid] > lst[mid - 1] else lst[mid - 1]

    if lst[mid - 1] < lst[mid] > lst[mid + 1]:
        return lst[mid]

    if lst[mid + 1] > lst[mid - 1]:
        return find_peak(lst[mid:])
    return find_peak(lst[:mid])
