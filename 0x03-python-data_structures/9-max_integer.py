#!/usr/bin/python3

def max_integer(my_list=[]):
    lent = len(my_list)
    if lent == 0:
        return (None)

    max = my_list[0]
    for i in range(len):
        if my_list[i] > max:
            max = my_list[i]

    return (max)
