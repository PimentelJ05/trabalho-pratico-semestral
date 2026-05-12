from fastapi import APIRouter, HTTPException
from models.filme_model import Filme, FilmeAtualizacao
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

@router.get("/{filme_id}")
def buscar_filme_por_id(filme_id: str):
    for filme in filmes:
        if filme["id"] == filme_id:
            return filme

    raise HTTPException(status_code=404, detail="Filme não encontrado")

@router.put("/{filme_id}")
def atualizar_filme(filme_id: str, filme_atualizado: FilmeAtualizacao):

    for filme in filmes:

        if filme["id"] == filme_id:

            dados_atualizados = filme_atualizado.dict(exclude_unset=True)

            filme.update(dados_atualizados)

            return {
                "message": "Filme atualizado com sucesso",
                "filme": filme
            }

    raise HTTPException(status_code=404, detail="Filme não encontrado")

@router.delete("/{filme_id}")
def deletar_filme(filme_id: str):

    for index, filme in enumerate(filmes):

        if filme["id"] == filme_id:
            filmes.pop(index)

            return {
                "message": "Filme deletado com sucesso"
            }

    raise HTTPException(status_code=404, detail="Filme não encontrado")