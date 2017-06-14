from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post


def post_list(request):
    post = Post.objects.order_by('-created_time')
    # post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'post/post_list.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        post.delete()

    return redirect('post_list')