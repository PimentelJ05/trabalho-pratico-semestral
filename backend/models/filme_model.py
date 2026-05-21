from pydantic import BaseModel, Field
from typing import Optional


class Filme(BaseModel):
    titulo: str = Field(..., min_length=2)
    descricao: str = Field(..., min_length=5)
    genero: str = Field(..., min_length=2)
    ano: int = Field(..., ge=1888)
    diretor: str = Field(..., min_length=2)
    poster_url: Optional[str] = None


class FilmeAtualizacao(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    genero: Optional[str] = None
    ano: Optional[int] = None
    diretor: Optional[str] = None
    poster_url: Optional[str] = None