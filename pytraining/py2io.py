"""demo program for python input/output"""

name = city = zip_code = 0

try:
    name = input('enter the name: ')
    city = input('enter the city: ')
    zip_code = int(input('enter the postal code: '))
except ValueError as error:
    print(error)

print('name: ', name)
print('city: ', city)
print('zip-code: ', zip_code)
print(type(zip_code))
