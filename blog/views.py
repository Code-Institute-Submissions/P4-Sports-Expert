from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from cloudinary.forms import cl_init_js_callbacks
from .models import BlogPost, Comments
from .forms import BlogForm, CommentForm


class BlogList(ListView):
    """
    Renders a list view of blogposts
    """
    model = BlogPost
    template_name = 'blog_home.html'
    paginate_by = 6


class BlogDetail(DetailView):
    """
    Renders a detailview of a single blogpost
    """
    model = BlogPost
    template_name = 'blog_detail.html'
    form = CommentForm

    def post(self, request, *args, **kwargs):
        """
        Overides post method, gives user success
        message and redirects them back to the
        same page.
        """
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            messages.success(
                request, "Your comment has been added"
            )
            return HttpResponseRedirect(
                reverse('blog_detail', kwargs={'pk': post.pk})
                )
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """
        Overides context data method to get post i.d and
        link to comment form
        """
        self.object = self.get_object()
        comments = Comments.objects.filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'comments': comments
        })
        return context


class DeleteComment(DeleteView, SuccessMessageMixin):
    """
    View for deleting a comment
    """
    model = Comments
    template_name = 'delete_comment.html'
    success_message = "Your comment has been deleted"

    def delete(self, request, *args, **kwargs):
        """
        Overides delete method and gives user
        success message
        """
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Overides get success url method,
        gets blog post id and redirects user
        there
        """
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.post_id})


class EditComment(SuccessMessageMixin, UpdateView):
    """
    Model for editing comment
    """
    model = Comments
    template_name = "edit_comment.html"
    fields = ['comment']
    success_message = "Your comment has been edited"

    def get_success_url(self):
        """
        Overides get success url method,
        gets blog post id and redirects user
        there
        """
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.post_id})


class AddBlog(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View to add a blog
    """
    model = BlogPost
    template_name = 'add_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('bloglist')
    success_message = "Blog post created."

    def get_initial(self):
        """
        Pre populates created by field with
        current logged in user
        """
        return {'created_by': self.request.user}


class EditBlog(SuccessMessageMixin, UpdateView):
    """
    View for editing a blog post
    """
    model = BlogPost
    template_name = 'edit_blog.html'
    fields = ['description', 'title', 'blog_image', 'body', 'category']
    success_url = reverse_lazy('bloglist')
    success_message = "Blog post edited successfully"


class DeleteBlog(DeleteView):
    """
    View for deleting a blog post
    """
    model = BlogPost
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('bloglist')
    success_message = "Blog post deleted successfully"

    def delete(self, request, *args, **kwargs):
        """
        Overides delete method and gives user
        success message
        """
        messages.success(self.request, self.success_message)
        return super(DeleteBlog, self).delete(request, *args, **kwargs)
