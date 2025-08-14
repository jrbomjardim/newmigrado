from flask import Blueprint, jsonify, request
from src.models.user import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

user_bp = Blueprint(\'user\', __name__)

@user_bp.route(\'/register\', methods=[\'POST\'])
def register_user():
    data = request.json
    username = data.get(\'username\')
    email = data.get(\'email\')
    password = data.get(\'password\')

    if not username or not email or not password:
        return jsonify({\'message\': \'Missing username, email or password\'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({\'message\': \'Username already exists\'}), 409

    if User.query.filter_by(email=email).first():
        return jsonify({\'message\': \'Email already exists\'}), 409

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({\'message\': \'User registered successfully\', \'user\': new_user.to_dict()}), 201

@user_bp.route(\'/login\', methods=[\'POST\'])
def login_user():
    data = request.json
    username = data.get(\'username\')
    password = data.get(\'password\')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({\'message\': \'Invalid credentials\'}), 401

    # TODO: Implementar JWT para gerar token de acesso
    return jsonify({\'message\': \'Login successful\', \'user\': user.to_dict()}), 200

@user_bp.route(\'/me\', methods=[\'GET\'])
def get_current_user():
    # TODO: Proteger esta rota com JWT
    # Por enquanto, retorna um usuário de exemplo ou o primeiro usuário
    user = User.query.first()
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({\'message\': \'No user found\'}), 404

@user_bp.route(\'/users\', methods=[\'GET\'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route(\'/users/<int:user_id>\', methods=[\'GET\'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@user_bp.route(\'/users/<int:user_id>\', methods=[\'PUT\'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data.get(\'username\', user.username)
    user.email = data.get(\'email\', user.email)
    if \'password\' in data:
        user.set_password(data[\'password\'])
    db.session.commit()
    return jsonify(user.to_dict())

@user_bp.route(\'/users/<int:user_id>\', methods=[\'DELETE\'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return \'\', 204


