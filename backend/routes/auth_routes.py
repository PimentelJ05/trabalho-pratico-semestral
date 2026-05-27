from fastapi import APIRouter, HTTPException, status
from models.usuario_model import UsuarioRegistro, UsuarioLogin
from database import usuarios_collection
from auth import (
    gerar_hash_senha,
    verificar_senha,
    criar_token
)
from uuid import uuid4


router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)


@router.post("/registro", status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioRegistro):

    usuario_existente = usuarios_collection.find_one({
        "email": usuario.email
    })

    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )

    novo_usuario = {
        "_id": str(uuid4()),
        "nome": usuario.nome,
        "email": usuario.email,
        "senha": gerar_hash_senha(usuario.senha),
        "perfil": usuario.perfil
    }

    usuarios_collection.insert_one(novo_usuario)

    return {
        "message": "Usuário registrado com sucesso"
    }


@router.post("/login")
def login(usuario: UsuarioLogin):

    usuario_encontrado = usuarios_collection.find_one({
        "email": usuario.email
    })

    if not usuario_encontrado:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos"
        )

    senha_valida = verificar_senha(
        usuario.senha,
        usuario_encontrado["senha"]
    )

    if not senha_valida:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos"
        )

    token = criar_token({
        "id": usuario_encontrado["_id"],
        "email": usuario_encontrado["email"],
        "perfil": usuario_encontrado["perfil"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }