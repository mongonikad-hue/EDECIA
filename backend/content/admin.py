from django.contrib import admin
from .models import Service, AboutPage, BlogPost, Contact


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('title', 'service_type', 'price_basic', 'price_premium', 'updated_at')
	search_fields = ('title', 'description')


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'role', 'bio')


admin.site.register(BlogPost)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'subject', 'created_at')
    search_fields = ('name', 'email', 'message')

