#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = None
    max_val = 0
    if a_dictionary == None:
        return a_dictionary
    for key in a_dictionary:
        if a_dictionary[key] > max_val:
            max_key = key
            max_val = a_dictionary[key]
    return max_key


"""Write a function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):
You can assume that all values are only integers
If no score found, return None
You can assume all students have a different score
You are not allowed to import any module"""
