from database.config import get_connection

class Crypto:
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cryptos (symbol, name, price) VALUES (%s, %s, %s)",
            (self.symbol, self.name, self.price)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cryptos")
        data = cursor.fetchall()
        conn.close()
        return data

    @staticmethod
    def get_by_symbol(symbol):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cryptos WHERE symbol = %s", (symbol,))
        data = cursor.fetchone()
        conn.close()
        return data

    @staticmethod
    def update(symbol, name, price):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE cryptos SET name = %s, price = %s WHERE symbol = %s",
            (name, price, symbol)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(symbol):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cryptos WHERE symbol = %s", (symbol,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_price(symbol, price):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE cryptos SET price = %s WHERE symbol = %s", (price, symbol))
        conn.commit()
        conn.close()