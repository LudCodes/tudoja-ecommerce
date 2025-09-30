from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from Funcionalidades.cadastrar_loja import views as loja_views
from Funcionalidades.cadastrar_loja.views import home as home_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial da vitrine
    path('', loja_views.index, name='index'),
    
    # Nova rota para vitrine
    path('vitrine/', loja_views.home, name='home'),

    # URLs do usuário
    path('usuarios/', include('Funcionalidades.cadastrar_usuario.urls')),

    # URLs do dono da loja / painel
    path('loja/', include('Funcionalidades.cadastrar_loja.urls')),

    #URLs carrinho
     path('carrinho/', include('Funcionalidades.carrinho.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
