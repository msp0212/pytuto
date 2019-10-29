s = 'root:x:0:0:root:/root:/bin/bash'
delim = ':'

items = s.split(delim)
print(items)
print()

print(s.split(delim)[0])  # indexing
print(s.split(delim)[1:])  # slicing
print()

for item in items:
    print(item, end="|")
print()

