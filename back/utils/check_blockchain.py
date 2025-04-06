import logging
from instance.blockchain_instance import blockchain_instance

def check_blockchain_integrity():
    is_valid = blockchain_instance.is_chain_valid()

    if is_valid:
        logging.info("[Segurança✅] Blockchain verificada: cadeia válida ✅")
    else:
        logging.error("[Segurança❌] Alerta: cadeia inválida ou corrompida ❌")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("logs/blockchain_check.log"),
            logging.StreamHandler()
        ]
    )
    check_blockchain_integrity()
