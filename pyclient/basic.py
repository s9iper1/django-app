import requests
import constants

# endpoint = "https://httpbin.org/status/200/"
# end_point = "https://httpbin.org/anything"
end_point = constants.SERVER_IP + "/api/"

response = requests.post(end_point, json={"title": None, "content": "Hello world"})
print(response.json())
