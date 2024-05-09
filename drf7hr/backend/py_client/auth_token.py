import requests
import getpass


endpoint_token = "http://localhost:8000/api/auth"

username = input("enter username: ")
password = getpass.getpass("enter password: ")



credentials = {"username": username, "password": password}
auth_response = requests.post(endpoint_token, data=credentials)


if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Token {token}"}
    endpoint_products = "http://localhost:8000/api/products/2"
    get_response = requests.get(endpoint_products, headers=headers)
    print(get_response.json())
