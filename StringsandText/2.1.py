from posixpath import join
import re #regular expression module

line = 'asdf fjdk; afed, fjek,asdf, foo'

words = re.split(r'[;,\s]s*', line) #get the words without the split characters
print(words)


#capture groups are | enclosed in () if they are used it will capture the delimers also

words_with_delimer = re.split(r'(;|,|\s)\s*', line)
print(words_with_delimer)

values = words_with_delimer[::2]
delimiter = words_with_delimer[1::2]
print(values)
print(delimiter)

joined = ''.join(v+d for v,d in zip(values, delimiter))
print(joined)
