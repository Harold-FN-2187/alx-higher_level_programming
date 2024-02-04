#!/usr/bin/python3

def no_c(my_string):

    new_str = my_string[:]

    i = 0

    for k in range(len(my_string)):
        if (my_string[k] == 'c' or my_string[k] == 'C'):
            new_str = my_string[:(k-i)] + my_string[(k+1):]
            i += 0
    return (new_str)
