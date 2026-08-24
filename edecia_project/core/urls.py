from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
]
