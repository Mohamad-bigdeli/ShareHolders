from __future__ import annotations

from django.apps import AppConfig


class ShareholderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shareholder'

    def ready(self):
        pass