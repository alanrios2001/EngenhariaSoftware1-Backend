from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Enum, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_de_usuario = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    nome = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    chats = relationship("Chat", back_populates="user")  

class Chat(Base):
    __tablename__ = 'chat'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(500), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)  
    user = relationship("User", back_populates="chats")  

    messages = relationship("Message", back_populates="chat")
    token_rel = relationship("Token", back_populates="chat", uselist=False)

class Token(Base):
    __tablename__ = 'token'

    token = Column(String(500), primary_key=True, nullable=False)
    chat_id = Column(Integer, ForeignKey('chat.id'), nullable=False, unique=True)

    chat = relationship("Chat", back_populates="token_rel")

class Message(Base):
    __tablename__ = 'message'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey('chat.id'), nullable=False)
    conteudo = Column(Text, nullable=False)
    role_type = Column(Enum('chatbot', 'usuario', name='role_type_enum'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    chat = relationship("Chat", back_populates="messages")

class Prompt(Base):
    __tablename__ = 'prompt'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    system_prompt = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

# Criar conexão com o banco de dados 
DATABASE_URL = "sqlite:///banco.db"  
engine = create_engine(DATABASE_URL, echo=True)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criar sessão para interagir com o banco
Session = sessionmaker(bind=engine)
