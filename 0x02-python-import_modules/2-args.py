#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
args_num = len(arguments)
print("{} argument{}".format(args_num, 's.' if args_num == 0 else ':' if
			                         args_num ==1  else 's:'))
for i,arg in enumerate(arguments, start=1):
    print("{}: {}".format(i, arg))
