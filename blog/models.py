from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from cloudinary.models import CloudinaryField

CATEGORY = (
    ('Football', 'Football'),
    ('GAA', 'GAA'),
    ('Rugby', 'Rugby'),
)


class BlogPost(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
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




