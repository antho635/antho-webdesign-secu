from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


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
