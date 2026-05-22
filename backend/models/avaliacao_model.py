from pydantic import BaseModel, Field
from typing import Optional


class Avaliacao(BaseModel):
    filme_id: str = Field(..., min_length=1)
    usuario: str = Field(..., min_length=2)
    nota: int = Field(..., ge=0, le=10)
    comentario: str = Field(..., min_length=3)


class AvaliacaoAtualizacao(BaseModel):
    usuario: Optional[str] = None
    nota: Optional[int] = Field(None, ge=1, le=5)
    comentario: Optional[str] = None