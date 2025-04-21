from __future__ import annotations

from datetime import datetime, timedelta

from .base_changes import BaseChanges


class MonthlyChanges(BaseChanges):
    def __init__(self, symbol: str, current_date: datetime.date):
        super().__init__(symbol, current_date - timedelta(days=30))

    def calculate_Monthly_changes(self):
        return self.calculate_changes()