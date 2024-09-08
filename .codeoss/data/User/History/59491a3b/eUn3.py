# create a program based on stock market. 

import requests

response = requests.get("https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query={stock}")