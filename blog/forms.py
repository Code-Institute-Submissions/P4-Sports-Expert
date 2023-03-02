from django.forms import ModelForm
from .models import BlogPost
from django import forms


class BlogForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True

    class Meta:
        model = BlogPost
        fields = (
            'created_by', 'description', 'title', 
            'blog_image', 'body', 'category'
            )
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
