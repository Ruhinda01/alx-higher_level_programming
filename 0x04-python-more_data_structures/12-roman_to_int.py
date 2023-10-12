#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        rom_dict = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
        }
        result = 0
        prev = 0
        for s in roman_string:
            value = rom_dict[s]
            if value > prev:
                result += value - (2 * prev)
            else:
                result += value
            prev = value
        return result
    else:
        return 0
