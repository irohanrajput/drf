import requests

product_id = input("Enter the product id: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print("Invalid product id")
    

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"



r = requests.delete(endpoint)

print(r.status_code, r.json())