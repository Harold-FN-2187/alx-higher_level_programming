#!/usr/bin/python3

# Function that replaces an element in a list
# in a specific position without modifying the
# original list

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > range(len(my_list) - 1):
        return my_list
# create copy of list
# to avoid changing the original
    cpy = [x for x in my_list]
    cpy[idx] = element
    return (cpy)
