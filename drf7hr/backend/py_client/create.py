import requests
from custom_detail import getToken

endpoint = "http://localhost:8000/api/products/"

headers = getToken()


def getData(*args):
    title = input("enter the title: ")
    price = float(input("enter the price: "))
    content = input("about the product:")
    return {"title": title, "price": price, "content": content}


data_dict = getData()


data = {
    "title": data_dict["title"],
    "content": data_dict["content"],
    "price": data_dict["price"],
}


response = requests.post(endpoint, json=data, headers=headers)


print(response.json())
