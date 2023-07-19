#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rec_list = []
    for a in my_list:
        if a == search:
            rec_list.append(replace)
        else:
            rec_list.append(a)
    return rec_list
