from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from main import db
from .models import Usuario

usuario_bp = Blueprint('usuario', __name__, template_folder='../templates/usuario')

@usuario_bp.route('/registro', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome or not email or not senha:
            flash('Todos os campos são obrigatórios!', 'error')
            return redirect(url_for('usuario.registro_usuario'))
        
        # Verifica se o email já existe
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            flash('Este email já está cadastrado.', 'warning')
            return redirect(url_for('usuario.registro_usuario'))

        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.set_senha(senha)
        db.session.add(novo_usuario)
        db.session.commit()
        
        flash('Cadastro realizado com sucesso! Faça seu login.', 'success')
        return redirect(url_for('usuario.login_usuario'))

    return render_template('registro_usuario.html')


@usuario_bp.route('/login', methods=['GET', 'POST'])
def login_usuario():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.checar_senha(senha):
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('loja.registro_loja')) # Redireciona para o cadastro de loja
        else:
            flash('Email ou senha inválidos.', 'error')

    return render_template('login_usuario.html')

@usuario_bp.route('/logout')
def logout_usuario():
    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('usuario.login_usuario'))