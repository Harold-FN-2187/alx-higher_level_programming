#!/usr/bin/python3

def roman_to_int(roman_string):
#Convert roman numeral to an integer
    rom_dict = {"I": 1, "V": 5, "X": 10,
                "L":50, "C":100, "D":500,
                "M":1000}