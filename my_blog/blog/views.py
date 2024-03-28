from django.shortcuts import render
from django.http import Http404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id_):
    try:
        post = Post.published.get(id=id_)
    except Post.DoesNotExist:
        raise Http404

    return render(request, 'blog/post/list-detail.html', {'post': post})

# Create your views here.
