#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    lst = set(my_list)
    # lst = list(filter(lambda x: x if x not in lst else None, my_list))
    print(lst)
    return reduce(lambda x, y: x + y, lst)