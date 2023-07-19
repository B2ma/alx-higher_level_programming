#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_elements = list(set(my_list))
    return sum(int(i) for i in uniq_elements)
