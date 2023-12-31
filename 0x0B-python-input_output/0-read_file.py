#!/usr/bin/python3
"""This module has a function that reads a text file (UTF8) and
    prints it to stdout"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
        filename(str): the name of the file
    """
    with open(filename, mode="r", encoding="utf-8") as myfile:
        for line in myfile:
            print(line, end='')
