from pymongo import MongoClient

def get_fields(client, db_name, collection_name):
    db = client[db_name]
    collection = db[collection_name]
    fields = collection.find_one()
    if fields is not None:
        for key in fields.keys():
            print(key)

def get_documents(client, db_name, collection_name, filter_criteria={}):
    db = client[db_name]
    collection = db[collection_name]
    documents = collection.find(filter_criteria)
    for document in documents:
        print(document)

def update_document(client, db_name, collection_name, filter_criteria, update_data):
    db = client[db_name]
    collection = db[collection_name]
    collection.update_one(filter_criteria, {"$set": update_data})

def update_all_documents(client, db_name, collection_name, update_data, filter_criteria={}):
    db = client[db_name]
    collection = db[collection_name]
    collection.update_many(filter_criteria, {"$set": update_data})

def delete_document(client, db_name, collection_name, filter_criteria):
    db = client[db_name]
    collection = db[collection_name]
    collection.delete_one(filter_criteria)

def delete_all_documents(client, db_name, collection_name, filter_criteria={}):
    db = client[db_name]
    collection = db[collection_name]
    collection.delete_many(filter_criteria)

def insert_many_documents(client, db_name, collection_name, documents):
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(documents)

if __name__ == "__main__":
    url = "mongodb://127.0.0.1:27017"
    client = MongoClient(url)
    get_fields(client=client, db_name="nareshcred", collection_name="urls")
    get_documents(client=client, db_name="nareshcred", collection_name="urls")
