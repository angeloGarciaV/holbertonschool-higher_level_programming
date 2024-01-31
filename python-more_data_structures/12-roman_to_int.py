#!/usr/bin/python3
def roman_to_int(roman_string):
    s = roman_string
    result = 0
    roman_nums = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
    if not isinstance(s, str) or s is None:
        return result

    for i, num in enumerate(s):
        if i < len(s) - 1 and roman_nums[s[i]] < roman_nums[s[i + 1]]:
            result -= roman_nums[num]
        else:
            result += roman_nums[num]
    return result
