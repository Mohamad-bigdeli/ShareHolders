from django.urls import path
from . import views

app_name = "api-v1"

urlpatterns = [
    path("/shareholders/<str:symbol>/", views.ShareholdersListAPIView.as_view(), name="shareholders-list")
]