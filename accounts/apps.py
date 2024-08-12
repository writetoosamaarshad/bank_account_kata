from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration class for the 'accounts' Django app.
    Specifies the default field type for auto-created primary keys and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Specifies the type of auto-created primary keys
    name = 'accounts'  # The name of the app as defined in the project
