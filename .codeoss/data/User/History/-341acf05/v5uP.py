import requests

response = requests.get("https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches")
data = response.json()

if data["success"]:
    user_data = data["data"]["data"][1]["title"]
    print(user_data)