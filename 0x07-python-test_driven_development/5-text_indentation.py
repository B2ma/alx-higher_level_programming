#!/usr/bin/python3
"""This module contains a function text_indentation that prints a text with 2
    new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these
        characters: ., ? and :

    Agrs:
        test(str): test must be a sting otherwise a TypeError exception wth
            the message text must be a string will be raised
    Raises:
        TypeError: Raised when text is not string.
    """
    the_characters = {'.', '?', ':'}
    output = ""
    prevChar = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1
    while char< len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
