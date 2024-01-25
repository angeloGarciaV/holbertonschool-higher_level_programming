#!/usr/bin/python3
def remove_char_at(str, n):
    strlen = len(str)
    if n < 0 or n > strlen:
        return str
    newstr = ''
    for i in range(strlen):
        if i == n:
            continue
        newstr += str[i]
    return newstr
