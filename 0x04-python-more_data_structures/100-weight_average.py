#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    values, weights = zip(*my_list)
    number = sum(map(lambda n, m: n * m, values, weights))
    denominator = sum(weights)

    return (number/denominator)
