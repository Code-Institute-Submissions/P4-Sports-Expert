from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile


class ProfileView(ListView):
    model = Profile
    template_name = 'profile.html'


