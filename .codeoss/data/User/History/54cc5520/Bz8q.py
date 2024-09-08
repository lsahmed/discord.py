import requests
import random

response = requests.get("https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo%2Cprice&query=tech")
data = response.json()

if data["success"] and data["data"]["data"]:

    booknum = random.randint(0,9)
    print("Suggesting you a random book")
    book_data1 = data["data"]["data"][booknum]["volumeInfo"].get(title)
    # book_data2 = data["data"]["data"][booknum]["volumeInfo"]
    print(f"Title of the book is: {book_data1}\ndescription: ")
