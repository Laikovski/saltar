from django.contrib import admin
from .models import Profile, Work

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'car_number']

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Work)

