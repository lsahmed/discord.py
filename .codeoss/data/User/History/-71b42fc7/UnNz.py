import requests

api_key = '5b18ca7cf1df4a78a42155718242007'
city = input("Enter city: ")
country = input("Enter Country: ")
response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city},{country}")
status = response.status_code
data = response.json()

