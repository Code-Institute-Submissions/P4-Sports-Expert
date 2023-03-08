from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Profile
from blog.models import BlogPost


class ProfileView(ListView):
    model = Profile
    template_name = 'profile.html'