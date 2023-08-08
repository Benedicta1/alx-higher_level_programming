#!/usr/bin/python3

def magic_string():
    # function that returns string BestSchool
    if hasattr(magic_string, 'BestSchool'):
        magic_string.BestSchool += 1
    else:
        magic_string.BestSchool = 1

    return ', '.join(['BestSchool'] * magic_string.BestSchool)
