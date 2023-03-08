from django.forms import ModelForm
from .models import Profile
from django import forms
from cloudinary.forms import CloudinaryFileField


class ProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    class Meta:
        model = Profile
        image = forms.ImageField()
        fields = (
            'user', 'name', 'about', 
            'image',
            )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
        }    
