"""
Problem
You want to match text using the same wildcard patterns as are commonly used when
working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).

Solution
The fnmatch module provides two functions—fnmatch() and fnmatchcase()—that
can be used to perform such matching. The usage is simple:

"""
from fnmatch import fnmatch, fnmatchcase
import re
print(re.match("foo.txt", "*.txt"))
print(fnmatch("foo.txt", "*.txt"))
print(fnmatch("Dat.csv", "Dat[0-9]*"))

#TODO: did not understand this recipe at all 
