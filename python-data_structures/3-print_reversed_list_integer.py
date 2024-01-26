#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)-1, -1, -1):
        if isinstance(my_list[i], str):
            my_list[i] = ord(my_list[i])
        print("{:d}".format((my_list[i])))
