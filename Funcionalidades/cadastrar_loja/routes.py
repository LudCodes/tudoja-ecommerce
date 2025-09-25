from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from main import db
from .models import Loja

loja_bp = Blueprint('loja', __name__, template_folder='../templates/loja')

@loja_bp.route('/registro', methods=['GET', 'POST'])
def registro_loja():
    # So permite criar loja se estiver logado
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        flash('Você precisa estar logado para cadastrar uma Loja.', 'warning')
        return redirect(url_for('usuario.login_usuario'))

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        descricao = request.form.get('descricao', '').strip()
        endereco = request.form.get('endereco', '').strip()
        telefone = request.form.get('telefone', '').strip()

        if not nome:
            flash('Nome da loja é obrigatório.', 'danger')
            return render_template('registro_loja.html')
        
        nova_loja = Loja(
            nome=nome, 
            descricao=descricao,
            endereco=endereco,
            telefone=telefone,
            proprietario_id=usuario_id
        )
        db.session.add(nova_loja)
        db.session.commit()

        flash('Loja cadastrada com sucesso!', 'success')
        return redirect(url_for('loja.registro_loja')) # Redireciona de volta para a mesma página

    return render_template('registro_loja.html')