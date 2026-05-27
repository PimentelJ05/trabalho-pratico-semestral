import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = MongoClient(MONGO_URI)

database = client[DATABASE_NAME]

filmes_collection = database["filmes"]
avaliacoes_collection = database["avaliacoes"]
usuarios_collection = database["usuarios"]

print("MongoDB conectado com sucesso!")