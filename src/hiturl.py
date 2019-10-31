import requests
import sys


url = sys.argv[1]

resp = requests.get(url)
print(resp.status_code)
print(resp.headers)
print(resp.content)


