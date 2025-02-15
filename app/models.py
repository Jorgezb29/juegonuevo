from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.String(50), unique=True, nullable=False)  # Nuevo campo
    username = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    referrals = db.Column(db.Integer, default=0)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    reward = db.Column(db.Integer, nullable=False)
    is_ad = db.Column(db.Boolean, default=False)

class CompletedMission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'))
    completed_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    type = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())