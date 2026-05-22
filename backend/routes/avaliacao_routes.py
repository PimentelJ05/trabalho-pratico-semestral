from fastapi import APIRouter, HTTPException, status
from models.avaliacao_model import Avaliacao, AvaliacaoAtualizacao
from database import avaliacoes_collection, filmes_collection
from uuid import uuid4


router = APIRouter(
    prefix="/avaliacoes",
    tags=["Avaliações"]
)


def formatar_avaliacao(avaliacao):
    return {
        "id": avaliacao["_id"],
        "filme_id": avaliacao["filme_id"],
        "usuario": avaliacao["usuario"],
        "nota": avaliacao["nota"],
        "comentario": avaliacao["comentario"]
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_avaliacao(avaliacao: Avaliacao):

    filme = filmes_collection.find_one({"_id": avaliacao.filme_id})

    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )

    nova_avaliacao = {
        "_id": str(uuid4()),
        **avaliacao.model_dump()
    }

    avaliacoes_collection.insert_one(nova_avaliacao)

    return {
        "message": "Avaliação criada com sucesso",
        "avaliacao": formatar_avaliacao(nova_avaliacao)
    }


@router.get("/")
def listar_avaliacoes():

    avaliacoes = avaliacoes_collection.find()

    return [
        formatar_avaliacao(avaliacao)
        for avaliacao in avaliacoes
    ]


@router.get("/{avaliacao_id}")
def buscar_avaliacao_por_id(avaliacao_id: str):

    avaliacao = avaliacoes_collection.find_one({"_id": avaliacao_id})

    if not avaliacao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Avaliação não encontrada"
        )

    return formatar_avaliacao(avaliacao)


@router.put("/{avaliacao_id}")
def atualizar_avaliacao(
    avaliacao_id: str,
    avaliacao_atualizada: AvaliacaoAtualizacao
):

    dados_atualizados = avaliacao_atualizada.model_dump(
        exclude_unset=True
    )

    if not dados_atualizados:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nenhum dado enviado para atualização"
        )

    resultado = avaliacoes_collection.update_one(
        {"_id": avaliacao_id},
        {"$set": dados_atualizados}
    )

    if resultado.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Avaliação não encontrada"
        )

    avaliacao = avaliacoes_collection.find_one(
        {"_id": avaliacao_id}
    )

    return {
        "message": "Avaliação atualizada com sucesso",
        "avaliacao": formatar_avaliacao(avaliacao)
    }


@router.delete(
    "/{avaliacao_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_avaliacao(avaliacao_id: str):

    resultado = avaliacoes_collection.delete_one(
        {"_id": avaliacao_id}
    )

    if resultado.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Avaliação não encontrada"
        )

    return None


@router.get("/filme/{filme_id}")
def listar_avaliacoes_por_filme(filme_id: str):

    filme = filmes_collection.find_one({"_id": filme_id})

    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )

    avaliacoes = avaliacoes_collection.find(
        {"filme_id": filme_id}
    )

    return [
        formatar_avaliacao(avaliacao)
        for avaliacao in avaliacoes
    ]