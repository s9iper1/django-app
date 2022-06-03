import requests

end_point = "http://localhost:3000/api/products/"

data = {
    "title": "Head's and shoulder",
    "price": 99.99,
    "content": "anti dandruff shampoo"
}

response = requests.get(end_point)
print(response.json())