class SystemInformation:
    def __init__(self):
        print(self, "I am in constructor")

    def __del__(self):
        print(self, "I am in destructor")


si = SystemInformation()
print(si)
