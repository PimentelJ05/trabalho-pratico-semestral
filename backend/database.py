import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Carrega variáveis do .env
load_dotenv()

# Pega dados do .env
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Conecta no MongoDB Atlas
client = MongoClient(MONGO_URI)

# Seleciona o banco
database = client[DATABASE_NAME]

# Seleciona a collection filmes
filmes_collection = database["filmes"]

print("MongoDB conectado com sucesso!")