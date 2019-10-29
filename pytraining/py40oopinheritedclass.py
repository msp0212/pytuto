import py39oopbaseclass


class Employee(py39oopbaseclass.Person):
    def __init__(self, empid, first_name, last_name):
        self.empid = empid
        super().__init__(first_name, last_name)  # invoke overriden method

    def get_info(self):
        print(f'Employee Id: {self.empid}')
        super().get_info()


if __name__ == '__main__':
    e = Employee(1, 'guido', 'rossum')
    e.get_info()
