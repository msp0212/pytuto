import re

patt = ' +'

# extract 5 columns from this file's lines
for line in open(r'D:\Work\pytest2.txt'):
    print(re.split(patt, line))
    print(re.split(patt, line)[4])
print()

# list comprehension
sizes = [int(re.split(patt, line)[4]) for line in open(r'D:\Work\pytest2.txt')]
print(sizes)
print()
print(f'Max: {max(sizes)}')
print(f'Min: {min(sizes)}')
print(f'Sum: {sum(sizes)}')
print(f'Avg: {sum(sizes) / len(sizes)}')