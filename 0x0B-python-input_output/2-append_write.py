#!/usr/bin/python3
"""This module contains function  that appends a string at the end of a text
    file (UTF8) and returns the number of characters written"""


def append_write(filename="", text=""):
    """
    Appends a string at the end ofa text file (UTF8) and returns the number of
        characters written

    Args:
        filename(str): The name of file to create or append
        text(str): The text to input to the created or appending file

    Returns:
        Number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        char_written = myfile.write(text)
    return char_written
