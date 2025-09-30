# cadastrar_usuario/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .form import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

    def get_success_url(self):
        """
        Redireciona o usuário para a página correta após o login.
        """
        user = self.request.user

        # Verifica se o usuário tem um perfil e se é dono de loja
        if hasattr(user, 'profile') and user.profile.is_store_owner:
            # Se for lojista, vai para a página de detalhes da loja
            return reverse_lazy('detalhe_loja')
        else:
            # Se for cliente, vai para a vitrine de produtos
            return reverse_lazy('home')
        
def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f"Conta criada para {username}. Você já pode fazer login.")
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo para continuar.') 
    
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'usuarios/cadastro_usuario.html', {'user_form': user_form, 'profile_form': profile_form})

from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

@login_required
def perfil(request):
    # mostra dados do usuário e do perfil
    return render(request, 'usuarios/perfil.html')
