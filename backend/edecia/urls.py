"""
URL configuration for edecia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from content.views import service_page, about_view, blog_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('content.urls')),
    path('', TemplateView.as_view(template_name='edecia/index.html'), name='index'),
    path('about/', about_view, name='about'),
    path('service/', service_page, name='service'),
    path('blog/', blog_view, name='blog'),
    path('contact/', contact_view, name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
