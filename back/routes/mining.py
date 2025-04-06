from flask import Blueprint, request, jsonify
from models.block import Blockchain

mining_bp = Blueprint('mining', __name__, url_prefix='/mining')
blockchain = Blockchain()

# 📌 Mineração de Blocos
@mining_bp.route('/mine', methods=['POST'])
def mine_block():
    miner_id = request.json.get("miner_id")
    
    if not miner_id:
        return jsonify({"error": "Minerador inválido"}), 400

    message = blockchain.mine_pending_transactions(miner_id)
    return jsonify({"message": message})

# 📌 Verificar a blockchain
@mining_bp.route('/validate', methods=['GET'])
def validate_chain():
    is_valid = blockchain.is_chain_valid()
    return jsonify({"valid": is_valid})
