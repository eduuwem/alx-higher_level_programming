#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    Maximum = 0
    for key, number in a_dictionary.items():
        if number > Maximum:
            Maximum = number
    for key, number in a_dictionary.items():
        if number == Maximum:
            return key
