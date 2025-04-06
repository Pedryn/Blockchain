import hashlib
import uuid
from database.config import get_connection

class User:
    def __init__(self, name, password, saldo=50):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.password_hash = self.hash_password(password)
        self.saldo = saldo

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, name, password_hash, saldo) VALUES (%s, %s, %s, %s)",
                       (self.id, self.name, self.password_hash, self.saldo))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

    @staticmethod
    def get_by_id(user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def delete(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(user_id, name, password):
        conn = get_connection()
        cursor = conn.cursor()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("UPDATE users SET name = %s, password_hash = %s WHERE id = %s", (name, password_hash, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def update_saldo(user_id, new_saldo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET saldo = %s WHERE id = %s", (new_saldo, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_saldo(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT saldo FROM users WHERE id = %s", (user_id,))
        saldo = cursor.fetchone()
        conn.close()
        return saldo[0] if saldo else None

    @staticmethod
    def get_crypto_amount(user_id, symbol):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT amount FROM user_cryptos WHERE user_id = %s AND symbol = %s", (user_id, symbol))
        result = cursor.fetchone()
        conn.close()
        return result["amount"] if result else 0.0

    @staticmethod
    def update_crypto_amount(user_id, symbol, amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT amount FROM user_cryptos WHERE user_id = %s AND symbol = %s", (user_id, symbol))
        existing = cursor.fetchone()
        if existing:
            new_amount = float(existing[0]) + float(amount)
            cursor.execute("UPDATE user_cryptos SET amount = %s WHERE user_id = %s AND symbol = %s",
                           (new_amount, user_id, symbol))
        else:
            cursor.execute("INSERT INTO user_cryptos (user_id, symbol, amount) VALUES (%s, %s, %s)",
                           (user_id, symbol, amount))
        conn.commit()
        conn.close()