#!/usr/bin/python3

"""Program converts roman numerals to integers"""


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
    }

    decimals = [roman_dict[x] for x in roman_string]
    output = 0
    for i in range(len(decimals)):
        output += decimals[i]
        if decimals[i - 1] < decimals[i] and i != 0:
            output -= (decimals[i - 1] + decimals[i - 1])
    return output
