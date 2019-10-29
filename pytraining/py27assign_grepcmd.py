import re

pattern = 'bash$'
for line in open(r'D:\Work\pythontest.txt'):
    if re.search(pattern, line, re.I):
        print(line, end='')