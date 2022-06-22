from pymongo import MongoClient
from exporter import MONGO_DB_LINK, DATABASE_NAME

DB_CONNECTION = None


def get_mongo_client():
    global DB_CONNECTION, DATABASE_NAME
    if DB_CONNECTION is None:
        DB_CONNECTION = MongoClient(MONGO_DB_LINK, connect=False)
    return DB_CONNECTION

def setup_db():
    client = get_mongo_client()
    db = client[DATABASE_NAME]
    collections_exist = db.list_collection_names()
    if "UserInfo" not in collections_exist:
        db.create_collection("UserInfo")