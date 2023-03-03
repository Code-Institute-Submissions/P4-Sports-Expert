from django.shortcuts import render
from django.views.generic import ListView
from blog.models import BlogPost


# Create your views here.

class HomeView(ListView):
    model = BlogPost
    template_name = 'index.html'
