print(range(10))
print(type(range(10)))
print()

for item in range(10):
    print(item, end='|')
print()

for item in range(1, 10, 2):  # start, stop, increment
    print(item, end='|')
print()

items = [hex(item) for item in range(1, 11)]  # list comprehension
print(items)
print()

items = [item**2 for item in range(1, 11)]  # list comprehension
print(items)
print()

items = [item for item in range(1, 11)]  # list comprehension
print(items)
print()

items = [item for item in range(1, 11) if item % 2]  # compound list comprehension
print(items)
print()

items = {item: hex(item) for item in range(1, 11)}  # dict comprehension
print(items)
print()

items = {hex(item) for item in range(1, 11)}  # set comprehension
print(items)
print()
