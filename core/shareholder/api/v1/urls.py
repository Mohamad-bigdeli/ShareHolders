from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()

router.register(r'shareholders/search', views.ShareholdersDocumentViewSet, basename='shareholders-search')

urlpatterns = [
    path("shareholders/<str:symbol>/", views.ShareholdersListAPIView.as_view(), name="shareholders-list"),
]

urlpatterns+=router.urls
