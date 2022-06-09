import requests
import constants

end_point = constants.SERVER_IP + "/api/products/2/update/"

data = {
    "title": "This is another test",
    "price": 10.99
}

response = requests.put(end_point, json=data)
print(response.json())
