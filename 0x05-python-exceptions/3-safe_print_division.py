#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res = a / b
    except (ZeroDivisionError, FloatingPointError):
        res = None
    finally:
        print("Inside result {}".format(res))
    return (res)
