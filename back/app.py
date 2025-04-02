import hashlib
import time
import json
import random
import uuid
from flask import Flask, request, jsonify, render_template
from models import User, Transaction, Block, Blockchain

app = Flask(__name__)

# Criando usuários
users = {user.address: user for user in [User("Alice"), User("Bob"), User("Charlie"), User("Dave"), User("Eve")]} 
blockchain = Blockchain()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({addr: {"name": user.name, "balance": user.balance} for addr, user in users.items()})

@app.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.json
    sender = data["sender"]
    receiver = data["receiver"]
    amount = int(data["amount"])
    
    if sender not in users or receiver not in users:
        return jsonify({"error": "Usuário inválido"}), 400
    
    if users[sender].balance < amount:
        return jsonify({"error": "Saldo insuficiente"}), 400
    
    users[sender].balance -= amount
    users[receiver].balance += amount
    blockchain.add_transaction(Transaction(sender, receiver, amount))
    return jsonify({"message": "Transação adicionada"})

@app.route('/mine', methods=['POST'])
def mine():
    miner = request.json["miner"]
    if miner not in users:
        return jsonify({"error": "Minerador inválido"}), 400
    blockchain.mine_pending_transactions(miner)
    return jsonify({"message": "Bloco minerado com sucesso"})

@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    return jsonify([{
        "index": block.index,
        "hash": block.hash,
        "transactions": [t.to_dict() for t in block.transactions]
    } for block in blockchain.chain])

if __name__ == '__main__':
    app.run(debug=True)
