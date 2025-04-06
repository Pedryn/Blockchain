from models.user import User
from models.crypto import Crypto
from models.transaction import Transaction
from instance.blockchain_instance import blockchain_instance

def transfer_user_to_user(sender_id, receiver_id, crypto_symbol, amount):
    sender = User.get_by_id(sender_id)
    receiver = User.get_by_id(receiver_id)
    crypto = Crypto.get_by_symbol(crypto_symbol)

    if not sender or not receiver or not crypto:
        return False, "Usuário ou cripto inválido."

    if User.get_crypto_amount(sender_id, crypto_symbol) <= 0:
        return False, "Criptos insuficiente."

    # Transferência
    User.update_crypto_amount(sender_id, crypto_symbol, -amount)
    User.update_crypto_amount(receiver_id, crypto_symbol, amount)

    # Registrar transação
    tx = Transaction(sender_id, receiver_id, crypto_symbol, amount)
    blockchain_instance.add_transaction(tx)
    blockchain_instance.mine_pending_transactions("SYSTEM")

    return True, "Transferência concluída."
