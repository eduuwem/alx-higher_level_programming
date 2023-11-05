#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        modified_list = []
        for k in range(len(my_list)):
            if k != idx:
                modified_list.append(my_list[k])
        my_list = modified_list
    return my_list
