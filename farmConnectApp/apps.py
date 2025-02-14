from django.apps import AppConfig


class FarmconnectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farmConnectApp'

    
    def ready(self):
        import farmConnectApp.signals  # Import the signals module