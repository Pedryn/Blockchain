from models.transaction import Transaction
import time, hashlib, json

class Block:
    def __init__(self, block_index, previous_hash, transactions, timestamp=None, nonce=0):
        self.block_index = block_index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = {
            "block_index": self.block_index,
            "previous_hash": self.previous_hash,
            "transactions": [t.to_dict() for t in self.transactions],
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = self.create_genesis_block()
        self.pending_transactions = []
        self.difficulty = difficulty

    def create_genesis_block(self):
        # Criando o bloco gênese manualmente
        return [Block(0, "0", [], timestamp=time.time())]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        if not self.pending_transactions:
            return "Nenhuma transação para minerar."

        new_block = Block(
            block_index=len(self.chain),
            previous_hash=self.chain[-1].hash if self.chain else "0",
            transactions=self.pending_transactions
        )

        new_block.mine_block(self.difficulty)
        self.pending_transactions = []

        self.chain.append(new_block)

        # Recompensa fictícia poderia ser registrada aqui como nova transação
        return new_block.hash

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print(f"Hash do bloco {current_block.block_index} é inválido!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Hash do bloco {current_block.block_index} não corresponde ao bloco anterior!")
                return False

            dados_bloco_atual = json.dumps({
                "block_index": current_block.block_index,
                "previous_hash": current_block.previous_hash,
                "transactions": [t.to_dict() for t in current_block.transactions],
                "timestamp": current_block.timestamp,
                "nonce": current_block.nonce
            }, sort_keys=True).encode()

            if current_block.hash != hashlib.sha256(dados_bloco_atual).hexdigest():
                return False

        return True
