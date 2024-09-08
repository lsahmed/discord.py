import requests

response = requests.get("https://api.freeapi.app/api/v1/seed/generated-credentials")
data = response.json()

if data