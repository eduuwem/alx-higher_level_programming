#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for b, number in tmp.items():
        if value == number:
            my_dict.pop(b)
    return my_dict
