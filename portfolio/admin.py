from django.contrib import admin
from .models import Category, Project, ProjectAdmin

# Register your models here.
admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
