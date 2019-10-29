"""byte strings"""

s = 'peter'
print(s)
print(type(s))
print(s.encode())
print()

s = b'peter\x30\x31\x7f'
print(s)
print(type(s))
print(s.decode())
print()
