#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]
    for k in range(2):
        result[k] = tuple_a[k] if k < len(tuple_a) else 0
        result[k] += tuple_b[k] if k < len(tuple_b) else 0
    return tuple(result)
