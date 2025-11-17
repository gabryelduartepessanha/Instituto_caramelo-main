from django.apps import AppConfig


class CadastroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cadastro'

    def ready(self):
        try:
            import cadastro.signals
        except Exception as e:
            print(f"Erro ao importar signals: {e}")
