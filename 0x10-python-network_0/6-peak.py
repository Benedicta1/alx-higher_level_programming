#!/usr/bin/python3
'''
function that finds a peak
'''


def find_peak(listint):
    ''' Function that returns peak value in a list '''
    if listint:
        b = listint[0]
        for a in listint:
            if a > b:
                b = a
        return b
    else:
        return None
