#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '' or sentence[0] == '':
        return None
    else:
        return (len(sentence), sentence[0])
