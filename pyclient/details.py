import requests
import constants

# endpoint = "https://httpbin.org/status/200/"
# end_point = "https://httpbin.org/anything"
end_point = constants.SERVER_IP + "/api/products/2/"

response = requests.get(end_point)
print(response.json())
