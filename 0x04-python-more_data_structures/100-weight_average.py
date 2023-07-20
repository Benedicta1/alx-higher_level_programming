#!/usr/bin/python3
def weight_average(my_list=[]):
    point = 0
    sum_up = 0
    if my_list:
        tup = ()
        for tup in my_list:
            point += (tup[0] * tup[1])
            sum_up += tup[1]
        return point / sum_up
    return 0
