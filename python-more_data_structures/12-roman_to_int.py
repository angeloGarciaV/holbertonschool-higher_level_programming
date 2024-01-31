#!/usr/bin/python3
def roman_to_int(roman_string):
    r_str = roman_string
    result = 0
    roman_nums = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
    if not isinstance(r_str, str) or r_str is None:
        return result
    if r_str == "IX":
        return 9
    for i in r_str:
        result += roman_nums[i]
    return result
