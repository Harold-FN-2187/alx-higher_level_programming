#!/usr/bin/python3

def multiple_returns(sentence):
    sen_length = len(sentence)

    if (sen_length == 0):
        n_tuple = (sen_length, None)
    else:
        n_tuple = (sen_length, sentence[0])

    return (n_tuple)
