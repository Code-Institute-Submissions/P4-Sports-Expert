from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Profile
from blog.models import BlogPost
from .forms import ProfileForm
from django.contrib.auth.models import User


@login_required()
def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    profile = Profile.objects.get(user=user)

    context = {
        "profile": profile,
    }

    return render(request, "profile.html", context)
