"""
python -m pip install requests
"""
import requests

url = 'https://reqres.in/api/users?page=2'

resp = requests.get(url)
print(resp.status_code)
print()
print(resp.headers)
print()
print(resp.content)
print()
print(resp.json())
