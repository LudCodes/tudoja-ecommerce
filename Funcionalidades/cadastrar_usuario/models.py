# cadastrar_usuario/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField("Telefone", max_length=20, blank=True)
    address = models.CharField("Endereço", max_length=255, blank=True)
    is_store_owner = models.BooleanField("É lojista?", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - perfil"
