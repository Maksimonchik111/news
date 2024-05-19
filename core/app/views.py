from django.shortcuts import render
from .models import Post


def post_list(request):
    post = Post.objects.all()

    return render(request, 'app/index.html', {'post': post})


def post_detail(request, pk):
    posts = Post.objects.get(id=pk)

    return render(request, 'app/post_detail.html', {posts: 'posts'})
