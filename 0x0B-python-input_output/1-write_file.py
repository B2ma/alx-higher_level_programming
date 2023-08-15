#!/usr/bin/python3
"""This module contains function  that writes a string to a text file (UTF8)
    and returns the number of characters written"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of
        characters written

    Args:
        filename(str): The name of file to create
        text(str): The text to input to the created file

    Returns:
        Number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        char_written = myfile.write(text)
    return char_written
