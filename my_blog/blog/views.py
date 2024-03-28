from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id_):
    post = get_object_or_404(Post, id=id_, status=Post.status.PUBLISHED)

    return render(request, 'blog/post/detail.html', {'post': post})

# Create your views here.
