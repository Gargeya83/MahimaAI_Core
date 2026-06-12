import sqlite3
from cryptography.fernet import Fernet
import os

class MemoryVault:
    def __init__(self, vault_path="data/memory.db"):
        self.vault_path = vault_path
        # Generate or load a local encryption key
        if not os.path.exists("data/secret.key"):
            key = Fernet.generate_key()
            with open("data/secret.key", "wb") as key_file:
                key_file.write(key)
        
        self.cipher = Fernet(open("data/secret.key", "rb").read())
        self.conn = sqlite3.connect(self.vault_path)
        self.setup_db()

    def setup_db(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS memories (id INTEGER PRIMARY KEY, content BLOB)")

    def save_memory(self, text):
        encrypted_text = self.cipher.encrypt(text.encode())
        self.conn.execute("INSERT INTO memories (content) VALUES (?)", (encrypted_text,))
        self.conn.commit()

    def get_all_memories(self):
        cursor = self.conn.execute("SELECT content FROM memories")
        return [self.cipher.decrypt(row[0]).decode() for row in cursor.fetchall()]