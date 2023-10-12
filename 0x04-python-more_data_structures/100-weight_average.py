#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        num1 = 0
        num2 = 0
        for c in my_list:
            num1 += c[0] * c[1]
            num2 += c[1]
        return ((num1) / (num2))
