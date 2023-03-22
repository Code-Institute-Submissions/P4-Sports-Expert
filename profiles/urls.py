from django.urls import path
from .views import ProfileView, MyBlogs, EditProfile


urlpatterns = [
    path("myprofile/<username>/", ProfileView.as_view(), name="profile"),
    path("myprofile/myblogs", MyBlogs.as_view(), name="myblogs"),
    path('edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),
]