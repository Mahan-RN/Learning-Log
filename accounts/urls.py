"""Defines URL patterns for accounts"""

from django.urls import path, include

app_name = "accounts"
urlpatterns = [
    # Include default authentication urls
    path("", include("django.contrib.auth.urls")),
]
