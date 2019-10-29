"""
access specifier
"""


class PackageManager:
    def __init__(self, name, version):
        self.__name = name  # private attribute
        self.version = version

    def __get_information(self):
        print(f'name: {self.__name}')
        print(f'version: {self.version}')

    def wrapper(self):
        self.__get_information()

pm = PackageManager('pip', '3.7.5')
# pm.__get_information()
pm.wrapper()
# print(pm.__name) cannot be accessed outside class since it is a private attribute
print()
