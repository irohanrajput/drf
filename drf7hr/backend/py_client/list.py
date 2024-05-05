import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "fan",
    "content": "home appliance",
    "price": 1100.00
}

response = requests.get(endpoint)
# response = requests.post(endpoint, json=data)

#now the same endpoint will handle both the requests


print(response.json())