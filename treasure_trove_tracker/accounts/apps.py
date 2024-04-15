from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'treasure_trove_tracker.accounts'

    def ready(self):
        import treasure_trove_tracker.accounts.signals
