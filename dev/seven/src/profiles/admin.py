from django.contrib import admin

# Register your models here.

from .models import Profile

class ProfileAdmin(admin.ModelAdmin) :
    class meta :
        model = Profile

admin.site.register(Profile,ProfileAdmin)