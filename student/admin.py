from django.contrib import admin
from MainApp.models import Students

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname']

admin.site.register(Students,StudentAdmin)