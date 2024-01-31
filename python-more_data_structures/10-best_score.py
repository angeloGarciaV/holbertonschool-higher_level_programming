#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = None
    max_val = 0
    if a_dictionary is None:
        return a_dictionary
    for key in a_dictionary:
        if a_dictionary[key] > max_val:
            max_key = key
            max_val = a_dictionary[key]
    return max_key
