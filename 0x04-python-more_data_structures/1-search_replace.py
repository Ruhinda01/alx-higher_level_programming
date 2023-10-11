#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return None

    new_list = list(my_list)

    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
