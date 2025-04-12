from django.db import models

# Create your models here.


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

class ShareholderHistory(models.Model):
    
    shareholder = models.ForeignKey(Shareholder, on_delete=models.CASCADE, related_name='history', verbose_name="سهامدار")
    date = models.DateField(verbose_name="تاریخ محاسبه")
    symbol = models.CharField(max_length=50, verbose_name="نماد بورسی")
    shares = models.BigIntegerField(verbose_name="تعداد سهام")
    percentage = models.DecimalField(max_digits=7, decimal_places=3, verbose_name="درصد مالکیت")
    shares_change = models.BigIntegerField(verbose_name="تغییر تعداد سهام", default=0)
    percentage_change = models.DecimalField(max_digits=7, decimal_places=3, verbose_name="تغییر درصد مالکیت", default=0)
    ownership_change_direction = models.CharField(max_length=10, verbose_name="جهت تغییر مالکیت", choices=[('increase', 'افزایش'), ('decrease', 'کاهش'), ('stable', 'ثابت')], default='stable')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")

    class Meta:
        verbose_name = "تاریخچه سهامدار"
        verbose_name_plural = "تاریخچه سهامداران"
        ordering = ['-date', '-percentage']
        indexes = [
            models.Index(fields=['symbol']),
            models.Index(fields=['date']),
            models.Index(fields=['shareholder']),
        ]
        unique_together = ['shareholder', 'date']

    def __str__(self):
        return f"{self.shareholder.shareholder_name} - {self.symbol} - {self.date}"