"""
Problem
You want to match or search text for a specific pattern.

Solution
If the text you’re trying to match is a simple literal, you can often just use the basic string
methods, such as str.find(), str.endswith(), str.startswith(), or similar. For
example:
"""
import re

text = 'yeah, but no, but yeah, but no, but yeah'

# exact match

print("yeah" == text)

# match at the start or end

print(text.startswith("yeah"))
print(text.endswith("yeah"))

# seach for the appearance of the first occurance

print(text.find("no"))
print(text.find("sam"))

"""
NOTE: For more complicated matching, use regular expressions and the re module. To illus‐
trate the basic mechanics of using regular expressions, suppose you want to match dates
specified as digits, such as “11/27/2012.” Here is a sample of how you would do it:
"""
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'


def did_match(text):
    if re.match(r'\d{2}/\d{2}/\d{4}', text):
        print("matched")
    else:
        print("not matched")


did_match(text1)
did_match(text2)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
date_pattern = re.compile(r'\d{1,2}/\d{1,2}/\d{4}')

print(date_pattern.findall(text))


"""
NOTE: Capture groups often simplify subsequent processing of the matched text because the
contents of each group can be extracted individually. For example:
"""
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
matched = datepat.match(text1)
print(matched.group(1))
print(matched.group(3))

# tuple unpacking can also be used with the groups() method  example

month, day, year = matched.groups()
print(month, day, year, sep="-")

#finding all matches 

print(datepat.findall(text))

for month, day, year in datepat.findall(text):
    print("{}-{}-{}".format(year, month, day))

"""NOTE: If you want an exact match, make sure the pattern includes the end-marker ($), as in
the following:
"""
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
m = datepat.match('11/27/2012abcdef')
print(m)
