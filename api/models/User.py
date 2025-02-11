from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
import pytz

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, autoincrement=True)
    nome_de_usuario: str = Field(unique=True, nullable=False, index=True)
    password: str = Field(nullable=False)
    nome: Optional[str] = Field(default=None) 
    created_at: datetime = Field(default_factory=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))
    deleted_at: Optional[datetime] = Field(default=None)

    def __repr__(self):
        return f"<User(id={self.id}, nome_de_usuario='{self.nome_de_usuario}')>"
