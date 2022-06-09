import time

import requests
import constants

end_point = constants.SERVER_IP + "/api/products/"

data = {
    "title": "Head's and shoulder",
    "price": 99.99,
    "content": "anti dandruff shampoo"
}
response = requests.post(end_point, json=data)
print(response.json())
product_id = response.json()['id']

time.sleep(2)

update_end_Point = constants.SERVER_IP + f"/api/products/{product_id}/update/"
data = {
    "title": "Dove shampoo",
    "price": 10.99
}
response = requests.put(update_end_Point, json=data)
print(response.json())

time.sleep(2)
end_point = constants.SERVER_IP + f"/api/products/{product_id}/delete/"
response = requests.delete(end_point)
print(response.status_code, response.status_code == 204)
