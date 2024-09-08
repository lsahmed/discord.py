import requests

app_id = 'f9ab519c8864420ab3e3bf3082b5d9f9'
response = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={app_id}&base=USD")
status = response.status_code
data = response.json()

if(status==200):
    curr = input("Enter currency you want to exchange from USD: ")
    howmuch = float(input("Enter quantity of dollars: "))
    product = data["rates"].get(curr)
    print(type(howmuch))
    # main_product = product*howmuch
    # round_product = round(main_product, 2)
