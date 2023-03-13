#!/usr/bin/python3

"""Program returns a tuple with the length of a string
and its first character"""


def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (0, None)
        return result
    else:
        result_2 = (length, sentence[0:1])
        return result_2
