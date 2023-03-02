from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost


class BlogList(ListView):
    model = BlogPost
    template_name = 'blog_home.html'

