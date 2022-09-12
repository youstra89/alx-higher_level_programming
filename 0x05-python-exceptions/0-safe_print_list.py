#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = ''
        last = None
        for i in my_list[0:x]:
            num = num + str(i)
            last = i - 1
            # num += "%s" % i
        print(f"{num}")
        return my_list[last]
    except Exception as ex:
        print(ex)
