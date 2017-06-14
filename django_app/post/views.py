from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_time')
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)