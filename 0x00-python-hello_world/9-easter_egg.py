#!/usr/bin/python3
with open('zenfile.txt', 'r') as file:
    for line in file:
            print(line.rstrip())

