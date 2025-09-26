# cadastrar_usuario/forms.py
from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("phone", "address", "is_store_owner")
