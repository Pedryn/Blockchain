import time, hashlib, json
from database.config import get_connection
from models.user import User
from models.crypto import Crypto

class Transaction:
    def __init__(self, sender, receiver, crypto_symbol, amount, timestamp=None):
        self.sender = sender
        self.receiver = receiver
        self.crypto_symbol = crypto_symbol
        self.amount = amount
        self.timestamp = timestamp or time.time()

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "crypto_symbol": self.crypto_symbol,
            "amount": self.amount,
            "timestamp": self.timestamp
        }
