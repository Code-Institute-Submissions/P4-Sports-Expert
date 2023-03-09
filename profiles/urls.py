from django.urls import path
from .views import profile, MyBlogs


urlpatterns = [
    path("profile/<username>/", profile, name="profile"),
    path("profile/myblogs", MyBlogs.as_view(), name="myblogs")
]