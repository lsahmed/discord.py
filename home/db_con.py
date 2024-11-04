import pymongo
from bson.objectid import ObjectId
import base64
import os

url = "mongodb+srv://contrailpy:contrailpy@cluster0.xpysx.mongodb.net/"
client = pymongo.MongoClient(url)
db = client['portfolio']

# <--- Skills Collection Management -->
skills = db['skills']

# <-- projects Collection Management -->
projects = db['projects']
project = list(projects.find())

# filter = {"_id":ObjectId('6728db4ef3d95aeafa9efd38')}
# update = {
#     "$set": {
#         "img1": "https://shorturl.at/kOzYZ"
#     }
# }
# result = projects.update_one(filter ,update)


# if result.modified_count > 0:
#     print(f'Document with ID  updated successfully.')
# else:
#     print(f'No document found with ID  or no changes made.')

print(project)







