from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        db = client["project-game"]
    except ConnectionError:
        print('Erro de conexão com o banco!')
    return db
