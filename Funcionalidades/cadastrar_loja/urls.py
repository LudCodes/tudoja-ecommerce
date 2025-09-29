from django.urls import path
from . import views  # cuidado, você estava usando 'view' (deve ser 'views')

urlpatterns = [
    # -------------------------------
    # URLs do dono da loja (painel)
    # -------------------------------
    path('minha-loja/criar/', views.criar_loja, name='criar_loja'),
    path('minha-loja/', views.detalhe_loja, name='detalhe_loja'),
    path('produtos/novo/', views.criar_produto, name='criar_produto'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),

    # -------------------------------
    # URLs para clientes / vitrine
    # -------------------------------
    path('', views.home, name='home'),  # página inicial com todos os produtos
    path('loja/<int:store_id>/', views.loja_detalhe, name='loja_detalhe'),  # produtos de uma loja específica
]
