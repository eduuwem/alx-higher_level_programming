#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return "None"
    return max([x for x in my_list])
