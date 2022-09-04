#!/usr/bin/python3
def multiple_returns(sentence):
    first_character = None
    if len(sentence) > 0:
        first_character = sentence[:1]
    return len(sentence), first_character
