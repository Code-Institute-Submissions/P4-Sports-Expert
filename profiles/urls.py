from django.urls import path
from .views import profile, MyBlogs, EditProfile


urlpatterns = [
    path("profile/<username>/", profile, name="profile"),
    path("profile/myblogs", MyBlogs.as_view(), name="myblogs"),
    path('edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),
]