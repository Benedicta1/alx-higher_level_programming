!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    rec_set_1 = {a for a in set_1 if a not in set_2}
    rec_set_2 = {a for a in set_2 if a not in set_1}
    return rec_set_1 | rec_set_2
