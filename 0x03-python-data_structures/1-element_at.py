#!/usr/bin/python3
def element_at(my_list, idx=None):
    if idx is not None and 0 <= idx < len(my_list):
        return my_list[idx]
    return None
