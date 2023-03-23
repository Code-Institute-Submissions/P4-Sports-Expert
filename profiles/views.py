from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Profile
from blog.models import BlogPost
from .forms import ProfileForm
from django.contrib.auth.models import User


class ProfileView(DetailView):
    """
    Renders profile page view
    """
    model = Profile
    template_name = 'profile.html'

    def get(self, request, username):
        """
        Overides get method. Checks that profile user is current
        logged in user using username
        """
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)

        context = {
            "profile": profile,
        }

        return render(request, self.template_name, context)


class MyBlogs(ListView):
    """
    Renders a list of all user blogs
    """
    model = BlogPost
    template_name = 'myblogs.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Overides get queryset method,
        links logged in user to blog post created_by
        field and returns filtered blogs
        """
        user = self.request.user
        return BlogPost.objects.filter(created_by=user)


class EditProfile(SuccessMessageMixin, UpdateView):
    """
    Renders form for editing profile
    """
    model = Profile
    template_name = 'edit_profile.html'
    form_class = ProfileForm
    success_message = "Profile edited successfully"

    def get_success_url(self):
        """
        Overrides get succes url method.
        Redirects user to their profile page when
        form is posted
        """
        return reverse('profile', args=[self.request.user.username])
