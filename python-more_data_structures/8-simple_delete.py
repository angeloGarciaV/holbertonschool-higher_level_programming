#!/usr/bin/python3
def simple_delete(a_dictionary, Key=""):
    if a_dictionary.get(Key):
        a_dictionary.pop(Key)
    else:
        return a_dictionary
    return a_dictionary
