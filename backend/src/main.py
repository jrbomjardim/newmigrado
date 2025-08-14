from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = 'migrado-secret-key-2025'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///migrado.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'jwt-secret-migrado-2025'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

# Inicializar extensões
db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app, origins="*")

# Modelos de dados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    trial_start = db.Column(db.DateTime, nullable=True)
    is_premium = db.Column(db.Boolean, default=False)
    
    # Relacionamentos
    cards = db.relationship('Card', backref='author', lazy=True)
    study_sessions = db.relationship('StudySession', backref='user', lazy=True)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.Text, nullable=False)
    back = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    difficulty = db.Column(db.Integer, default=1)  # 1-5
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_reviewed = db.Column(db.DateTime, nullable=True)
    next_review = db.Column(db.DateTime, nullable=True)
    review_count = db.Column(db.Integer, default=0)
    correct_count = db.Column(db.Integer, default=0)
    
    # Chave estrangeira
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relacionamentos
    study_sessions = db.relationship('StudySession', backref='card', lazy=True)

class StudySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studied_at = db.Column(db.DateTime, default=datetime.utcnow)
    was_correct = db.Column(db.Boolean, nullable=False)
    response_time = db.Column(db.Integer, nullable=True)  # em segundos
    
    # Chaves estrangeiras
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)

