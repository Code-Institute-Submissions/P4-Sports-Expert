from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost


class BlogList(ListView):
    model = BlogPost
    template_name = 'blog_home.html'


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    

