#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    rec_set = set(my_list)
    for number in rec_set:
        sum += number
    return sum
