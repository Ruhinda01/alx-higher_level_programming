#!/usr/bin/python3

def padd(tuple_x):
    if len(tuple_x) == 0:
        return (0, 0)
    elif len(tuple_x) == 1:
        return (tuple_x[0], 0)
    else:
        return (tuple_x[0], tuple_x[1])



def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = padd(tuple_a)
    tuple_b = padd(tuple_b)
    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]

    final = (first, second)
    return final
