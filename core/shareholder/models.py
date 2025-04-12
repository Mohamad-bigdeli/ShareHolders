from django.db import models

# Create your models here.

from django.db import models

class Shareholder(models.Model):
    
    original_id = models.BigIntegerField(verbose_name="ID منبع")
    date = models.DateField(verbose_name="تاریخ ثبت")
    shareholder_id = models.BigIntegerField(verbose_name="شناسه سهامدار")
    shareholder_shares = models.BigIntegerField(verbose_name="تعداد سهام")
    shareholder_percentage = models.DecimalField(max_digits=7, decimal_places=3, verbose_name="درصد سهام")
    shareholder_instrument_id = models.CharField(max_length=20, verbose_name="شناسه ابزار مالی")
    shareholder_name = models.CharField(max_length=255, verbose_name="نام سهامدار")
    change = models.SmallIntegerField(verbose_name="تغییر")
    symbol = models.CharField(max_length=50, verbose_name="نماد بورسی")
    
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
        unique_together = ['original_id', 'date']  

    def __str__(self):
        return f"{self.shareholder_name} - {self.symbol})"