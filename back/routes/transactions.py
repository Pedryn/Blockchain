from flask import Blueprint, request, jsonify
from utils import buy_crypto
from utils import sell_crypto
from utils import transfer_to_user
from models.transaction import Transaction
from models.user import User
from models.crypto import Crypto

# --- Blueprint para Transações ---
transactions_bp = Blueprint('transactions', __name__, url_prefix='/transactions')

@transactions_bp.route('/comprar', methods=['POST'])
def buy_crypto_route():
    data = request.json
    user = User.get_by_id(data['user_id'])
    crypto = Crypto.get_by_symbol(data['symbol'])
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    if not crypto:
        return jsonify({'error': 'Cripto não encontrada'}), 404

    result = buy_crypto(data['user_id'], data['symbol'], float(data['amount']))
    return jsonify(result), 200 if 'message' in result else 400

@transactions_bp.route('/vender', methods=['POST'])
def sell_crypto_route():
    data = request.json
    user = User.get_by_id(data['user_id'])
    crypto = Crypto.get_by_symbol(data['symbol'])
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    if not crypto:
        return jsonify({'error': 'Cripto não encontrada'}), 404

    result = sell_crypto(data['user_id'], data['symbol'], float(data['amount']))
    return jsonify(result), 200 if 'message' in result else 400

@transactions_bp.route('/transferir', methods=['POST'])
def transfer_crypto_route():
    data = request.json
    sender = User.get_by_id(data['sender_id'])
    receiver = User.get_by_id(data['receiver_id'])
    crypto = Crypto.get_by_symbol(data['symbol'])

    if not sender:
        return jsonify({'error': 'Remetente não encontrado'}), 404
    if not receiver:
        return jsonify({'error': 'Destinatário não encontrado'}), 404
    if not crypto:
        return jsonify({'error': 'Cripto não encontrada'}), 404

    result = transfer_to_user(data['sender_id'], data['receiver_id'], data['symbol'], float(data['amount']))
    return jsonify(result), 200 if 'message' in result else 400
