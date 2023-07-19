#!/usr/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary.values:
        return a_dictionary
    toDeleteKey = []
    for key, val in a_dictionary.items():
        if val == value:
            toDeleteKey.append(key)
    for key in toDeleteKey:
        del a_dictionary[key]
    return a_dictionary
