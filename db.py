MONGODB_SETTINGS = {
    'DB': 'Your_DB_Name',
    'host': 'localhost',
    'port': 27017,
}
from pymongo import MongoClient
client = MongoClient(f'{MONGODB_SETTINGS["host"]}:{MONGODB_SETTINGS["port"]}')
db = client.DoctorsDB