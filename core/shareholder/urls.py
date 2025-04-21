from __future__ import annotations

from django.urls import include, path


app_name = "shareholder"

urlpatterns = [
    path("api/v1/", include("shareholder.api.v1.urls", namespace="api-v1"))
]