#!/usr/bin/python3
def uniq_add(my_list=[]):
    lst = set(my_list)
    sum = 0
    for i in lst:
        sum += i
    return sum
