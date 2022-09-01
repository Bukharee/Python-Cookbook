"""
Problem
You need to check the start or end of a string for specific text patterns, such as filename
extensions, URL schemes, and so on.

Solution
A simple way to check the beginning or end of a string is to use the str.starts
with() or str.endswith() methods. For example:
"""

import os
from urllib.request import urlopen
import re


filename = "spam.txt"
print(filename.endswith(".txt"))  # True
print(filename.startswith("file:"))  # False

url = 'http://www.python.org'
print(url.startswith('http:'))  # True

"""
If you need to check against multiple choices, simply provide a tuple of possibilities to
startswith() or endswith():
"""

filenames = os.listdir('.')  # list of all directories
python_and_html = [name for name in filenames if name.endswith(
    (".py", ".html"))]  # filter only files that endswith .py and .html
print(python_and_html)

# heres another exmple


def read_data(name):
    if name.startswith(("http:", "https:", "ftp: ")):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


print(read_data("StringsandText/2.1.py"))

# NOTE:
"""
Oddly, this is one part of Python where a tuple is actually required as input. If you happen
to have the choices specified in a list or set, just make sure you convert them using
tuple() first. For example:
"""
choices = ['http:', 'ftp:']
print(url.startswith(tuple(choices)))

"""
NOTE: You might also be inclined to use regular expressions as an alternative. For example:
"""
print(bool(re.match('http:|https:|ftp:', url)))

""" ast, but not least, the startswith() and endswith() methods look nice when com‐
bined with other operations, such as common data reductions. For example: """

if any(file for file in os.listdir('.') if file.endswith(('.py', '.html'))):
    print("there is a python or html file here")

