#!/usr/bin/python3

def div(a, b):
    quotient = 0
    try:
        quotient = a / b
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    finally:
        return quotient


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(div(my_list_1[i], my_list_2[i]))
        except IndexError:
            print("out of range")
            new_list.append(0)

    return new_list
