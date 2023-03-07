from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from cloudinary.forms import cl_init_js_callbacks
from .models import BlogPost
from .forms import BlogForm


class BlogList(ListView):
    model = BlogPost
    template_name = 'blog_home.html'


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'


class AddBlog(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = BlogPost
    template_name = 'add_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('bloglist')
    success_message = "Blog post created successfully"

    def get_initial(self):
        return {'created_by': self.request.user}


class EditBlog(SuccessMessageMixin, UpdateView):
    model = BlogPost
    template_name = 'edit_blog.html'
    fields = ['description', 'title', 'blog_image', 'body', 'category']
    success_url = reverse_lazy('bloglist')
    success_message = "Blog post edited successfully"


class DeleteBlog(SuccessMessageMixin, DeleteView):
    model = BlogPost
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('bloglist')
