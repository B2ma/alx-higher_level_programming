#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    args_num = len(arguments)
    if args_num == 0:
        print("0")
    elif args_num > 0:
        total_sum = sum(int(arg) for arg in arguments)
        print("{}".format(total_sum))
