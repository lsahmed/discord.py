import requests

response = requests.get(f"https://api.exchangerate-api.com/v4/latest/USD")
status = response.status_code
data = response.json()

if(status==200):
    curr = input("Enter in which currency you want to exchange from USD(currency code): ").upper()
    amount = input("Enter amount: ")
    val = data["rates"][curr]
    print(type(amount), type(val))
    