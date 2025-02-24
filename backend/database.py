# MongoDB connection
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://baggiop1:PEBcap04!@cluster0.s8sih.mongodb.net/"

# MongoDB setup
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Improving_Intelligence_Confidence"]
history_collection = db["UserHistory"]