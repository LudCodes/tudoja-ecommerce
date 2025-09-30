# cadastrar_usuario/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .form import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
