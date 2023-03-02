from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost
from .forms import BlogForm


class BlogList(ListView):
    model = BlogPost
    template_name = 'blog_home.html'


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'


class AddBlog(CreateView):
    model = BlogPost
    template_name = 'add_blog.html'
    form_class = BlogForm