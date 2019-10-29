import re

s = 'the python and perl scripting'
pattern = 'P.+N'  # greedy match

# case sensitive match
m = re.search(pattern, s)
print(m)
print(type(m))
if m:
    print(m)
    print(type(m))
else:
    print('match failed !')
print()

# case insensitive match
m = re.search(pattern, s, re.I)
if m:
    print(m)
    print(type(m))
else:
    print('match failed !')
print()

pattern = 'P.+?N'  # non-greedy match
m = re.search(pattern, s, re.I)
if m:
    print(m)
    print(type(m))
else:
    print('match failed !')
print()

pattern = 'P.+?N'  # non-greedy match
m = re.search(pattern, s, re.I)
if m:
    print(f'matched string is: {m.group()}')
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print('match failed !')
print()

# multiple matches
for m in re.finditer(pattern, s, re.I):
    print(m.group())
    print(m.span())
print()
