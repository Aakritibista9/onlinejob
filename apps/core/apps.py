from django.apps import AppConfig

# Django AppConfig for the 'core' app
class CoreConfig(AppConfig):
    # Sets the default auto field to 'BigAutoField' for model ID fields
    default_auto_field = 'django.db.models.BigAutoField'
    # Specifies the name of the app, used in various Django configurations
    name = 'apps.core'
