from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from cloudinary.forms import cl_init_js_callbacks
from .models import BlogPost, Comments
from .forms import BlogForm


class BlogList(ListView):
    model = BlogPost
    template_name = 'blog_home.html'
    paginate_by = 6


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'


class AddBlog(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = BlogPost
    template_name = 'add_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('bloglist')
    success_message = "Blog post created."

    def get_initial(self):
        return {'created_by': self.request.user}


class AddComment(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comments
    template_name = 'add_comment.html'
    success_url = reverse_lazy('bloglist')
    success_message = "Comment added."       


class EditBlog(SuccessMessageMixin, UpdateView):
    model = BlogPost
    template_name = 'edit_blog.html'
    fields = ['description', 'title', 'blog_image', 'body', 'category']
    success_url = reverse_lazy('bloglist')
    success_message = "Blog post edited successfully"


class DeleteBlog(DeleteView):
    model = BlogPost
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('bloglist')
    success_message = "Blog post deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBlog, self).delete(request, *args, **kwargs)


def CategoryView(request, cats):
    category_posts = BlogPost.objects.filter(category=cats)
    context = {
        'cats': cats,
        'category_posts': category_posts
    }
    return render(request, 'categories.html', context)    
