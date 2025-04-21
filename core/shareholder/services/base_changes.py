from ..models import ShareholdersHistory
from datetime import datetime, timedelta
from ..utils.get_trading_day import get_last_trading_day

class BaseChanges:

    def __init__(self, symbol, target_date):
        self.symbol = symbol
        self.target_date = get_last_trading_day(target_date=target_date)
    
    def calculate_changes(self):
        
        current_data = ShareholdersHistory.objects.filter(symbol=self.symbol, date=datetime.now().date()).values('shareholder_id', 'shareholder_name', 'shareholder_shares', 'shareholder_percentage')
        previous_data = ShareholdersHistory.objects.filter(symbol=self.symbol, date=self.target_date).values('shareholder_id', 'shareholder_name', 'shareholder_shares', 'shareholder_percentage')

        changes = []

        for current in current_data:
            previous = previous_data.filter(shareholder_id=current.shareholder_id, symbol=current.symbol).first()
        
            if previous:
                change = {
                    "shareholder_id": current.shareholder_id,
                    "shareholder_name": current.shareholder_name,
                    "current_shares": current.shareholder_shares,
                    "previous_shares": previous.shareholder_shares,
                    "change_shares": current.shareholder_shares - previous.shareholder_shares,
                    "current_percentage": current.shareholder_percentage,                    
                    "previous_percentage": previous.shareholder_percentage,
                    "change_percentage": current.shareholder_percentage - previous.shareholder_percentage,
                    "changes": "صعودی" if current.shareholder_shares > previous.shareholder_shares else "نزولی"
                }
            else:
                change = {
                    "shareholder_id": current.shareholder_id,
                    "shareholder_name": current.shareholder_name,
                    "changes": "صعودی تغییرات به بالای 1 آمده"
                }
            changes.append(change)

            for previous in previous_data:
                if not current_data.filter(shareholder_id=previous.shareholder_id, symbol=previous.symbol):
                    change = {
                        "shareholder_id": previous.shareholder_id,
                        "shareholder_name": previous.shareholder_name,
                        "changes": "نزولی تغییرات به زیر 1 آمده"
                    }
                changes.append(change)
        return changes
                


        