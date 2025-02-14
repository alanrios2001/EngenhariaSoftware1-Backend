from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from Chat import Chat

class Token(SQLModel, table=True):
    token: str = Field(primary_key=True)
    chat_id: Optional[int] = Field(default=None, foreign_key="chat.id")
    chat: Optional["Chat"] = Relationship(back_populates="token")
