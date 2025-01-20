from pymongo import MongoClient
import json




# data = {}
# with open("urls.json","r") as f:
#     data = json.load(f)
#     print(data)
# for i, j in data.items():
#     print(i, j)


if __name__ == "__main__":
    url = "mongodb://127.0.0.1:27017"
    client = MongoClient(url)
    db = client["nareshcred"]
    collection = db["urls"]
    # collection.insert_one({"host":"localhost","port":"27017","user":"","pass":"","uri":"mongodb://127.0.0.1:27017"})
    print(collection.find().to_list())