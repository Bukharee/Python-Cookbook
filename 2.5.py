"""
2.5. Searching and Replacing Text

Problem
You want to search for and replace a text pattern in a string.

Solution
For simple literal patterns, use the str.replace() method. For example:
"""
import re
from calendar import month_abbr

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

"""
NOTE: For more complicated patterns, use the sub() functions/methods in the re module. To
illustrate, suppose you want to rewrite dates of the form “11/27/2012” as “2012-11-27.”
Here is a sample of how to do it:
"""
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# TODO: did not understand  this
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{4})', r'\3-\1-\2', text))
"""
TODO: did not understand this also
If you’re going to perform repeated substitutions of the same pattern, consider compil‐
ing it first for better performance. For example:"""
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)
'Today is 2012-11-27. PyCon starts 2013-3-13.'

"""
For more complicated substitutions, it’s possible to specify a substitution callback func‐
tion instead. For example:
"""
m = datepat.match('11/27/2012')


def change_date():
    month_nam = month_abbr[int(m.group(1))]


print(change_date())
