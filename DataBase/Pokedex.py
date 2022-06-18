from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

client = MongoClient(getenv('MONGO_POKEMMO'))
db = client.get_database('VOS')

pokedex = db.pokedex

def find(name: str):
    return pokedex.find_one({'species': name})