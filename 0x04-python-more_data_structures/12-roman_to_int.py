#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    integer_sum = 0
    converter = dict(I=1, IV=4, IX=9, XLIX=49, XCIX=99, CDXCIX=499, CMXCIX=999)
    for current, next in zip(roman_string, roman_string[1:]):
        if converter[current] >= converter[next]:
            integer_sum += converter[current]
        else:
            integer_sum -= converter[current]
    integer_sum += converter[roman_string[-1]]
    return integer_sum
