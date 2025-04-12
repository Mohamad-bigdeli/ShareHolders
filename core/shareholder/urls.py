from django.urls import path, include

app_name = "shareholder"

urlpatterns = [
    path("api/v1/", include("shareholder.api.v1.urls", namespace="api-v1"))
]