CREATE TABLE message (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chat_id INT NOT NULL,
    conteudo TEXT NOT NULL,
    role_type ENUM('chatbot', 'usuario') NOT NULL,
    created_at DATETIME NOT NULL,
    deleted_at DATETIME,
    FOREIGN KEY (chat_id) REFERENCES chat(id)
);
