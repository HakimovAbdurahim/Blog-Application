from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
# Project
from .models import Post
from .forms import EmailPostForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post/list.html'


def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.published.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404('No Post found')
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post, publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'post/detail.html', {'post': post})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

    else:
        form = EmailPostForm()
    return render(request, 'post/share.html', {'post': post, 'form': form})
