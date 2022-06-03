import requests

# endpoint = "https://httpbin.org/status/200/"
# end_point = "https://httpbin.org/anything"
end_point = "http://localhost:3000/api/products/2/"

response = requests.get(end_point)
print(response.json())
