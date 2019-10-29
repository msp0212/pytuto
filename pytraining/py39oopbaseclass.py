class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')


if __name__ == '__main__':
    p = Person('tom', 'larry')
    p.get_info()
    print(__name__)
