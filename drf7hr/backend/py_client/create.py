import requests

endpoint = "http://localhost:8000/api/products/create/"

data = {
    "title": "anythin",
    "content": "wearable item",
    "price": 1000.00
}

create_object = requests.post(endpoint, json=data)


print(create_object.json())