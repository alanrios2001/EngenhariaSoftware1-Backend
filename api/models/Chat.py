from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from models.Message import Message
from Token import Token
import pytz

class Chat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, autoincrement=True, primary_key=True)
    token: Optional["Token"] = Relationship(back_populates="chat", sa_relationship_kwargs={"uselist": False})
    created_at: datetime = Field(default_factory=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))
    deleted_at: datetime = Field(default_factory=None)
    mensagens: List["Message"] = Relationship(back_populates="chat", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    
    def __init__(self, token: str):
        self.token = token
        self.created_at = datetime.now(pytz.timezone('America/Sao_Paulo'))
        self.updated_at = datetime.now(pytz.timezone('America/Sao_Paulo'))
        self.deleted_at = None
        self.mensagens = []
    
    def adicionar_mensagem(self, mensagem: "Message"):
        self.mensagens.append(mensagem)

