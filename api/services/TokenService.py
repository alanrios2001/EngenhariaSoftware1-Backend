import uuid
import sqlite3

class TokenService:
    def __init__(self, db_path):
        self.db_path = db_path

    def gerar_token_unico(self, chat_id):
        token = str(uuid.uuid4())
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO token (token, chat_id) VALUES (?, ?)", (token, chat_id))
        conn.commit()
        conn.close()
        return token

    def verificar_token_existe(self, token):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM token WHERE token = ?", (token,))
        existe = cursor.fetchone() is not None
        conn.close()
        return existe

    def deletar_token(self, token):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM token WHERE token = ?", (token,))
        conn.commit()
        conn.close()

# Exemplo de uso
# token_service = TokenService('path/to/your/database.db')
# token = token_service.gerar_token_unico(chat_id=1)
# print(token)
# print(token_service.verificar_token_existe(token))
