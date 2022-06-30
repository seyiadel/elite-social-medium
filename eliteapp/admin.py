from django.contrib import admin
from .models import UserProfile, Feedpost

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Feedpost)