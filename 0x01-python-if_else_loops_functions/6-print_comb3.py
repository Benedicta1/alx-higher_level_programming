#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.
The two digits must be different - 01 and 10 are considered identical."""
for fig1 in range(0, 10):
    for fig2 in range(fig1 + 1, 10):
        if fig1 == 8 and fig2 == 9:
            print("{}{}".format(fig1, fig2))
        else:
            print("{}{}".format(fig1, fig2), end=", ")
