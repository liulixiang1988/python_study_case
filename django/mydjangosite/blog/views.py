from django.shortcuts import render, get_object_or_404

from .models import Post, Category


def index(request):
    """Blog 列表"""
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'posts': posts, 'categories': categories})


def post(request, pk):
    """单篇文章"""
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.all()
    return render(request, 'blog/post.html', {'post': post, 'categories': categories})


def category(request, pk):
    """文章分类"""
    cat = get_object_or_404(Category, pk=pk)
    posts = cat.post_set.all()
    return render(request, 'blog/index.html', {'posts': posts, 'categories': Category.objects.all(),
                                               'is_category': True, 'cat_name': cat.name})

