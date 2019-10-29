"""
cat /etc/passwd | head | nl
"""


import  subprocess

cat = subprocess.Popen(['cat', '/etc/passwd'], stdout=subprocess.PIPE)
head = subprocess.Popen(['head'], stdin=cat.stdout, stdout=subprocess.PIPE)
nl = subprocess.Popen(['nl'], stdin=head.stdout, stdout=subprocess.PIPE)

for item in nl.communicate():
    if item:
        print(item.decode())