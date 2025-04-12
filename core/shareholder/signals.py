from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shareholder
from .tasks import create_history_record

@receiver(post_save, sender=Shareholder)
def create_shareholder_history(sender, instance, created, **kwargs):
    if created:
        create_history_record.delay(instance.id) 