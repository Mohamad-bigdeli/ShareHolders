from __future__ import annotations

from datetime import datetime

from ..models import ShareholdersHistory
from ..utils.get_trading_day import get_last_trading_day


class BaseChanges:

    def __init__(self, symbol: str, target_date: datetime.date):
        self.symbol = symbol
        self.target_date = get_last_trading_day(target_date=target_date)
        
    def calculate_changes(self):
        current_data = ShareholdersHistory.objects.filter(symbol=self.symbol, date=datetime.now().date()).values('shareholder_id', 'shareholder_name', 'shareholder_shares', 'shareholder_percentage')
        previous_data = ShareholdersHistory.objects.filter(symbol=self.symbol, date=self.target_date).values('shareholder_id', 'shareholder_name', 'shareholder_shares', 'shareholder_percentage')

        changes = []
        
        for current in current_data:
            previous = next((p for p in previous_data if p['shareholder_id'] == current['shareholder_id']), None)
            if previous:
                change_shares = current['shareholder_shares'] - previous['shareholder_shares']
                change_percentage = current['shareholder_percentage'] - previous['shareholder_percentage']
                change_type = (
                    "صعودی" if change_shares > 0 else
                    "نزولی" if change_shares < 0 else
                    "بدون تغییر"
                )
                change = {
                    "shareholder_id": current['shareholder_id'],
                    "shareholder_name": current['shareholder_name'],
                    "current_shares": current['shareholder_shares'],
                    "previous_shares": previous['shareholder_shares'],
                    "change_shares": change_shares,
                    "current_percentage": current['shareholder_percentage'],
                    "previous_percentage": previous['shareholder_percentage'],
                    "change_percentage": change_percentage,
                    "changes": change_type
                }
            else:
                change = {
                    "shareholder_id": current['shareholder_id'],
                    "shareholder_name": current['shareholder_name'],
                    "current_shares": current['shareholder_shares'],
                    "current_percentage": current['shareholder_percentage'],
                    "previous_shares": 0,
                    "previous_percentage": 0,
                    "change_shares": current['shareholder_shares'],
                    "change_percentage": current['shareholder_percentage'],
                    "changes": "صعودی تغییرات به بالای 1 آمده"
                }
            changes.append(change)

        for previous in previous_data:
            if not any(c['shareholder_id'] == previous['shareholder_id'] for c in current_data):
                change = {
                    "shareholder_id": previous['shareholder_id'],
                    "shareholder_name": previous['shareholder_name'],
                    "current_shares": 0,
                    "current_percentage": 0,
                    "previous_shares": previous['shareholder_shares'],
                    "previous_percentage": previous['shareholder_percentage'],
                    "change_shares": -previous['shareholder_shares'],
                    "change_percentage": -previous['shareholder_percentage'],
                    "changes": "نزولی تغییرات به زیر 1 آمده"
                }
                changes.append(change)

        return changes
            