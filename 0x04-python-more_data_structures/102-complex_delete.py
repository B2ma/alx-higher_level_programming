#!/usr/python3
def complex_delete(a_dictionary, value):
    dict_copy = a_dictionary.copy()
    for i in dict_copy:
        if dict_copy[i] == value:
            del a_dictionary[i]
    return a_dictionary
