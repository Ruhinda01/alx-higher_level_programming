#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """
    MyList class
    Args:
        list
    Return:
        nothing
    """
    def print_sorted(self):
        """
        Prints a sorted list but sorted
        (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
