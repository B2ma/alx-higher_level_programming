#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        i = iter(my_list)
        while count < x:
            item = next(i)
            print(item, end='')
            count += 1
    except StopIteration:
        pass
    except TypeError as e:
        print("Error: ", e)
    finally:
        print()
    return count
