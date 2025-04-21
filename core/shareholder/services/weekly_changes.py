from __future__ import annotations

from datetime import datetime, timedelta

from .base_changes import BaseChanges


class WeeklyChanges(BaseChanges):
    def __init__(self, symbol: str, current_date: datetime.date):
        super().__init__(symbol, current_date - timedelta(days=7))

    def calculate_weekly_changes(self):
        return self.calculate_changes()