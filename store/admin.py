from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import Category, Gig

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ['name']

@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ['get_username', 'get_image', 'name', 'get_price', 'category']

    def get_price(self, instance):
        try:
            return f"{instance.get_basic_package.price} $"
        except:
            return None
    get_price.short_description = 'Starting Price'

    def get_username(self, instance):
        return instance.profile.user.username
    get_username.short_description = 'User'

    def get_image(self, instance):
        return format_html('<img src="{}" width="200px"/>'.format(instance.image.url))
    get_image.short_description = 'Image'
