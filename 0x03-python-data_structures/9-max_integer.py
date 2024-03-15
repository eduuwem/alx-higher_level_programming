#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return "None"
    max_val = my_list[0]
    k = 1
    while k < len(my_list):
        if my_list[k] > max_val:
            max_val = my_list[k]
        k += 1
    return max_val
