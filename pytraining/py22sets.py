a = [1, 2, 3, 4, 5]
b = [1, 3, 5, 7, 9]

x = set(a)
y = set(b)

print(x & y)  # intersection
print(x.intersection(y))  # intersection
print(x | y)  # union
print(x.union(y))  # union
print(x - y)  # difference
print(x.difference(y))  # difference
print(y - x)  # difference

items = set()
print(items)
print(type(items))
print(len(items))

items = {2.2, 1, 'kim', 2, 3, 4, 5, 'pat'}
print(items)
print()

# add to set
items.add('citrix')
items.add('dell')
items.add(3.14)
print(items)
print()

# remove from set
items.remove('kim')
items.remove(5)
print(items)
print()

for item in items:
    print(item, end=' ')
