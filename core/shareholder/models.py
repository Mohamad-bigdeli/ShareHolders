from __future__ import annotations

from django.db import models
from django_jalali.db import models as jmodels


# Create your models here.

class ShareholdersHistory(models.Model):
    id = models.AutoField(verbose_name="آیدی", primary_key=True)
    date = models.DateField(verbose_name="تاریخ ثبت میلادی", null=True, blank=True)
    shareholder_id = models.CharField(max_length=55, verbose_name="شناسه سهامدار", null=True, blank=True)
    shareholder_shares = models.FloatField(verbose_name="تعداد سهام", null=True, blank=True)
    shareholder_percentage = models.FloatField(verbose_name="درصد سهام", null=True, blank=True)
    shareholder_instrument_id = models.CharField(max_length=55, verbose_name="شناسه ابزار مالی", null=True, blank=True)
    shareholder_name = models.CharField(max_length=255, verbose_name="نام سهامدار", null=True, blank=True)
    change = models.IntegerField(verbose_name="تغییر", null=True, blank=True)
    symbol = models.CharField(max_length=50, verbose_name="نماد بورسی", null=True, blank=True)
    jalali_date = jmodels.jDateField(verbose_name="تاریخ ثبت شمسی", null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")

    class Meta:
        verbose_name = "سهامدار عمده"
        verbose_name_plural = "سهامداران عمده"
        ordering = ['-date', '-shareholder_percentage']
        indexes = [
            models.Index(fields=['symbol']),
            models.Index(fields=['date']),
            models.Index(fields=['shareholder_name']),
        ]

    def __str__(self):
        return f"{self.shareholder_name} - {self.symbol}"