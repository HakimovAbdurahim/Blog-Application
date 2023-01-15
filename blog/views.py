from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Project
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'post/list.html', {'posts': posts})


def post_detail(request, pk):
    # try:
    #     post = Post.published.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404('No Post found')
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)

    return render(request, 'post/detail.html', {'post': post})
