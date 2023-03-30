from django.urls import path
from .views import ProfileView, MyBlogs, EditProfile, DeleteProfile


urlpatterns = [
    path("myprofile/<username>/", ProfileView.as_view(), name="profile"),
    path("myprofile/myblogs", MyBlogs.as_view(), name="myblogs"),
    path('edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),
    path(
        'delete_profile/<int:pk>',
        DeleteProfile.as_view(),
        name='delete_profile'
        ),
]
