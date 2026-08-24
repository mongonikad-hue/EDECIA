from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from .models import Service, AboutPage, BlogPost, Contact
from .serializers import ServiceSerializer, AboutPageSerializer, BlogPostSerializer, ContactSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


def service_page(request):
    type_filter = request.GET.get('type')
    services = Service.objects.all().order_by('-updated_at')
    if type_filter and type_filter != 'all':
        services = services.filter(service_type=type_filter)
    return render(request, 'edecia/service.html', {'services': services, 'selected_type': type_filter or 'all'})

def about_view(request):
    team_members = AboutPage.objects.filter(is_active=True)
    return render(request, 'edecia/about.html', {'team_members': team_members})

def blog_view(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'edecia/blog.html', {'posts': posts})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        messages.success(request, 'Message reçu !')
        return redirect('contact')
    return render(request, 'edecia/contact.html')

class AboutPageViewSet(viewsets.ModelViewSet):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
