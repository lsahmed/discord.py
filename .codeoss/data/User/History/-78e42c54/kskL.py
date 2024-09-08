import requests

app_id = 'f9ab519c8864420ab3e3bf3082b5d9f9'
response = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={app_id}&base=USD")
status = response.status_code
print(status)
data = response.json()

if(status==200):
    print(status)
