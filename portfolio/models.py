from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=2500, blank=True, null=True)

    date_send = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_send']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_send']
    list_filter = ['date_send']
    ordering = ['-date_send']


# Langages
class Language(models.Model):
    language_name = models.CharField(max_length=120, blank=True, null=True)
    image_language = models.ImageField(upload_to='portfolio/images/languages', blank=True, null=True)

    # slug_language = models.SlugField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.language_name

    class Meta:
        ordering = ['language_name']


PROJECT_STATUS = [
    (0, "En cours"),
    (1, "En ligne")
]


class ProjectList(models.Model):
    project_title = models.CharField(max_length=200, unique=True)
    project_slug = models.SlugField(max_length=200, unique=True)
    project_description = models.TextField()
    project_date_created_on = models.DateTimeField(auto_now_add=True)
    project_status = models.IntegerField(choices=PROJECT_STATUS, default=0)
    language_tags = models.CharField(max_length=50)
    project_thumbnail = models.ImageField(upload_to='images/portfolio/project/',
                                          default='images/portfolio/project/indispo.png')

    class Meta:
        ordering = ['-project_date_created_on']

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse("ProjectListView", kwargs={"slug": self.project_slug})
