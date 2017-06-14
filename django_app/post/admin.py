from django.contrib import admin

# Register your models here.
from post.models import Post, PostLike, Comment, User

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostLike)
admin.site.register(User)