from django.contrib import admin
from .models import Applicants,user_profiles

# Register your models here.
admin.site.register(Applicants)
admin.site.register(user_profiles)