from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'um_segredo_muito_seguro_e_aleatorio' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .cadastrar_usuario.routes import usuario_bp
from .cadastrar_loja.routes import loja_bp

app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(loja_bp, url_prefix='/loja')

@app.route('/')
def home():
    return "Bem-vindo ao TudoJá! Acesse /usuario/registro para se cadastrar."

if __name__ == '__main__':
    with app.app_context():
        
        db.create_all()
    app.run(debug=True)