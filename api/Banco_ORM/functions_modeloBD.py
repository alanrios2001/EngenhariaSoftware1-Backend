from modeloBD import Session, User, Chat, Message

# Função para criar um usuário
def criar_usuario(nome_de_usuario, password, nome=None):
    session = Session()
    usuario = User(nome_de_usuario=nome_de_usuario, password=password, nome=nome)
    session.add(usuario)
    session.commit()
    session.close()
    return usuario

# Função para criar um chat
def criar_chat(usuario, token):
    session = Session()
    chat = Chat(token=token, user=usuario)
    session.add(chat)
    session.commit()
    session.close()
    return chat

# Função para criar uma mensagem
def criar_mensagem(chat, conteudo, role_type="usuario"):
    session = Session()
    mensagem = Message(chat_id=chat.id, conteudo=conteudo, role_type=role_type)
    session.add(mensagem)
    session.commit()
    session.close()
    return mensagem

# Função para buscar um usuário
def buscar_usuario(nome_de_usuario):
    session = Session()
    usuario = session.query(User).filter_by(nome_de_usuario=nome_de_usuario).first()
    session.close()
    return usuario

# Função para buscar chats de um usuário
def buscar_chats(usuario_id):
    session = Session()
    chats = session.query(Chat).filter_by(user_id=usuario_id).all()
    session.close()
    return chats

# Função para buscar mensagens de um chat
def buscar_mensagens(chat_id):
    session = Session()
    mensagens = session.query(Message).filter_by(chat_id=chat_id).all()
    session.close()
    return mensagens
