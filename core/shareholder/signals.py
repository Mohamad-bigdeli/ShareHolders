from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shareholder, ShareholderHistory

@receiver(post_save, sender=Shareholder)
def create_shareholder_history(sender, instance, created, **kwargs):
    if created:
        try:
            shareholder = Shareholder.objects.get(id=instance.id)
            
            shares_change = 0
            percentage_change = 0
            direction = 'stable'
            
            ShareholderHistory.objects.create(
                shareholder=shareholder,
                date=shareholder.date,
                symbol=shareholder.symbol,
                shares=shareholder.shareholder_shares,
                percentage=shareholder.shareholder_percentage,
                shares_change=shares_change,
                percentage_change=percentage_change,
                ownership_change_direction=direction)
        except Exception:
            print("Shareholder dose not exist")