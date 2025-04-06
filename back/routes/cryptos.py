from flask import Blueprint, request, jsonify
from models.crypto import Crypto

cryptos_bp = Blueprint('cryptos', __name__, url_prefix='/cryptos')

@cryptos_bp.route('/cadastrar', methods=['POST'])
def create_crypto():
    data = request.json
    new_crypto = Crypto(data['symbol'], data['name'], data['price'])
    created = new_crypto.save()
    if created:
        return jsonify({'message': 'Cripto criada com sucesso'}), 201
    return jsonify({'error': 'Erro ao criar cripto'}), 500

@cryptos_bp.route('/listar', methods=['GET'])
def list_cryptos():
    return jsonify(Crypto.get_all()), 200

@cryptos_bp.route('/listar/<symbol>', methods=['GET'])
def get_crypto(symbol):
    crypto = Crypto.get_by_symbol(symbol)
    if crypto:
        return jsonify(crypto), 200
    return jsonify({'error': 'Cripto não encontrada'}), 404

@cryptos_bp.route('/atualizar/<symbol>', methods=['PUT'])
def update_crypto(symbol):
    data = request.json
    updated = Crypto.update(symbol, data.get('name'), data.get('price'))
    if updated:
        return jsonify({'message': 'Cripto atualizada com sucesso'}), 200
    return jsonify({'error': 'Erro ao atualizar cripto'}), 500

@cryptos_bp.route('/excluir/<symbol>', methods=['DELETE'])
def delete_crypto(symbol):
    deleted = Crypto.delete(symbol)
    if deleted:
        return jsonify({'message': 'Cripto excluída com sucesso'}), 200
    return jsonify({'error': 'Erro ao excluir cripto'}), 500
