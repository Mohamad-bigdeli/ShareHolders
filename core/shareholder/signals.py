from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shareholder, ShareholderHistory

@receiver(post_save, sender=Shareholder)
def create_shareholder_history(sender, instance, created, **kwargs):
    pass 