# https://docs.python.org/3/library

import os  # standart module import qilish.
import os as operating_system  # module import ni nomlash
from os import getcwd  # module dagi function import qilish

import libs.libs_module as lib  # Personal module import qilish

print(os)  # Ex: <module 'os' from 'C:\\Python39\\lib\\os.py'>
print(operating_system)  # Ex: <module 'os' from 'C:\\Python39\\lib\\os.py'>
print(getcwd())  # Ex: D:\GitHub\Python


print(lib.get_count("hello", 'l'))  # Ex: Personal module function = 2
print(lib.get_length("hello"))  # Ex: Personal module function = 5
