from fastapi import APIRouter, HTTPException, status
from models.filme_model import Filme, FilmeAtualizacao
from database import filmes_collection
from uuid import uuid4


router = APIRouter(
    prefix="/filmes",
    tags=["Filmes"]
)


def formatar_filme(filme):
    return {
        "id": filme["_id"],
        "titulo": filme["titulo"],
        "descricao": filme["descricao"],
        "genero": filme["genero"],
        "ano": filme["ano"],
        "diretor": filme["diretor"],
        "poster_url": filme.get("poster_url")
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_filme(filme: Filme):
    novo_filme = {
        "_id": str(uuid4()),
        **filme.model_dump()
    }

    filmes_collection.insert_one(novo_filme)

    return {
        "message": "Filme adicionado com sucesso",
        "filme": formatar_filme(novo_filme)
    }


@router.get("/")
def listar_filmes():
    filmes = filmes_collection.find()

    return [formatar_filme(filme) for filme in filmes]


@router.get("/{filme_id}")
def buscar_filme_por_id(filme_id: str):
    filme = filmes_collection.find_one({"_id": filme_id})

    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )

    return formatar_filme(filme)


@router.put("/{filme_id}")
def atualizar_filme(filme_id: str, filme_atualizado: FilmeAtualizacao):
    dados_atualizados = filme_atualizado.model_dump(exclude_unset=True)

    if not dados_atualizados:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nenhum dado enviado para atualização"
        )

    resultado = filmes_collection.update_one(
        {"_id": filme_id},
        {"$set": dados_atualizados}
    )

    if resultado.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )

    filme = filmes_collection.find_one({"_id": filme_id})

    return {
        "message": "Filme atualizado com sucesso",
        "filme": formatar_filme(filme)
    }


@router.delete("/{filme_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_filme(filme_id: str):
    resultado = filmes_collection.delete_one({"_id": filme_id})

    if resultado.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )

    return None