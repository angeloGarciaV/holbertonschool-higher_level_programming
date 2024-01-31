#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for key in a_dictionary:
        b_dictionary.update({key: a_dictionary[key]*2})

    return b_dictionary
