#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_number = len(sys.argv) - 1
    if arg_number == 0:
        print('0')
    if arg_number == 1:
        print("{}".format(int(sys.argv[1])))
    if arg_number > 1:
        sum = 0
        for i in range(1, arg_number + 1):
            sum = sum + int(sys.argv[i])
        print("{}".format(sum))
