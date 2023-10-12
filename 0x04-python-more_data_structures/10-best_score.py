#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        score = None
        key = None
        
        for k, v in a_dictionary.items():
            if score is None or a_dictionary[k] > score:
                score = a_dictionary[k]
                key = k
        return key
