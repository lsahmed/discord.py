import requests

app_id = 'f9ab519c8864420ab3e3bf3082b5d9f9'
response = requests.get(f"https://api.exchangerate-api.com/v4/latest/USD")
status = response.status_code
data = response.json()