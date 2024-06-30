from django.apps import AppConfig
from django.apps import apps


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    """def ready(self) -> None:
        model_list = apps.get_models()
        for model in model_list:
            print(model.__name__)
            field_list = model._meta.get_fields()
            for field in field_list:
                print(field.name)
        return super().ready()
"""