#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        iterator = iter(my_list)
        while count < x:
            item = next(iterator)
            print(item, end='')
            count += 1
    except StopIteration:
        pass
    except TypeError as e:
        pass
    except IndexError:
        pass
    finally:
        print()
    return count
