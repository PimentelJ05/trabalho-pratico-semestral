from fastapi import APIRouter
from models.filme_model import Filme
from uuid import uuid4

router = APIRouter(
    prefix="/filmes",
    tags=["Filmes"]
)

filmes = []


@router.post("/")
def criar_filme(filme: Filme):

    novo_filme = {
        "id": str(uuid4()),
        **filme.dict()
    }

    filmes.append(novo_filme)

    return {
        "message": "Filme adicionado com sucesso",
        "filme": novo_filme
    }


@router.get("/")
def listar_filmes():
    return filmes