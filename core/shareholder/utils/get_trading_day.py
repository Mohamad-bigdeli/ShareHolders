from datetime import timedelta , datetime
from jdatetime import date as jdate
import holidays

IRAN_HOLIDAYS = holidays.Iran()

def get_last_trading_day(target_date):

    current_date = target_date
    while True:
        jalali_date = jdate.fromgregorian(date=current_date)
        is_weekend = current_date.weekday() in [3, 4]  
        is_holiday = current_date in IRAN_HOLIDAYS
        if not is_weekend and not is_holiday:
            return current_date
        current_date -= timedelta(days=1)
