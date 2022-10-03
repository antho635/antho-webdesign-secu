from django.contrib import admin
from .models import Language, ProjectList


class ProjectListAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'project_status', 'project_date_created_on']
    list_filter = ['project_status']
    ordering = ['-project_date_created_on']


# Register your models here.
admin.site.register(Language)
admin.site.register(ProjectList, ProjectListAdmin)
