#!/usr/bin/python3
def simple_delete(a_dictionary, Key=""):
    if a_dictionary.get(Key):
        a_dictionary.pop(Key)
    else:
        return a_dictionary
    return a_dictionary


"""Write a function that deletes a key in a dictionary.

Prototype: def simple_delete(a_dictionary, key=""):
key argument will be always a string
If a key doesn’t exist, the dictionary won’t change
You are not allowed to import any module"""
