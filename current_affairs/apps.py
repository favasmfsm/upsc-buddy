from django.apps import AppConfig


class CurrentAffairsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "current_affairs"
    verbose_name = "Current Affairs"

    def ready(self):
        from . import signals  # noqa: F401
