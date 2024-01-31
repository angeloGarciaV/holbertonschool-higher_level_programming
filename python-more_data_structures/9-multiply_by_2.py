#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for key in a_dictionary:
        b_dictionary.update({key: a_dictionary[key]*2})

    return b_dictionary


"""Write a function that returns a new dictionary with all values multiplied by 2

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are only integers
Returns a new dictionary
You are not allowed to import any module"""
