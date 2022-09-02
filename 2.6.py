"""
2.6. Searching and Replacing Case-Insensitive Text

Problem
You need to search for and possibly replace text in a case-insensitive manner.

Solution
To perform case-insensitive text operations, you need to use the re module and supply
the re.IGNORECASE flag to various operations. For example:
"""
import re
text = 'UPPER PYTHON, lower python, Mixed Python'

text2 = re.findall("python", text, flags=re.IGNORECASE)

print(text2)

text3 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(text3)

"""
The last example reveals a limitation that replacing text won’t match the case of the
matched text. If you need to fix this, you might have to use a support function, as in the
following:
"""

def matchcase(word):
    def replace(m):
        pass

