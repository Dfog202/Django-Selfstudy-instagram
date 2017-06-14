from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User)
    photo = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(
        User,
        related_name='like_posts',
        through='PostLike',
    )

class Comment(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)