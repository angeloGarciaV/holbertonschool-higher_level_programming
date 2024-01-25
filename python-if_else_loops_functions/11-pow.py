#!/usr/bin/python3
def pow(a, b):
    j = 1
    if b < 0:
        b = abs(b)
        c = 1/a
        for i in range(b):
            j *= c
        return round(j, 2)
    else:
        for i in range(b):
            j *= a
    return j
