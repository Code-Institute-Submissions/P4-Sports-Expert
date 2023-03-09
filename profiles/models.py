from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from blog.models import BlogPost

# Create your models here.
placeholder = (
    "https://res.cloudinary.com/dsdurzeu2/image/upload/v1678279560/profile-placeholder_bkm8nk.webp"
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=200, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
