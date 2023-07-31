#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    a = 0
    ben_list = []
    for a in range(list_length):
        try:
            b = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            b = 0
        except ZeroDivisionError:
            print("division by 0")
            b = 0
        except IndexError:
            print("out of range")
            b = 0
        finally:
            ben_list.append(b)
    return ben_list
