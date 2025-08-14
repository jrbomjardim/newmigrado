from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    access_level = db.Column(db.String(20), default='user') # 'user' ou 'admin'
    test_start_time = db.Column(db.DateTime, default=datetime.utcnow)
    is_premium = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_remaining_test_time(self):
        if self.is_premium:
            return timedelta(0) # Usuário premium não tem tempo de teste
        
        time_elapsed = datetime.utcnow() - self.test_start_time
        remaining_time = timedelta(hours=24) - time_elapsed
        return remaining_time if remaining_time > timedelta(0) else timedelta(0)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'access_level': self.access_level,
            'is_premium': self.is_premium,
            'remaining_test_time_seconds': self.get_remaining_test_time().total_seconds()
        }

