from __init__ import client

def list_all_databases(client):
    databases = [
        db for db in client.list_database_names() if db not in ["config", "local"]
    ]
    print("Databases in MongoDB:")
    for db in databases:
        print(db)


def get_database_size(client, db_name="admin"):
    db = client[db_name]
    stats = db.command("dbStats")
    db_size = stats.get("dataSize", 0)
    print(f"Size of database '{db_name}': {db_size / (1024 * 1024)} MB")


def list_all_collections(client, db_name="admin"):
    db = client[db_name]
    collections = db.list_collection_names()
    print(f"Collections in database '{db_name}':")
    for collection in collections:
        print(collection)


def get_collection_size(client, db_name, collection_name):
    db = client[db_name]
    collection = db[collection_name]
    stats = collection.database.command("collstats", collection.name)
    collection_size = stats.get("storageSize", "N/A")
    print(
        f"Size of collection '{collection_name}' in database '{db_name}': {collection_size / (1024 * 1024)} MB"
    )


def get_document_count_in_collection(client):
    pass


def ping_check(client):
    status = client.admin.command("ping")
    print(f"Ping status: {status['ok']}")


def get_mongo_connections(client, db_name):
    try:
        db = client[db_name]
        server_status = db.command("serverStatus")
        connections = server_status.get("connections", {})
        print("MongoDB Connection Details:")
        print(f"Current connections: {connections.get('current', 'N/A')}")
        print(f"Available connections: {connections.get('available', 'N/A')}")
        print(f"Total created connections: {connections.get('totalCreated', 'N/A')}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    ping_check(client=client)
    get_mongo_connections(client=client, db_name="test")
    get_database_size(client=client)
    list_all_databases(client=client)
    list_all_collections(client=client)
    get_collection_size(client=client, db_name="user", collection_name="user")
