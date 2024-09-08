# create a program based on stock market. 

import requests

stock = input("Enter the stock: ")
response = requests.get(f"https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query={stock}")

status = response.status_code
data = response.json()

if(status==200 and (data["success"]==True)):
    name = data["data"]["data"]["Name"]
    mc = data["data"]["data"]["marketCap"]
    cp = data["data"]["data"]["CurrentPrice"]
    print(f"Market cap of {name} is {mc} and current price of {name} is {cp} ")
        
        

