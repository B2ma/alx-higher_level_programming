#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set1 = set_1.difference(set_2)
    diff_set2 = set_2.difference(set_1)
    output = diff_set1.union(diff_set2)
    return list(output)
