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
    model = Profile
    template_name = 'profile.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)

        context = {
            "profile": profile,
        }

        return render(request, self.template_name, context)


class MyBlogs(ListView):
    model = BlogPost
    template_name = 'myblogs.html'
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        return BlogPost.objects.filter(created_by=user)


class EditProfile(SuccessMessageMixin, UpdateView):
    model = Profile
    template_name = 'edit_profile.html'
    form_class = ProfileForm
    success_message = "Profile edited successfully"
    success_url = reverse_lazy('home')