# Rotas de Autenticação
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Validações
        if not data.get('name') or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Nome, email e senha são obrigatórios'}), 400
        
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email já cadastrado'}), 400
        
        # Criar usuário
        user = User(
            name=data['name'],
            email=data['email'],
            password_hash=generate_password_hash(data['password']),
            trial_start=datetime.utcnow()
        )
        
        db.session.add(user)
        db.session.commit()
        
        # Criar token JWT
        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'message': 'Usuário criado com sucesso',
            'access_token': access_token,
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'trial_start': user.trial_start.isoformat()
            }
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        if not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email e senha são obrigatórios'}), 400
        
        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not check_password_hash(user.password_hash, data['password']):
            return jsonify({'error': 'Credenciais inválidas'}), 401
        
        # Iniciar período de teste se não existir
        if not user.trial_start:
            user.trial_start = datetime.utcnow()
            db.session.commit()
        
        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'message': 'Login realizado com sucesso',
            'access_token': access_token,
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'trial_start': user.trial_start.isoformat() if user.trial_start else None,
                'is_premium': user.is_premium
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rotas de Cards
@app.route('/api/cards', methods=['GET'])
@jwt_required()
def get_cards():
    try:
        user_id = get_jwt_identity()
        cards = Card.query.filter_by(user_id=user_id).all()
        
        cards_data = []
        for card in cards:
            accuracy = (card.correct_count / card.review_count * 100) if card.review_count > 0 else 0
            cards_data.append({
                'id': card.id,
                'front': card.front,
                'back': card.back,
                'category': card.category,
                'difficulty': card.difficulty,
                'created_at': card.created_at.isoformat(),
                'last_reviewed': card.last_reviewed.isoformat() if card.last_reviewed else None,
                'review_count': card.review_count,
                'accuracy': round(accuracy, 1)
            })
        
        return jsonify({'cards': cards_data}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/cards', methods=['POST'])
@jwt_required()
def create_card():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data.get('front') or not data.get('back'):
            return jsonify({'error': 'Frente e verso do card são obrigatórios'}), 400
        
        card = Card(
            front=data['front'],
            back=data['back'],
            category=data.get('category', ''),
            difficulty=data.get('difficulty', 1),
            user_id=user_id
        )
        
        db.session.add(card)
        db.session.commit()
        
        return jsonify({
            'message': 'Card criado com sucesso',
            'card': {
                'id': card.id,
                'front': card.front,
                'back': card.back,
                'category': card.category,
                'difficulty': card.difficulty
            }
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/cards/<int:card_id>', methods=['DELETE'])
@jwt_required()
def delete_card(card_id):
    try:
        user_id = get_jwt_identity()
        card = Card.query.filter_by(id=card_id, user_id=user_id).first()
        
        if not card:
            return jsonify({'error': 'Card não encontrado'}), 404
        
        db.session.delete(card)
        db.session.commit()
        
        return jsonify({'message': 'Card excluído com sucesso'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota de Estudo
@app.route('/api/study', methods=['POST'])
@jwt_required()
def study_card():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        card_id = data.get('card_id')
        was_correct = data.get('was_correct')
        response_time = data.get('response_time', 0)
        
        if not card_id or was_correct is None:
            return jsonify({'error': 'card_id e was_correct são obrigatórios'}), 400
        
        card = Card.query.filter_by(id=card_id, user_id=user_id).first()
        if not card:
            return jsonify({'error': 'Card não encontrado'}), 404
        
        # Registrar sessão de estudo
        session = StudySession(
            user_id=user_id,
            card_id=card_id,
            was_correct=was_correct,
            response_time=response_time
        )
        
        # Atualizar estatísticas do card
        card.review_count += 1
        if was_correct:
            card.correct_count += 1
        
        card.last_reviewed = datetime.utcnow()
        
        # Algoritmo simples de repetição espaçada
        if was_correct:
            days_to_add = min(card.difficulty * 2, 30)
        else:
            days_to_add = 1
            card.difficulty = max(1, card.difficulty - 1)
        
        card.next_review = datetime.utcnow() + timedelta(days=days_to_add)
        
        db.session.add(session)
        db.session.commit()
        
        return jsonify({'message': 'Estudo registrado com sucesso'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota de Estatísticas
@app.route('/api/stats', methods=['GET'])
@jwt_required()
def get_stats():
    try:
        user_id = get_jwt_identity()
        
        # Estatísticas básicas
        total_cards = Card.query.filter_by(user_id=user_id).count()
        total_sessions = StudySession.query.filter_by(user_id=user_id).count()
        correct_sessions = StudySession.query.filter_by(user_id=user_id, was_correct=True).count()
        
        accuracy = (correct_sessions / total_sessions * 100) if total_sessions > 0 else 0
        
        # Sequência de dias estudando
        today = datetime.utcnow().date()
        streak = 0
        current_date = today
        
        while True:
            sessions_on_date = StudySession.query.filter(
                StudySession.user_id == user_id,
                db.func.date(StudySession.studied_at) == current_date
            ).count()
            
            if sessions_on_date > 0:
                streak += 1
                current_date -= timedelta(days=1)
            else:
                break
        
        # Meta diária (assumindo 20 cards por dia)
        today_sessions = StudySession.query.filter(
            StudySession.user_id == user_id,
            db.func.date(StudySession.studied_at) == today
        ).count()
        
        daily_goal = 20
        
        # Atividade recente
        recent_activities = []
        recent_sessions = StudySession.query.filter_by(user_id=user_id)\
            .order_by(StudySession.studied_at.desc()).limit(5).all()
        
        for session in recent_sessions:
            hours_ago = (datetime.utcnow() - session.studied_at).total_seconds() / 3600
            if hours_ago < 1:
                time_str = f"{int(hours_ago * 60)} minutos atrás"
            elif hours_ago < 24:
                time_str = f"{int(hours_ago)} horas atrás"
            else:
                days_ago = int(hours_ago / 24)
                time_str = f"{days_ago} dias atrás"
            
            recent_activities.append({
                'text': f"Estudou {session.card.category or 'card'}",
                'time': time_str,
                'type': 'blue' if session.was_correct else 'red'
            })
        
        return jsonify({
            'cards_studied': total_cards,
            'streak_days': streak,
            'accuracy': round(accuracy, 1),
            'daily_progress': {
                'current': today_sessions,
                'goal': daily_goal
            },
            'recent_activities': recent_activities
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota de informações do usuário
@app.route('/api/user', methods=['GET'])
@jwt_required()
def get_user():
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'trial_start': user.trial_start.isoformat() if user.trial_start else None,
            'is_premium': user.is_premium
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)

