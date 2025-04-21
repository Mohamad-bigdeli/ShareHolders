from __future__ import annotations

from datetime import datetime, timedelta
import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import ShareholdersHistory


class Command(BaseCommand):
    help = 'تولید ۱۰۰ رکورد تستی برای مدل ShareholdersHistory با استفاده از bulk_create'

    def handle(self, *args, **options):

        fake = Faker('fa_IR')

        symbols = [
            'خودرو', 'فولاد', 'وبصادر', 'فملی', 'کگل',
            'شپنا', 'شتران', 'خساپا', 'وتجارت', 'وبملت',
            'فارس', 'خپارس', 'ذوب', 'رمپنا', 'برکت',
            'ثبهساز', 'ثامید', 'ثمسکن', 'ثشهاب', 'ثاختر'
        ] * 3
        
        shareholder_names = [
            "شرکت سرمایه گذاری تأمین اجتماعی",
            "شرکت سرمایه گذاری ملی ایران",
            "صندوق بازنشستگی کشوری",
            "شرکت سرمایه گذاری غدیر",
            "شرکت سرمایه گذاری خوارزمی",
            "شرکت سرمایه گذاری توسعه صنعتی ایران",
            "شرکت سرمایه گذاری بانک ملت",
            "شرکت سرمایه گذاری بانک تجارت",
            "شرکت سرمایه گذاری بانک صادرات",
            "صندوق توسعه ملی",
            "شرکت سرمایه گذاری بانک ملی",
            "شرکت سرمایه گذاری بانک سپه",
            "شرکت سرمایه گذاری بانک صنعت و معدن",
            "شرکت سرمایه گذاری بانک کشاورزی",
            "شرکت سرمایه گذاری بانک مسکن"
        ]

        shareholder_ids = {
            "شرکت سرمایه گذاری تأمین اجتماعی": 10000001,
            "شرکت سرمایه گذاری ملی ایران": 10000002,
            "صندوق بازنشستگی کشوری": 10000003,
            "شرکت سرمایه گذاری غدیر": 10000004,
            "شرکت سرمایه گذاری خوارزمی": 10000005,
            "شرکت سرمایه گذاری توسعه صنعتی ایران": 10000006,
            "شرکت سرمایه گذاری بانک ملت": 10000007,
            "شرکت سرمایه گذاری بانک تجارت": 10000008,
            "شرکت سرمایه گذاری بانک صادرات": 10000009,
            "صندوق توسعه ملی": 10000010,
            "شرکت سرمایه گذاری بانک ملی": 10000011,
            "شرکت سرمایه گذاری بانک سپه": 10000012,
            "شرکت سرمایه گذاری بانک صنعت و معدن": 10000013,
            "شرکت سرمایه گذاری بانک کشاورزی": 10000014,
            "شرکت سرمایه گذاری بانک مسکن": 10000015
        }
        
        records = []

        for i in range(100):
            random_date = datetime.now() - timedelta(days=random.randint(1, 730))
            symbol = random.choice(symbols)
            if random.random() < 0.6:
                shareholder_name = random.choice(shareholder_names)
                shareholder_id = shareholder_ids[shareholder_name]
            else:
                shareholder_name = fake.company() + " - سهامی خاص"
                shareholder_id = random.randint(20000000, 99999999)
            
            records.append(ShareholdersHistory(
                date=random_date.date(),
                shareholder_id=shareholder_id,
                shareholder_shares=random.randint(100000, 500000000),
                shareholder_percentage=round(random.uniform(0.1, 15.0), 3),
                shareholder_instrument_id=f"IRO1{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))}{random.randint(1000, 9999)}",
                shareholder_name=shareholder_name,
                change=random.choice([-2, -1, 0, 1, 2]),
                symbol=symbol,
                jalali_date=random_date.date()
            ))
        ShareholdersHistory.objects.bulk_create(records)
        
        self.stdout.write(self.style.SUCCESS(f'با موفقیت {len(records)} رکورد تستی برای ShareholdersHistory ایجاد شد'))
