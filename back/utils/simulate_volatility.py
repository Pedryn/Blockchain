import random
import logging
from models.crypto import Crypto

def simulate_volatility():
    all_cryptos = Crypto.get_all()

    if not all_cryptos:
        logging.info("[Volatility] Nenhuma cripto encontrada.")
        return

    for crypto in all_cryptos:
        volatility = random.uniform(-0.05, 0.05)
        if volatility != 0:
            current_price = crypto['price']
            new_price = round(current_price + (current_price * volatility), 4)

            new_price = max(new_price, 0.001)

            Crypto.update_price(crypto['symbol'], new_price)

            if volatility > 0:
                logging.info(
                f"[Subiu! :)] {crypto['name']} - {crypto['symbol']} valorizou {volatility*100:.2f}%: R${current_price} -> R${new_price}"
            )   
            else:
                logging.info(
                    f"[Desceu :/] {crypto['name']} - {crypto['symbol']} desvalorizou {volatility*100:.2f}%: R${current_price} -> R${new_price}"
            )
