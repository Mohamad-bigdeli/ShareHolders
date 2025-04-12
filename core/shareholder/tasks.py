from celery import shared_task
from .models import Shareholder, ShareholderHistory

@shared_task(bind=True, max_retries=3)
def create_history_record(self, shareholder_id):
    try:
        shareholder = Shareholder.objects.get(id=shareholder_id)
        
        last_history = ShareholderHistory.objects.filter(shareholder_id=shareholder.shareholder_id, symbol=shareholder.symbol).order_by('-date').first()
        
        shares_change = 0
        percentage_change = 0
        direction = 'stable'
        
        if last_history:
            shares_change = shareholder.shareholder_shares - last_history.shares
            percentage_change = shareholder.shareholder_percentage - last_history.percentage
            direction = 'increase' if percentage_change > 0 else 'decrease' if percentage_change < 0 else 'stable'
        
        ShareholderHistory.objects.create(
            shareholder=shareholder,
            date=shareholder.date,
            symbol=shareholder.symbol,
            shares=shareholder.shareholder_shares,
            percentage=shareholder.shareholder_percentage,
            shares_change=shares_change,
            percentage_change=percentage_change,
            ownership_change_direction=direction
        )
    except Exception as e:
        raise self.retry(exc=e, countdown=60)