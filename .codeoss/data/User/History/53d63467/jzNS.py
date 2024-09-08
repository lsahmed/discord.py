import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
request = requests.get(url)
print(request.status())