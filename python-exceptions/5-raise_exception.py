#!/usr/bin/python3
def raise_exception():
    wrong = ""
    if not type(wrong) is int:
        raise TypeError("Only integers are allowed")
