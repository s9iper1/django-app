import requests

# endpoint = "https://httpbin.org/status/200/"
# end_point = "https://httpbin.org/anything"
end_point = "http://localhost:3000/api/"

response = requests.post(end_point, json={"title": None, "content": "Hello world"})
print(response.json())
