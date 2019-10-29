"""
pypi.org (repository of python modules)

On windows, use below command to install paramiko module
python -m pip install paramiko

"""

import paramiko

class CustomSSHClient:
    def __init__(self, user, passwd, host, port=22):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, self.passwd)
        print(f'Connected to {host} !')

    def run_cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        output = stdout.read()
        payload = output if output else stderr.read()
        return payload.decode()  # bytes into str

    def __del__(self):
        self.ssh.close()

if __name__ == '__main__':
    host = input('Enter host IP: ')
    user = input('Enter username: ')
    passwd = input('Enter passwd: ')

    sshc = CustomSSHClient(user, passwd, host)
    cmd = input(f'{host}:{user}>')
    while cmd != 'exit':
        op = sshc.run_cmd(cmd)
        print(op)
        cmd = input(f'{host}:{user}>')
    print()
