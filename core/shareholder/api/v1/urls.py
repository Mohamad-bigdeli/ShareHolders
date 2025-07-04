from __future__ import annotations

from django.urls import path

from . import views


app_name = "api-v1"

urlpatterns = [
    path("shareholders/<str:symbol>/", views.ShareholdersListAPIView.as_view(), name="shareholders-list"),
    path("shareholders/changes/daily/<str:symbol>", views.ShareholdersDailyChangesApiView.as_view(), name="shareholders-change-daily"),
    path("shareholders/changes/weekly/<str:symbol>", views.ShareholdersWeeklyChangesApiView.as_view(), name="shareholders-change-weekly"),
    path("shareholders/changes/monthly/<str:symbol>", views.ShareholdersMonthlyChangesApiView.as_view(), name="shareholders-change-monthly"),
    path("shareholders/search/<str:query>", views.ShareholdersSearchApiView.as_view(), name="shareholders-search")
]

