from pydantic import BaseModel, EmailStr


class UsuarioRegistro(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    perfil: str = "usuario"


class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str