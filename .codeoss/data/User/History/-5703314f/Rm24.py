import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
status = response.status_code
data = response.json()

print(status)