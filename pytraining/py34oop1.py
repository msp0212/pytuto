"""demo for class and object"""

import sys
import math

class SystemInformation:
    pass  # define a dummy code block


si = SystemInformation()
print(si)
print()
print(SystemInformation)
print()

print(__name__)  # gives the default namespace for the python script
print(sys.__name__)  # get the namespace for the python module
print(math.__name__)
print()
