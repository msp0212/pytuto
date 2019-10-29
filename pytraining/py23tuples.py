"""
tuple aka read only list
immutable object
"""

items = (2.2, 1.2, .98, 3, 2.4, 5, 'alpha', 'beta', 'charlie')
# items[3] = 333 not allowed since tuple is read only
print(items)
print(type(items))
print(len(items))
print()

# indexing
print(items[-4])
print()

# slicing
print(items[-4:])
print()

for item in items[-4:]:
    print(item)
print()

# another way to initialize a tuple
name = 'pam', 'john', 'mary', 'tom'
print(name)
print(type(name))
print()

n = (1000)
print(n)
print(type(n))
print()

# defining a single element tuple
n = (1000, )
print(n)
print(type(n))
print()
