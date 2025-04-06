from instance.blockchain_instance import blockchain_instance
from models.transaction import Transaction
from models.crypto import Crypto
from models.user import User

def buy_crypto(user_id, crypto_symbol, amount):
    user = User.get_by_id(user_id)
    crypto = Crypto.get_by_symbol(crypto_symbol)

    if not user or not crypto:
        return False, "Usuário ou cripto inválido."

    total_cost = crypto["price"] * amount
    if user["saldo"] < total_cost:
        return False, "Saldo insuficiente."

    # Deduz do saldo em reais
    User.update_saldo(user_id, (user['saldo']-total_cost) )
    # Aumenta a quantidade de cripto
    User.update_crypto_amount(user_id, crypto_symbol, amount)

    # Registrar transação
    tx = Transaction("SYSTEM", user_id, crypto_symbol, amount)
    blockchain_instance.add_transaction(tx)
    blockchain_instance.mine_pending_transactions("SYSTEM")

    return True, "Compra concluída."
