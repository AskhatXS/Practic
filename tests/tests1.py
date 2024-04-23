import requests
url = "http://127.0.0.1:8000/api/products/create"

data1 = {
        "name": "idk",
        "description1": "idk",
        "description2": "idk",
        "price": "100",
        "quantity": "10",
        "image": "",
}
response = requests.post(url, json=data1)

print(response.json())
