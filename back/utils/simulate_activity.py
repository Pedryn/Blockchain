import random
import logging
from models.user import User
from models.crypto import Crypto
from utils.buy_crypto import buy_crypto
from utils.sell_crypto import sell_crypto
from utils.transfer_to_user import transfer_user_to_user

def simulate_user_activity():
    users = User.get_all()
    cryptos = Crypto.get_all()

    if len(users) < 2 or not cryptos:
        logging.warning("[Simulação] Dados insuficientes para simular interações.")
        return

    user = random.choice(users)
    user_id = user['id']
    user_saldo = User.get_saldo(user_id)

    # Obter criptos que o usuário possui
    user_cryptos = [
        {'symbol': c['symbol'], 'amount': User.get_crypto_amount(user_id, c['symbol']), 'name': c['name']}
        for c in cryptos
    ]
    owned_cryptos = [c for c in user_cryptos if c['amount'] > 0]

    # Determinar ações possíveis com base no estado atual
    possible_actions = []
    if user_saldo >= min(c['price'] * 0.1 for c in cryptos):  # consegue comprar pelo menos 0.1 de alguma
        possible_actions.append("buy")
    if owned_cryptos:
        possible_actions.extend(["sell", "transfer"])

    if not possible_actions:
        # logging.info(f"[Ops] {user['name']} não tem saldo ou cripto suficiente para interações.")
        return

    action = random.choice(possible_actions)

    try:
        if action == "buy":
            crypto = random.choice(cryptos)
            symbol = crypto['symbol']
            price = crypto['price']
            max_amount = user_saldo // price
            amount = round(random.uniform(0.1, max_amount), 4)

            logging.info(f"[Compra] {user['name']} comprou {amount} de {crypto['name']} - {symbol}")
            buy_crypto(user_id, symbol, amount)

        elif action == "sell":
            crypto = random.choice(owned_cryptos)
            symbol = crypto['symbol']
            amount = round(random.uniform(0.1, min(2.0, crypto['amount'])), 4)

            logging.info(f"[Venda] {user['name']} vendeu {amount} de {crypto['name']} - {symbol}")
            sell_crypto(user_id, symbol, amount)

        elif action == "transfer":
            crypto = random.choice(owned_cryptos)
            symbol = crypto['symbol']
            amount = round(random.uniform(0.1, min(2.0, crypto['amount'])), 4)

            receiver = random.choice([u for u in users if u['id'] != user_id])
            logging.info(f"[Transferência] {user['name']} transferiu {amount} de {crypto['name']} - {symbol} para {receiver['name']}")
            transfer_user_to_user(user_id, receiver['id'], symbol, amount)

    except Exception as e:
        logging.error(f"[Erro] Erro na simulação de {action}: {str(e)}")
