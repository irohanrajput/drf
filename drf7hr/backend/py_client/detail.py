import requests

pk = 1
endpoint = "http://localhost:8000/api/products/1/"

gettt = requests.get(endpoint)

print(gettt.json())