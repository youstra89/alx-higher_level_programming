#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        item = 0
        key = None
        for i in a_dictionary:
            if a_dictionary[i] > item:
                item = a_dictionary[i]
                key = i
        return key
