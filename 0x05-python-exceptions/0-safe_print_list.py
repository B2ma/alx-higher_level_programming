#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for item in my_list:
            if i < x:
                print(item, end='')
                i += 1
            else:
                break
    except:
        pass
    finally:
        print()
    return i
