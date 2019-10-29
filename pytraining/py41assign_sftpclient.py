from py38assign_sshclient import CustomSSHClient


class SFTPClient(CustomSSHClient):
    def __init__(self, user, passwd, host, port=22):
        super().__init__(user, passwd, host, port)
        self.sftp = self.ssh.open_sftp()

    def upload(self, src, dst):
        self.sftp.put(src, dst)
        print(f'{src} upload to {dst}')

    def download(self, remote, local):
        self.sftp.get(remote, local)
        print(f'{remote} downloaded to {local}')

    def __del__(self):
        self.sftp.close()
        super().__del__()


if __name__ == '__main__':
    sftpc = SFTPClient('root', 'msp.321', '10.102.34.200')
    sftpc.upload('py41assign_sftpclient.py', '/root/work/python/sftp_client.py')
    sftpc.download('/root/work/python/sftp_client.py', '__sftp_client.py')
