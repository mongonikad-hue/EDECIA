from django.urls import path, include
from rest_framework.routers import DefaultRouter                                
from .views import ServiceViewSet, AboutPageViewSet, BlogPostViewSet,ContactViewSet

router = DefaultRouter()

router.register(r'services', ServiceViewSet)
router.register(r'blog', BlogPostViewSet)
router.register(r'about', AboutPageViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

