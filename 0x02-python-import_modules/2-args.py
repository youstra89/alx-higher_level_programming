#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_number = len(sys.argv) - 1
    if arg_number == 0:
        print("{} arguments.".format(arg_number))
    elif arg_number == 1:
        print("{} argument:".format(arg_number))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(arg_number))
        for i in range(1, arg_number + 1):
            print("{}: {}".format(i, sys.argv[i]))
        
