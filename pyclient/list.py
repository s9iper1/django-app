import requests
import constants

end_point = constants.SERVER_IP + "/api/products/"

# data = {
#     "title": "Head's and shoulder",
#     "price": 99.99,
#     "content": "anti dandruff shampoo"
# }

response = requests.get(end_point)
print(response.json())