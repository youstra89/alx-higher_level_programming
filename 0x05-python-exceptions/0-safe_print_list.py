#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = ''
        j = 0
        for i in my_list[0:x]:
            num = num + str(i)
            j += 1
            # num += "%s" % i
        print(f"{num}")
        return j
    except Exception:
        print("ex")
