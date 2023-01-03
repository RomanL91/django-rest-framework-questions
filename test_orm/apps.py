from django.apps import AppConfig


class TestOrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_orm'
