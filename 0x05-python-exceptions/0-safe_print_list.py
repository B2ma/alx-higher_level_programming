#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for item in my_list:
            if i < x:
                print(item, end='')
                i += 1
    except TypeError as e:
        pass
    except IndexError:
        pass
    finally:
        print()
    return i
