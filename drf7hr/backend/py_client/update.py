import requests
pk = 4
endpoint = f"http://localhost:8000/api/products/{pk}/update"

data = {
    "title": "Updated title",
    "content": "Updated content",
    "price": 75,
}

r = requests.put(endpoint, data=data)