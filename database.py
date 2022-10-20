from pymongo import MongoClient
import certifi


MONGO_URI = 'mongodb+srv://flask:BgFuKCPs06zEM3xr@project-game.4cpmyde.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()


def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        db = client["project-game"]
    except ConnectionError:
        print('Erro de conexão com o banco!')
    return db
