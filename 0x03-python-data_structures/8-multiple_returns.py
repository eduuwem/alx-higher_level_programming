#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        str_length, first_char = len(sentence), sentence[0]
    else:
        str_length, first_char = 0, "None"
    return str_length, first_char
