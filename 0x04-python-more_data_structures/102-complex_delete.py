#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is not None:
        new_dict = dict(a_dictionary)
        for k, v in new_dict.items():
            if v == value:
                del a_dictionary[k]
        return a_dictionary
