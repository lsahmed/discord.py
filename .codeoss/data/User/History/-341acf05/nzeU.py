import requests

response = requests.get("https://api.freeapi.app/api/v1/seed/generated-credentials")
data = response.json()

if data["success"]:
    user_data = data["data"][1]
    print(user_data)