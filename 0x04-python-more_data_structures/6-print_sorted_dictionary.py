#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)
    for i in keys:
        print(f"{i}: {a_dictionary[i]}")
