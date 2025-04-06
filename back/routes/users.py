from flask import Blueprint, request, jsonify
from models.user import User

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/cadastrar', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(data['id'], data['name'], data['password'])
    created = new_user.save()
    if created:
        return jsonify({'message': 'Usuário criado com sucesso'}), 201
    return jsonify({'error': 'Erro ao criar usuário'}), 500

@users_bp.route('/listar', methods=['GET'])
def get_all_users():
    users = User.get_all()
    return jsonify(users), 200

@users_bp.route('/listar/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'Usuário não encontrado'}), 404

@users_bp.route('/atualizar/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    success = User.update(user_id, data.get('name'), data.get('password'))
    if success:
        return jsonify({'message': 'Usuário atualizado com sucesso'}), 200
    return jsonify({'error': 'Erro ao atualizar usuário'}), 500

@users_bp.route('/excluir/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = User.delete(user_id)
    if success:
        return jsonify({'message': 'Usuário excluído com sucesso'}), 200
    return jsonify({'error': 'Erro ao excluir usuário'}), 500
