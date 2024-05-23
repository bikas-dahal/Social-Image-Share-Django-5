# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # tags = models.ManyToManyField('Tag', related_name='posts')
    # categories = models.ManyToManyField('Category', related_name='posts')
    # views = models.IntegerField(default=0)
    # likes = models.ManyToManyField(User, related_name='liked_posts')
    # dislikes = models.ManyToManyField(User, related_name='disliked_posts')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_comments')
    dislikes = models.ManyToManyField(User, related_name='disliked_comments')
    
    def __str__(self):
        return self.content