from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Login personalizado
    path('login/', views.CustomLoginView.as_view(), name='login'),

    # Logout usando LogoutView do Django
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    # Cadastro de novo usuário
    path('register/', views.register, name='register'),

    # Perfil do usuário (requer login)
    path('perfil/', views.perfil, name='perfil'),
]
