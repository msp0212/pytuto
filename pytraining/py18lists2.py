items = []

print(items)
print(type(items))
print(len(items))

items = [2.2, 'pam', 'delhi', 11.77, 'mumbai', 'pam', 'pam', .98, 1., 2, 3]
print(items)
print(type(items))
print(len(items))

# update a list item
items[-2] = 'ii'
print(items)
print()

# append an item to a list
items.append('citrix')

# insert an item in a list
items.insert(2, 'bengaluru')
items.insert(0, 'shimla')
print(items)
print()

# pop the last element from a list
value = items.pop()
print(value)
print(items)

# pop an element from a specific index from a list
value = items.pop(-3)
print(value)
print(items)
print()

# delete by value from a list
item = 'pam'
items.remove(item)  # deletes only first occurrence
print(items)
print()

# delete all occurrences of an item
item = 'pam'
while item in items:
    items.remove(item)

print(items)
print()

# remove all float types from the list
for item in items:
    if type(item) is float:
        items.remove(item)

print(items)
print()

# list concatenation
print(items + items)
print()
# list duplication
print(items * 3)
print()

# removing duplicates from a list
duplicates = [2, 3, 4, 2, 3, 4]
print(set(duplicates))
unique = list(set(duplicates))  # order is not preserved
print(unique)
print()

# sorting a list
duplicates = [2.2, 3.2, 0.98, 1.0, 2, 3, 2.2, 3.2, 0.98, 1.0, 2, 3, 2.2, 3.2, 0.98, 1.0, 2, 3]
duplicates.sort()  # inplace sorting
print(duplicates)
print()

duplicates.sort(reverse=True)
print(duplicates)
print()

# reverse a list
duplicates = [2.2, 3.2, 0.98, 1.0, 2, 3, 2.2, 3.2, 0.98, 1.0, 2, 3, 2.2, 3.2, 0.98, 1.0, 2, 3]
duplicates.reverse()
print(duplicates)
print()
