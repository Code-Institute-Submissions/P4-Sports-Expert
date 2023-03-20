from django.forms import ModelForm
from .models import BlogPost, Comments
from django import forms
from django_summernote.widgets import SummernoteWidget
from cloudinary.forms import CloudinaryFileField


class BlogForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True

    class Meta:
        model = BlogPost
        blog_image = forms.ImageField()
        fields = (
            'created_by', 'description', 'title', 
            'blog_image', 'body', 'category'
            )
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentForm(ModelForm):

    class Meta:
        model = Comments
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }


