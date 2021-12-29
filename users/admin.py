from django.contrib import admin
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ['user', 'role', 'country']
