#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list
    Args:
        my_list(list): the list to print elements
        x: Number of elements of my_list to print.
    Returns:
        the number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            count += 1
        except IndexError:
            break
    print("")
    return count
