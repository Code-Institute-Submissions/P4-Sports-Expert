from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField

CATEGORY = (
    ('Football', 'Football'),
    ('GAA', 'GAA'),
    ('Rugby', 'Rugby'),
)


class BlogPost(models.Model):
    """
    Database model for blogposts
    """
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    blog_image = CloudinaryField('image', default='placeholder')
    body = models.TextField()
    category = models.CharField(
        max_length=10, choices=CATEGORY, default='Football'
        )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"Blog post by {self.created_by} on {self.date_created}"

    def get_absolute_url(self):
        return reverse('home')


class Comments(models.Model):
    """
    Database model for comments
    """
    post = models.ForeignKey(
        BlogPost, related_name="comments", on_delete=models.CASCADE,
        )
    comment = models.TextField(null=True, blank=False)
    time = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user} on {self.time}"
