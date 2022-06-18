from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

client = MongoClient(getenv('MONGO_POKEMMO'))
db = client.get_database('VOS')

trainers = db.trainers

def insert_one(user: int = None, message: int = None):
    payload = {
        '_id': user,
        'message': message,
        'ou': 0,
        'uu': 0,
        'nu': 0,
        'db': 0
    }
    
    try:
        trainers.insert_one(payload)
    
    except DuplicateKeyError: pass

def update(user: int, operator: str, path: str, value: int | str):
    data = trainers.find_one_and_update(
        {'_id': user}, 
        {f'${operator}': {
            path: value
            }
        },
        return_document = True
    )

    return data

def update_many(operator: str, payload: dict):
    trainers.update_many({}, {f'${operator}': payload})

def find(user: int = None, message: int = None):
    payload = {}

    if user:
        payload['_id'] = user

    if message:
        payload['message'] = message

    if payload:
        return trainers.find_one(payload)
    
    return list(trainers.find())

def delete(user: int = None, message: int = None):
    payload = {}

    if user:
        payload['_id'] = user

    if message:
        payload['message'] = message

    if payload:
        trainers.delete_one(payload)