#!/usr/bin/python3

def best_score(a_dictionary):
    if len(a_dictionary) == 0 or not isinstance(a_dictionary, dict):
        return None

    current_score = list(a_dictionary.keys())[0]
    best = a_dictionary(current_score)

    for ke_y, val in a_dictionary.items():
        if ke_y > best:
            best = val
            current_score = ke_y
        return (current_score)
