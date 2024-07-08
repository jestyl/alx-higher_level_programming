#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Find a peak element using binary search """
    def find_peak_util(low, high):
        mid = (low + high) // 2

        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]

        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return find_peak_util(low, mid - 1)

        else:
            return find_peak_util(mid + 1, high)

     return find_peak_util(0, len(list_of_integers) - 1)
