info = {
    'host': 'ws1',
    'domain': 'ws.com',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

print(info)
print(type(info))
print(len(info))
print()

# add
key = 'arch'
info[key] = 'x86_64'
print(info)
print()

# delete
info.pop('arch')
print(info)
print()

# update
key = 'version'
if key in info:  # validate if the key exists
    info[key] = 2.3
print(info)
print()

# lookup
val = info['domain']
print(val)
print(type(val))
print()

val = info['version']
print(val)
print(type(val))
print()

# iterate
for key in info:
    val = info[key]
    print(f'{key}: {val}')
print()

for key, value in info.items():
    print(f'{key} -> {val}')
print()

print(info.keys())
print(info.values())
print(info.items())

