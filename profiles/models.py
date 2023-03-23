from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField
from blog.models import BlogPost
from django.dispatch import receiver

# Create your models here.
placeholder = (
    "bit.ly/3JXQzON"
    )


class Profile(models.Model):
    """
    Database model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50, null=True, blank=True, default="Enter your full name"
        )
    about = models.TextField(
        max_length=200, null=True, blank=True, default="Tell us about yourself"
    )
    image = CloudinaryField('image', default='placeholder')
    blogs = models.ManyToManyField(
        BlogPost, related_name="blogs", blank=True,
    )
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns user profile username
        in admin page
        """
        return self.user.username
