#!/usr/bin/python3
def magic_string():
    setattr(magic_string, 'i', getattr(magic_string, 'i', 0) + 1)
    return ', '.join(['BestSchool'] * getattr(magic_string, 'i'))
