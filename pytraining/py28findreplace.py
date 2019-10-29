import re

s = 'root:x:0:0:root:/root:/bin/bash'
print(s)
patt = ':'
repl = ','

s2 = re.sub(patt, repl, s)
print(s2)
print()

s3 = re.sub('[AEIOU]', '*', s2, flags=re.I)
print(s3)
print()
s3 = re.sub('[AEIOU]', '*$', s2, flags=re.I)
print(s3)
print()
s3 = re.sub('oo', '$*$', s2, flags=re.I)
print(s3)
print()

# replace fist N matches
s3 = re.sub('[AEIOU]', '*', s2, flags=re.I, count=3)
print(s3)
print()
