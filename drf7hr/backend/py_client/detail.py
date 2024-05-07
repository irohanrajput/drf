import requests

pk = 1
endpoint = f"http://localhost:8000/api/products/{pk}/"

gettt = requests.get(endpoint, params={"pk": pk})

print(gettt.json())