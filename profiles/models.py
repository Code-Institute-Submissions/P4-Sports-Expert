from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from blog.models import BlogPost

# Create your models here.
placeholder = (
    "https://res.cloudinary.com/dsdurzeu2/image/upload/v1678279560/profile-placeholder_bkm8nk.webp")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=200, null=True, blank=True)
    blogs = models.ManyToManyField(BlogPost, blank=True, related_name='blogs')
    image = CloudinaryField('image', default='placeholder')
