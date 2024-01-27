#!/usr/bin/python3
def max_integer(my_list=[]):
    x = my_list[0]
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > x:
            x = i
    return x


"""Write a function that finds the biggest integer of a list.

Prototype: def max_integer(my_list=[]):
If the list is empty, return None
You can assume that the list only contains integers
You are not allowed to import any module
You are not allowed to use the builtin max()"""
