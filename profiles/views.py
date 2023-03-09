from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Profile
from blog.models import BlogPost
from .forms import ProfileForm


class ProfileView(ListView):
    model = Profile
    template_name = 'profile.html'


class AddProfile(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Profile
    template_name = 'add_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profileview')
    success_message = "Profile created successfully"

    def get_initial(self):
        return {'created_by': self.request.user}