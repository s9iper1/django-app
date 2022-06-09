import requests
import constants

end_point = constants.SERVER_IP + "/api/products/"

data = {
    "id": 11000,
    "title": "Head's and shoulder",
    "price": 99.99,
    "content": "anti dandruff shampoo"
}

response = requests.post(end_point, json=data)
print(response.json())