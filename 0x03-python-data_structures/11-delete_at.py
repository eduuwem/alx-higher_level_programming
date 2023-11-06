#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        modified_list = my_list[:idx] + my_list[idx + 1:]
        my_list = modified_list
    return my_list
