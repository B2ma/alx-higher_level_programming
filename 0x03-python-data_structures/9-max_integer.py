#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_numb = my_list[0]
        for numb in my_list:
            if numb > max_numb:
                max_numb = numb
        return max_numb
