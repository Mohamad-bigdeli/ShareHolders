from __future__ import annotations

from django.contrib import admin

from .models import ShareholdersHistory


# Register your models here.

@admin.register(ShareholdersHistory)
class ShareholderAdmin(admin.ModelAdmin):
    list_display = (
        'shareholder_name',
        'symbol',
        'shareholder_percentage',
        'date',
        'change',
        'shareholder_instrument_id',
    )
    
    list_filter = (
        'symbol',
        ('date', admin.DateFieldListFilter),
        ('shareholder_percentage', admin.ChoicesFieldListFilter),
        'change',
    )
    
    search_fields = (
        'shareholder_name',
        'symbol',
    )
    
    list_per_page = 50
    date_hierarchy = 'date'
    ordering = ('-date', '-shareholder_percentage')

