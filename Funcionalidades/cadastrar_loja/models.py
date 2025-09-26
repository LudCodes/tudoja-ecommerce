from main import db
from datetime import datetime

class Loja(db.Model):
    __tablename__ = 'lojas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(500))
    endereco = db.Column(db.String(200))
    telefone = db.Column(db.String(20))
    
    # Chave estrangeira para ligar à tabela de usuários
    proprietario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    criado_em = db.Column(db.DateTime, default=datetime.utcnow)