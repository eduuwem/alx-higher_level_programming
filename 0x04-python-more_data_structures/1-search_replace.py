#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for k in range(len(new_list)):
        if new_list[k] == search:
            new_list[k] = replace
    return new_list
