from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    price_basic = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_premium = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    SERVICE_TYPE_CHOICES = [
        ('formation', 'Formation'),
        ('produit', 'Produit digital'),
        ('service', 'Service'),
    ]
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES, default='service')
  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class AboutPage(models.Model):
    name = models.CharField(max_length=100, default='')
    role = models.CharField(max_length=100, default='')
    bio = models.TextField(default='')
    photo = models.ImageField(upload_to="team/", blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('formation', 'Inscription à une Formation'),
        ('service', 'Demande de Service Créatif / Tech'),
        ('produit', 'Achat de Produit Digital'),
        ('autre', 'Autre'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True, null=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='service')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"