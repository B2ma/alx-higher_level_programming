#!/usr/python3
def complex_delete(a_dictionary, value):
    to_del_keys = []

    for key, val in a_dictionary.items():
        if val == value:
            to_del_keys.append(key)
    for key in to_del_keys:
        del a_dictionary[key]
    return a_dictionary
