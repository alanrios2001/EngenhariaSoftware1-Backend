from datetime import datetime
from Chat import Chat
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from enum import Enum
import pytz

class Roles(str, Enum):
    USUARIO = 'usuario'
    CHATBOT = 'chatbot'

class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, autoincrement=True)
    chat_id: int = Field(foreign_key="chat.id")
    conteudo: str = Field()
    role_type: Roles = Field()
    created_at: datetime = Field(default_factory=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))
    deleted_at: datetime = Field(default_factory=None)
    chat: "Chat" = Relationship(back_populates="mensagens", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    
    def __init__(self, conteudo, chat_id, role):
        self.conteudo = conteudo
        self.chat_id = chat_id
        self.role_type = role
        self.created_at = datetime.now(pytz.timezone('America/Sao_Paulo'))
        self.deleted_at = None

