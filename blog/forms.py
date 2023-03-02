from django.forms import ModelForm
from .models import BlogPost
from django import forms


class BlogForm(ModelForm):
    
    class Meta:
        model = BlogPost
        fields = '__all__'