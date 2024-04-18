from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return usuario.query.get(user_id)

class usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False, unique=True)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())   

class produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    tamanho = db.Column(db.String(255), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())   