from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
import pytz

class Prompt(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, autoincrement=True)
    system_prompt: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))
    deleted_at: Optional[datetime] = Field(default=None)

    def __repr__(self):
        return f"<Prompt(id={self.id}, system_prompt='{self.system_prompt[:30]}...')>"
