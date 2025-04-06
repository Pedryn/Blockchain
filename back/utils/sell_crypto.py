from instance.blockchain_instance import blockchain_instance
from models.transaction import Transaction
from models.crypto import Crypto
from models.user import User


def sell_crypto(user_id, crypto_symbol, amount):
    user = User.get_by_id(user_id)
    crypto = Crypto.get_by_symbol(crypto_symbol)

    if not user or not crypto:
        return False, "Usuário ou cripto inválido."

    if User.get_crypto_amount(user_id, crypto_symbol) <= 0:
        return False, "Quantidade insuficiente para venda."

    total_gain = crypto["price"] * amount

    # Retira cripto e adiciona saldo
    User.update_crypto_amount(user_id, crypto_symbol, -amount)
    User.update_saldo(user_id, (user['saldo']+total_gain))

    # Registrar transação
    tx = Transaction(user_id, "SYSTEM", crypto_symbol, amount)
    blockchain_instance.add_transaction(tx)
    blockchain_instance.mine_pending_transactions("SYSTEM")

    return True, "Venda concluída."
