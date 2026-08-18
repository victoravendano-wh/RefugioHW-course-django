from django.apps import AppConfig


class MascotasConfig(AppConfig):
    name = 'apps.mascotas'
    def ready(self):
        import apps.mascotas.signals

