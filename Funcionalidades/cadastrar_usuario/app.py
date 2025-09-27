# cadastrar_usuario/apps.py
from django.apps import AppConfig

class CadastrarUsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cadastrar_usuario'

    def ready(self):
        import cadastrar_usuario.signals  # noqa
