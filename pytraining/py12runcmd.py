import sys
import subprocess  # process management

if sys.platform in ['linux', 'darwin']:
    cmd = ['ifconfig']
elif sys.platform == 'win32':
    cmd = ['ipconfig']
else:
    raise OSError('Unsupported OS')

print(type(cmd))
print(cmd)
op = subprocess.check_output(cmd)
print(op)
print(op.decode())  # bytes into unicode
