from django.urls import path
from .views import ProfileView, AddProfile


urlpatterns = [
    path('', ProfileView.as_view(), name="profileview"),
    path('add_profile/', AddProfile.as_view(), name='add_profile')
]