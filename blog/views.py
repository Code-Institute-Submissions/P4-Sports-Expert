from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponseForbidden
from .models import BlogPost
from .forms import BlogForm


class BlogList(ListView):
    model = BlogPost
    template_name = 'blog_home.html'


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'


class AddBlog(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'add_blog.html'
    form_class = BlogForm

    def get_initial(self):
        return {'created_by': self.request.user}


class EditBlog(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = 'edit_blog.html'
    fields = ['description', 'title', 'blog_image', 'body', 'category']

    def dispatch(self, request, *args, **kwargs):
        handler = super(EditBlog, self).dispatch(request, *args, **kwargs)
        if self.object.created_by != request.user:
            return HttpResponseForbidden("You are not the owner of this blog")
            return handler
        else:
            return handler