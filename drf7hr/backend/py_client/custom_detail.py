import requests
from getpass import getpass

endpoint_token = "http://localhost:8000/api/auth"

username = "sastauser"
password = None


def getToken(username: str = None, password: str = None):
    if username is None:
        username = input("enter username: ")
    if password is None:
        password = getpass(f"enter password for {username}: ")
    credentials = {"username": username, "password": password}
    auth_response = requests.post(endpoint_token, data=credentials)

    if auth_response.status_code == 200:
        token = auth_response.json()["token"]
        headers = {"Authorization": f"Bearer {token}"}
        return headers


if __name__ == "__main__":

    headers = getToken(username, password)
    index = int(input("enter the object index: "))
    print("im running")
    endpoint_products = f"http://localhost:8000/api/products/"
    get_response = requests.get(endpoint_products, headers=headers)
    json_obj = get_response.json()[int(index)]
    print(
        f" the pk of requested objected is {index+1}. \n The title is: {json_obj['title']}. \n The price is: {json_obj['price']} \n and the content is: {json_obj['content']} \n"
    )
