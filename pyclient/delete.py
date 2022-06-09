import requests
import constants

# endpoint = "https://httpbin.org/status/200/"
# end_point = "https://httpbin.org/anything"
product_id = input("what is the product id you want to delete?\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print("product id is not valid")

end_point = constants.SERVER_IP + f"/api/products/{product_id}/delete/"

response = requests.delete(end_point)
print(response.status_code, response.status_code == 204)
