#!/usr/bin/python3
def islower(c):
    response = None
    if c != '':
        if c.islower():
            response = True
        else:
            response = False
    return response