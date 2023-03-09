from django.urls import path
from .views import profile


urlpatterns = [
    path(
        "profile/<username>/",
        profile,
        name="profile",
    ),
]