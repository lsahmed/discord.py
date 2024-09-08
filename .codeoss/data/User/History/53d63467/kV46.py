import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
response = requests.get(url)
data = response.json()

if data["success"] and data["data"]:
    user_login = data["data"].get("email")
    print(user_login)