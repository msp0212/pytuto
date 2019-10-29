"""
PackageManager

name
version

__init__()
get_information()
"""


class PackageManager:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def get_information(self):
        print(f'name: {self.name}')
        print(f'version: {self.version}')


pm = PackageManager('pip', '3.7.5')
pm.get_information()
print()
