from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
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
    # Checks if logged in user is owner of the post and has permission to edit

    def dispatch(self, request, *args, **kwargs):
        handler = super(EditBlog, self).dispatch(request, *args, **kwargs)
        if self.object.created_by != request.user:
            return HttpResponseForbidden("You are not the owner of this blog")
            return handler
        else:
            return handler


class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')
