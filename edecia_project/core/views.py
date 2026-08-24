from django.shortcuts import render, get_object_or_404
from .models import Blog, Product


def index(request):
    products = Product.objects.all()[:6]
    return render(request, 'core/index.html', {'products': products})


def about(request):
    return render(request, 'core/about.html')


def blog_list(request):
    posts = Blog.objects.order_by('-created_at')
    return render(request, 'core/blog.html', {'posts': posts})


def service(request):
    return render(request, 'core/service.html')


def contact(request):
    return render(request, 'core/contact.html')
