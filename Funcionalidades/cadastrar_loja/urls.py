# cadastrar_loja/urls.py
from django.urls import path
from . import view

urlpatterns = [
    path('minha-loja/criar/', view.criar_loja, name='criar_loja'),
    path('minha-loja/', view.detalhe_loja, name='detalhe_loja'),
    path('produtos/novo/', view.criar_produto, name='criar_produto'),
    path('produtos/', view.listar_produtos, name='listar_produtos'),
]
