from django.forms import ModelForm
from .models import Profile
from django import forms
from cloudinary.forms import CloudinaryFileField


class ProfileForm(ModelForm):
    """
    Profile modelform
    """
    def __init__(self, *args, **kwargs):
        """
        Disables user select on profile form
        """
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    class Meta:
        """
        Form fields and widgets
        """
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
