#!/usr/bin/python3
def safe_print_integer(value):
    try:
        result = isinstance(value, int)
        print("{:d}".format(value))
        return result
    except Exception as ex:
        return False
    except:
        return False
