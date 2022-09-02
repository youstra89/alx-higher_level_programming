#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arg_number = len(sys.argv) - 1
    if arg_number != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("1")
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
            print("0")
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
            print("0")
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
            print("0")
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
            print("0")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            print("1")
