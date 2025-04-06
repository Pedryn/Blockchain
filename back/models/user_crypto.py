from database.config import get_connection

class UserCrypto:
    @staticmethod
    def update_balance(user_id, symbol, amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO user_cryptos (user_id, symbol, amount)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE amount = amount + VALUES(amount)
        """, (user_id, symbol, amount))
        conn.commit()
        conn.close()