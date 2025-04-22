from celery import shared_task
from .services import DailyChanges, WeeklyChanges, MonthlyChanges


@shared_task
def daily_changes_task(symbol, current_date):
    
    service = DailyChanges(symbol=symbol, current_date=current_date)
    changes_data = service.calculate_daily_changes()
    return changes_data

@shared_task
def weekly_changes_task(symbol, current_date):
    
    service = WeeklyChanges(symbol=symbol, current_date=current_date)
    changes_data = service.calculate_weekly_changes()
    return changes_data

@shared_task
def monthly_changes_task(symbol, current_date):
    
    service = MonthlyChanges(symbol=symbol, current_date=current_date)
    changes_data = service.calculate_Monthly_changes()
    return changes_data